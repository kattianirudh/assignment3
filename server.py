import pyodbc
import redis

server = 'adb6.database.windows.net'
database = 'quiz2'
username = 'axk3905'
password = 'Password@123'
driver = '{ODBC Driver 17 for SQL Server}'

# redis connection
host = 'assignment3r.redis.cache.windows.net'
port = 6380
db = 0
r_password = '0ERMlR2UfOt5M65JTOq4Xbl5ifWzGtx9qAzCaHsnLj0='


def connect_db():
        cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        return cursor


def connect_redis():
        r = redis.StrictRedis(host=host, port=port, db=db, password=r_password, ssl=True)
        return r
