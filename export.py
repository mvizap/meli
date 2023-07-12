import pandas as pd
from sqlalchemy import create_engine

user = "root"
password = ""
database = "meli2"
server = "localhost"

def create_table(file, table_name, start=0):
    # Leer el archivo XLSX con Pandas
    data = pd.read_excel(f'{file}', header=start)

    # Identificar las columnas que terminan con _at y convertirlas a tipo fecha
    date_columns = [col for col in data.columns if col.endswith('_at')]
    data[date_columns] = data[date_columns].apply(pd.to_datetime)

    # Crear una conexión a la base de datos
    engine = create_engine(f'mariadb://{user}:{password}@{server}/{database}')

    # Especificar el nombre de la tabla y guardar los datos en la base de datos
    data.to_sql(table_name, engine, index=False, if_exists='replace')
              
print('Exportando background_jobs')
create_table('../data/background_jobs.xlsx','background_jobs')
print('Exportando events_types')
create_table('../data/events_types.xlsx','events_types',1)
print('Exportando historical_events')
create_table('../data/historical_events.xlsx','historical_events')
print('Exportando http_requests')
create_table('../data/http_requests.xlsx','http_requests')
print('Exportando sites')
create_table('../data/sites.xlsx','sites',1)
print('Exportando users')
create_table('../data/users.xlsx','users',1)
print('Exportando workbooks')
create_table('../data/workbooks.xlsx','workbooks',1)