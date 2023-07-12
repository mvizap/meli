# Proyecto "Analisis Meli"

Este proyecto consta de dos componentes principales: `export.py` y el dashboard del "Análisis Meli" para mostrar métricas de un Tableau Server de Mercado Libre.

En un principio me dieron varios excel, pero para facilitar la union, considere que mas facil era dejarlo en una base de datos.

## export.py

El archivo `export.py` es una utilidad que exporta datos de un archivo CSV a una base de datos MariaDB. Utiliza las siguientes bibliotecas:

- SQLAlchemy: Una biblioteca de mapeo relacional de objetos (ORM) para interactuar con la base de datos.
- Pandas: Una biblioteca de análisis de datos para manipular y transformar los datos del CSV.
- Driver de MariaDB: El controlador necesario para conectar y comunicarse con la base de datos MariaDB.

## Dashboard del "Análisis Meli"

El dashboard del "Desafío Meli" muestra métricas extraídas de un día de Tableau Server de Mercado Libre. Utiliza las siguientes tablas del Tableau Data Dictionary (especificación en [enlace](https://tableau.github.io/tableau-data-dictionary/2021.3/data_dictionary.htm#public.http_requests_anchor)):

- background_jobs: Contiene las tareas de actualización de extractos y suscripciones que se ejecutan en procesos de Backgrounder.
- events_types: Contiene los tipos de eventos.
- historical_events: muestra eventos que ocurren en Tableau Server. Incluye registros de usuarios que inician sesión, acceden a vistas, publican contenido, etc.
- http_requests: solicitudes realizadas a través del componente del servidor web de Tableau Server. Útil para comprender la interacción del usuario con las visualizaciones, así como el monitoreo del rendimiento.
- sites: Lista de sitios.
- users: Lista de usuarios.
- workbooks: Lista de workbooks.

El dashboard proporciona información y visualizaciones basadas en los datos de estas tablas.

## Requisitos

Para ejecutar el archivo `export.py` y utilizar el dashboard del "Desafío Meli", asegúrate de tener instaladas las siguientes dependencias:

- SQLAlchemy
- Pandas
- Driver de MariaDB

Lo puedes ejecutar como:

python export.py
