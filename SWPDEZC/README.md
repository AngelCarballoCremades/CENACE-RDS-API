# Servicio Web para la descarga de Pronóstico de Demanda de Energía por Zona de Carga (SW-PDEZC)

## Consideraciones

1. El uso del presente Servicio Web es exclusivamente para la descarga de información de la [Pronóstico de Demanda de Energía por Retiros](https://www.cenace.gob.mx/Paginas/SIM/Reportes/PronosticosDemanda.aspx) del modelo AU-GC.
2. Se consideran pronósticos realizados el día anterior al día de operación (no se toman en cuenta pronósticos realizados los días anteriores).
3. El SW-PDEZC es un proyecto abierto y para uso del público en general.
4. En caso de observar alguna falla en los datos o funcionamiento del servicio o si tienes alguna sugerencia, levanta un *Issue* en Github o mándame un mensaje directo en [Linkedin](https://www.linkedin.com/in/angelcarballo/).

## Descripción del SW-PDEZC
Según el CENACE: *Para cada hora del Día de Operación correspondiente el CENACE pronostica la demanda que se espera para el Mercado del Día en Adelanto (MDA), de acuerdo con las ofertas de compra que envían los Participantes del Mercado. Para el proceso de Asignación Suplementaria de Unidades de Central Eléctrica para Confiabilidad (AUGC), el CENACE pronostica la demanda de cada Zona de Carga para los siguientes siete Días de Operación*.

La información se encuentra disponible al público aproximadamente 1 día antes del Día de Operación correspondiente.

## Método y formato de invocación del SW-PDEZC
El Servicio Web está basado en el estilo arquitectónico "REST" (en inglés, REpresentation State Transfer). En la invocación del SW-PDEZC se utiliza el método GET para obtener información de un recurso.
El formato de invocación del SW-PDEZC es:
**https://api.energia-mexico.org/SWPDEZC/parámetros**

* Parámetros para la invocación del SW-PDEZC
    * **SISTEMA** - Sistema Interconectado [SIN, BCA, BCS].
    * **PROCESO** - Proceso [MDA-AUGC].
    * **ZONAS DE CARGA** - Lista de Zonas de Carga.
    * **AÑO INICIAL** - Año inicial del periodo. Formato AAAA.
    * **MES INICIAL** - Mes inicial del periodo. Formato MM.
    * **DÍA INICIAL** - Día inicial del periodo. Formato DD.
    * **AÑO FINAL** - Año final del periodo. Formato AAAA.
    * **MES FINAL** - Mes final del periodo. Formato MM.
    * **DÍA FINAL** - Día final del periodo. Formato DD.
    * **FORMATO** - Formato de Salida [JSON].


* Todos los parámetros son obligatorios.
* Cada uno de los parámetros deberá separarse por el caracter reservado (/).
* La lista de Zonas de Carga deberá separarse por comas, sin espacios.
* La lista de Zonas de Carga podrá considerar de 1 a 10 Zonas de Carga para la consulta.
* En los nombres de las Zonas de Carga que se incluyan en la consulta deberán remplazarse los espacios por el símbolo "-" (guión). Por ejemplo, la Zona de Carga "CENTRO ORIENTE" se deberá especificar como "CENTRO-ORIENTE".
* Los días para los cuales se realiza la solicitud, corresponden a Días de Operación del MEM.
* La información se encuentra disponible a partir del 10 de enero del 2019.
* La información se actualiza varias veces a la semana.
* El periodo de consulta podrá considerar de 1 a 200 Días de Operación.
* La información oficial sobre el Pronóstico de Demanda de Energía se publica diariamente en el Área Pública del SIM, en la siguiente liga:
https://www.cenace.gob.mx/Paginas/SIM/Reportes/PronosticosDemanda.aspx

## Información que devuelve la invocación del SW-PDEZC

* **status** - Estado de la respuesta [OK, ZERO_RESULTS].
* **nombre** - Nombre del reporte [Pronóstico de Demanda de Energía por Zona de Carga].
* **proceso** - Proceso [MDA-AUGC].
* **sistema** - Sistema Interconectado [SIN, BCA o BCS].
* **area** - Origen de la API [Open Source Project https://github.com/AngelCarballoCremades/energia-mexico-REST-API].
* **zona_carga** - Zona de Carga.
* **fecha** - Día de Operación.
* **hora** - Hora de Operación.
* **energia** - Pronóstico de Demanda de Energía en MWh.

## Ejemplo de invocación del SW-PDEZC
Para obtener información de la Pronóstico de Demanda de Energía para las Zonas de Carga "OAXACA y CENTRO ORIENTE" del Sistema Interconectado Nacional, correspondiente al Día de Operación 20 de enero de 2020, en formato de salida JSON.

La invocación del SW-PDEZC sería de la siguiente manera:

https://api.energia-mexico.org/SWPDEZC/SIN/MDA-AUGC/OAXACA,CENTRO-ORIENTE/2020/01/20/2020/01/20/JSON