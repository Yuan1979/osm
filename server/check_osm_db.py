from psycopg2 import connect, OperationalError


try:
    connection = connect(dbname='postgres', user='postgres', host='db', password='admin')
    print('Connected to OsmGIS')
except OperationalError as e:
    print(str(e))