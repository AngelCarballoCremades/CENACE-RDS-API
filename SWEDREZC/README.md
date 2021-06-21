# Servicio Web para la descarga de Estimación de Demanda Real de Energía por Zona de Carga (SW-EDREZC)

## Consideraciones

1. El uso del presente Servicio Web es exclusivamente para la descarga de información de la [Estimación de Demanda Real de Energía por Retiros](https://www.cenace.gob.mx/Paginas/SIM/Reportes/EstimacionDemandaReal.aspx).
2. Se consideran únicamente Liquidaciones 0 (Cuando no hay Liquidaciones 0 puede que se muestre información de Re-Liquidaciones 1)
3. El SW-EDREZC es un proyecto abierto y para uso del público en general.
4. En caso de observar alguna falla en los datos o funcionamiento del servicio o si tienes alguna sugerencia, levanta un *Issue* en Github o mándame un mensaje directo en [Linkedin](https://www.linkedin.com/in/angelcarballo/).

## Descripción del SW-EDREZC
Según el CENACE: *La estimación de la Demanda Real del Sistema por Retiros se obtiene agregando todas las compras de energía que se realizan por las Entidades Responsables de Carga, incluyendo las exportaciones. Se excluyen las pérdidas técnicas y no técnicas de la red que corresponde al Mercado Eléctrico Mayorista*.

La información se encuentra disponible al público aproximadamente 15 días después del Día de Operación correspondiente.

## Método y formato de invocación del SW-EDREZC
El Servicio Web está basado en el estilo arquitectónico "REST" (en inglés, REpresentation State Transfer). En la invocación del SW-EDREZC se utiliza el método GET para obtener información de un recurso.
El formato de invocación del SW-EDREZC es:
**https://api.energia-mexico.org/SWEDREZC/parámetros**

* Parámetros para la invocación del SW-EDREZC
    * **SISTEMA** - Sistema Interconectado [SIN, BCA, BCS].
    * **PROCESO** - Proceso [MTR].
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
* La información se encuentra disponible a partir del 1 de enero del 2018.
* La información se actualiza varias veces a la semana.
* El periodo de consulta podrá considerar de 1 a 200 Días de Operación.
* La información oficial sobre la Estimación de Demanda Real de Energía por Retiros se publica diariamente en el Área Pública del SIM, en la siguiente liga:
https://www.cenace.gob.mx/Paginas/SIM/Reportes/EstimacionDemandaReal.aspx

## Información que devuelve la invocación del SW-EDREZC

* **status** - Estado de la respuesta [OK, ZERO_RESULTS].
* **nombre** - Nombre del reporte [Estimación de la Demanda Real de Energía por Zona de Carga].
* **proceso** - Proceso [MTR].
* **sistema** - Sistema Interconectado [SIN, BCA o BCS].
* **area** - Origen de la API [Open Source Project https://github.com/AngelCarballoCremades/energia-mexico-REST-API].
* **zona_carga** - Zona de Carga.
* **fecha** - Día de Operación.
* **hora** - Hora de Operación.
* **energia** - Estimación de Demanda Real de Energía en MWh.

## Ejemplo de invocación del SW-EDREZC
Para obtener información de la Estimación de Demanda Real de Energía para las Zonas de Carga "OAXACA y CENTRO ORIENTE" del Sistema Interconectado Nacional, correspondiente al Día de Operación 20 de enero de 2020, en formato de salida JSON.

La invocación del SW-EDREZC sería de la siguiente manera:

https://api.energia-mexico.org/SWEDREZC/SIN/MTR/OAXACA,CENTRO-ORIENTE/2020/01/20/2020/01/20/JSON