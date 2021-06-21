"""
Pronósticos de Generación Intermitente
https://www.cenace.gob.mx/Paginas/SIM/Reportes/H_PronosticosGeneracion.aspx?N=245&opc=divCssPronosticosGen&site=Pron%C3%B3sticos%20de%20Generaci%C3%B3n%20Intermitente&tipoArch=C&tipoUni=ALL&tipo=All&nombrenodop=
"""

import psycopg2 as pg2
import os
import pandas as pd
import json
from datetime import date, datetime


DB_NAME = os.environ["DB_NAME"]
DB_TABLE = os.environ["DB_TABLE"]
DB_HOST = os.environ["DB_HOST"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]


def check_data(system, market, year_start, month_start, day_start, year_end, month_end, day_end):
    """Basic check of entered variables"""

    return all([
        system in ["SIN","BCA","BCS"],
        market == "MDA",
        len(year_start) == 4,
        year_start.isnumeric(),
        len(month_start) == 2,
        month_start.isnumeric(),
        len(day_start) == 2,
        day_start.isnumeric(),
        len(year_end) == 4,
        year_start.isnumeric(),
        len(month_end) == 2,
        month_start.isnumeric(),
        len(day_end) == 2,
        day_end.isnumeric()])

def postgres_password():
    """Returns required parameters to connect to RDS instance"""

    params = {
    "host":DB_HOST,
    "user":DB_USER,
    "password":DB_PASSWORD,
    "port":5432,
    "database":DB_NAME
    }

    return params


def format_df(df):
    """Formats DataFrame columns to required string format"""

    df.drop(columns=["sistema"], inplace=True)
    df["fecha"] = df["fecha"].apply(lambda x: date.strftime(x, r"%Y-%m-%d"))
    df = df.applymap(str)
    df.set_index(["fecha","hora"], inplace=True)
    df = df.stack().reset_index()
    df.columns = ["fecha","hora","tecnologia","energia"]

    return df


def request_to_db(cursor, DB_TABLE, system, date_start, date_end):
    """Makes a query to db with selected options, returns clean DataFrame"""

    cursor.execute("""
        SELECT * FROM {}
        WHERE
            sistema = '{}' AND
            fecha >= '{}' AND
            fecha <= '{}'
        ORDER BY
            fecha ASC,
            hora ASC
        ;""".format(DB_TABLE, system, date_start, date_end))

    colnames = [desc[0] for desc in cursor.description] # Get column names from cursor
    df = pd.DataFrame(data=cursor.fetchall(), columns=colnames)
    df = format_df(df)

    return df


def check_status(df):
    """Checks if DataFrame is empty, returns status string 'OK' or 'ZERO_RESULTS'"""

    if df.size == 0:
        return "ZERO_RESULTS"
    else:
        return "OK"


def lambda_handler(event, context):
    """Main function to be executed"""
    
    # Extract variables from 'event'
    system = event['system']
    market = event['market']
    year_start = event['year_start']
    month_start = event['month_start']
    day_start = event['day_start']
    year_end = event['year_end']
    month_end = event['month_end']
    day_end = event['day_end']
    format = event['format'] # Not used for now
    
    # Check of entered variables
    if not check_data(system, market, year_start, month_start, day_start, year_end, month_end, day_end):
        return {"Message":"Datos incorrectos"}      

    # Prepare zones and dates for query
    date_start = f"{year_start}-{month_start}-{day_start}"
    date_end = f"{year_end}-{month_end}-{day_end}"
    delta = datetime.strptime(date_end, r"%Y-%m-%d") - datetime.strptime(date_start, r"%Y-%m-%d")

    # End date must be greater than start date and difference must be at most 200 days
    if delta.days > 200 or 0 > delta.days:
        return {"Message":"Fechas inválidas"}
    
    # Connect to RDS and request information
    with pg2.connect(**postgres_password()) as conn:
        cursor = conn.cursor()
        df = request_to_db(cursor, DB_TABLE, system, date_start, date_end)

    # Check if DataFrame is empty
    status = check_status(df)    

    generation_types = df["tecnologia"].unique().tolist()
         
    response = {
        "status":status,
        "nombre":"Pronóstico de Generación Intermitente",
        "proceso":market,
        "sistema":system,
        "area":"Open Source Project https://github.com/AngelCarballoCremades/energia-mexico-REST-API",
        "Resultados":generation_types
    }

    # Format response json to fit CENACE APIs format
    for i,gen_type in enumerate(generation_types):

        values = json.loads(df.loc[df['tecnologia'] == gen_type][['fecha','hora','energia']].reset_index(drop=True).to_json(orient='index'))
        values = list(values.values())
        response["Resultados"][i] = {"tecnologia":gen_type,"Valores":values}

    return response