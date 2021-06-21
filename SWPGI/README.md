# Servicio Web para la descarga de Pronóstico de Generación Intermitente (SW-PGI)

## Consideraciones

1. El uso del presente Servicio Web es exclusivamente para la descarga de información del [Pronóstico de Generación Intermitente](https://www.cenace.gob.mx/Paginas/SIM/Reportes/H_PronosticosGeneracion.aspx?N=245&opc=divCssPronosticosGen&site=Pron%C3%B3sticos%20de%20Generaci%C3%B3n%20Intermitente&tipoArch=C&tipoUni=ALL&tipo=All&nombrenodop=).
2. El SW-PGI es un proyecto abierto y para uso del público en general.
3. En caso de observar alguna falla en los datos o funcionamiento del servicio o si tienes alguna sugerencia, levanta un *Issue* en Github o mándame un mensaje directo en [Linkedin](https://www.linkedin.com/in/angelcarballo/).

## Método y formato de invocación del SW-PGI
El Servicio Web está basado en el estilo arquitectónico "REST" (en inglés, REpresentation State Transfer). En la invocación del SW-PGI se utiliza el método GET para obtener información de un recurso.
El formato de invocación del SW-PGI es:
**https://api.energia-mexico.org/SWPGI/parámetros**

* Parámetros para la invocación del SW-PGI
    * **SISTEMA** - Sistema Interconectado [SIN, BCA, BCS].
    * **PROCESO** - Proceso [MDA].
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
* La información se encuentra disponible a partir del 1 de enero del 2018.
* La información se actualiza varias veces a la semana.
* El periodo de consulta podrá considerar de 1 a 200 Días de Operación.
* La información oficial sobre el Pronóstico de Generación Intermitente se publica diariamente en el Área Pública del SIM, en la siguiente liga:
https://www.cenace.gob.mx/Paginas/SIM/Reportes/H_PronosticosGeneracion.aspx?N=245&opc=divCssPronosticosGen&site=Pron%C3%B3sticos%20de%20Generaci%C3%B3n%20Intermitente&tipoArch=C&tipoUni=ALL&tipo=All&nombrenodop=

## Información que devuelve la invocación del SW-PGI

* **status** - Estado de la respuesta [OK, ZERO_RESULTS].
* **nombre** - Nombre del reporte [Pronóstico de Generación Intermitente].
* **proceso** - Proceso [MDA].
* **sistema** - Sistema Eléctrico Nacional [SIN, BCA o BCS].
* **area** - Origen de la API [Open Source Project https://github.com/AngelCarballoCremades/energia-mexico-REST-API].
* **tecnologia** - Tipo de tecnología de generación [eolica, fotovoltaica].
* **fecha** - Día de Operación.
* **hora** - Hora de Operación.
* **energia** - Pronóstico de energía generada en MWh.

## Ejemplo de invocación del SW-PGI
Para obtener información del Pronóstico de Generación Intermitente correspondiente al Día de Operación 20 de enero de 2020 en el Sistema Interconectado Nacional (SIN), en formato de salida JSON.

La invocación del SW-PGI sería de la siguiente manera:

https://api.energia-mexico.org/SWPGI/SIN/MDA/2020/01/20/2020/01/20/JSON