# Servicio Web para la descarga de Energía Generada por Tipo de Tecnología (SW-EGTT)

## Consideraciones

1. El uso del presente Servicio Web es exclusivamente para la descarga de información de la [Energía Generada por Tipo de Tecnología](https://www.cenace.gob.mx/Paginas/SIM/Reportes/EnergiaGeneradaTipoTec.aspx) en el Sistema Eléctrico Nacional.
2. Se consideran únicamente Liquidaciones 0 (Cuando no hay Liquidaciones 0 puede que se muestre información de Re-Liquidaciones 1)
3. El SW-EGTT es un proyecto abierto y para uso del público en general.
4. En caso de observar alguna falla en los datos o funcionamiento del servicio o si tienes alguna sugerencia, levanta un *Issue* en Github o mándame un mensaje directo en [Linkedin](https://www.linkedin.com/in/angelcarballo/).

## Descripción del SW-EGTT
Según el CENACE: *Se presenta la estadística de generación intermitente y firme a nivel agregado. Integra los valores históricos y pronosticados de la generación de energía por tipo de tecnología. La información se publica por Mes de Operación, por cada Liquidación disponible El día de publicación de los reportes, será de acuerdo con las fechas en que está disponible la información mensual completa de cada proceso de liquidación.*.

La información se encuentra disponible al público aproximadamente 15 días después de terminado el mes correspondiente.

## Método y formato de invocación del SW-EGTT
El Servicio Web está basado en el estilo arquitectónico "REST" (en inglés, REpresentation State Transfer). En la invocación del SW-EGTT se utiliza el método GET para obtener información de un recurso.
El formato de invocación del SW-EGTT es:
**https://api.energia-mexico.org/SWEGTT/parámetros**

* Parámetros para la invocación del SW-EGTT
    * **SISTEMA** - Sistema Eléctrico Nacional [SEN].
    * **PROCESO** - Proceso [MTR].
    * **AÑO INICIAL** - Año inicial del periodo. Formato AAAA.
    * **MES INICIAL** - Mes inicial del periodo. Formato MM.
    * **DÍA INICIAL** - Día inicial del periodo. Formato DD.
    * **AÑO FINAL** - Año final del periodo. Formato AAAA.
    * **MES FINAL** - Mes final del periodo. Formato MM.
    * **DÍA FINAL** - Día final del periodo. Formato DD.
    * **FORMATO** - Formato de Salida [JSON].


* Todos los parámetros son obligatorios.
* Cada uno de los parámetros deberá separarse por el caracter reservado (/).
* Los días para los cuales se realiza la solicitud, corresponden a Días de Operación del MEM.
* La información se encuentra disponible a partir del 1 de abril del 2016.
* La información se actualiza una vez al mes.
* El periodo de consulta podrá considerar de 1 a 200 Días de Operación.
* La información oficial sobre la Energía Generada por Tipo de Tecnología se publica mensualmente en el Área Pública del SIM, en la siguiente liga:
https://www.cenace.gob.mx/Paginas/SIM/Reportes/EnergiaGeneradaTipoTec.aspx

## Información que devuelve la invocación del SW-EGTT

* **status** - Estado de la respuesta [OK, ZERO_RESULTS].
* **nombre** - Nombre del reporte [Energía Generada por Tipo de Tecnología].
* **proceso** - Proceso [MTR].
* **sistema** - Sistema Eléctrico Nacional [SEN].
* **area** - Origen de la API [Open Source Project https://github.com/AngelCarballoCremades/energia-mexico-REST-API].
* **tecnologia** - Tipo de tecnología de generación.
* **fecha** - Día de Operación.
* **hora** - Hora de Operación.
* **energia** - Energía generada en MWh.

## Ejemplo de invocación del SW-EGTT
Para obtener información de la Energía Generada por Tipo de Tecnología correspondiente al Día de Operación 20 de enero de 2020, en formato de salida JSON.

La invocación del SW-EGTT sería de la siguiente manera:

https://api.energia-mexico.org/SWEGTT/SEN/MTR/2020/01/20/2020/01/20/JSON