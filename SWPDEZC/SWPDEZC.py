"""
Pronósticos de Demanda de Energía por Zona de Carga
https://www.cenace.gob.mx/Paginas/SIM/Reportes/PronosticosDemanda.aspx
"""

import psycopg2 as pg2
import os
import pandas as pd
import json
from datetime import date


DB_NAME = os.environ['DB_NAME']
DB_TABLE = os.environ['DB_TABLE']
DB_HOST = os.environ['DB_HOST']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']


def check_data(system, market, zonas_carga, year_start, month_start, day_start, year_end, month_end, day_end):
    """Basic check of entered variables"""

    return all([
        system in ["SIN","BCA","BCS"],
        market == 'MTR',
        zonas_carga != "",
        len(year_start) == 4,
        len(month_start) == 2,
        len(day_start) == 2,
        len(year_end) == 4,
        len(month_end) == 2,
        len(day_end) == 2])

def postgres_password():
    """Returns required parameters to connect to RDS instance"""

    params = {
    'host':DB_HOST,
    'user':DB_USER,
    'password':DB_PASSWORD,
    'port':5432,
    'database':DB_NAME
    }

    return params


def format_df(df):
    """Formats DataFrame columns to required string format"""

    df['fecha'] = df['fecha'].apply(lambda x: date.strftime(x, r"%Y-%m-%d"))
    df['hora'] = df['hora'].astype(str)
    df['energia'] = df['energia'].astype(str)
    
    return df


def request_to_db(cursor, DB_TABLE, zonas_carga, date_start, date_end):
    """Makes a query to db with selected options, returns clean DataFrame"""

    cursor.execute("""
        SELECT * FROM {}
        WHERE zona_de_carga IN ('{}') AND
            fecha >= '{}' AND
            fecha <= '{}'
        ORDER BY
            zona_de_carga ASC, 
            fecha ASC,
            hora ASC
        ;""".format(DB_TABLE,zonas_carga, date_start, date_end))

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
    zonas_carga = event['zonas_carga']
    year_start = event['year_start']
    month_start = event['month_start']
    day_start = event['day_start']
    year_end = event['year_end']
    month_end = event['month_end']
    day_end = event['day_end']
    format = event['format'] # Not used for now
    
    # Check of entered variables
    if not check_data(system, market, zonas_carga, year_start, month_start, day_start, year_end, month_end, day_end):
        return json.dumps("Error: Datos incorrectos.")    

    # Prepare zones and dates for query
    zonas_carga = zonas_carga.replace(",","','")
    date_start = f"{year_start}-{month_start}-{day_start}"
    date_end = f"{year_end}-{month_end}-{day_end}"
    
    # Connect to RDS and request information
    with pg2.connect(**postgres_password()) as conn:
        cursor = conn.cursor()
        df = request_to_db(cursor, DB_TABLE, zonas_carga, date_start, date_end)

    # Check if DataFrame is empty
    status = check_status(df)    
     
    response = {
        "status":status,
        "nombre":"Pronóstico de Demanda de Energía por Zona de Carga",
        "proceso":market,
        "sistema":system,
        "area":"Open Source Project https://github.com/AngelCarballoCremades/CENACE-RDS-API",
        "Resultados":{}
    }

    # Format response json to fit CENACE APIs format
    for i,zona in enumerate(zonas_carga.split("','")):

        values = df.loc[df['zona_de_carga'] == zona][['fecha','hora','energia']].reset_index(drop=True).to_json(orient='index')
        response["Resultados"][i] = {"zona_carga":zona,"Valores":json.loads(values)}
    
    return response