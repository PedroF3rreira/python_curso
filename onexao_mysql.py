import mysql.connector
from mysql.connector import errorcode

db_credentials = {
    "user": "root",
    "password": "",
    "host": "localhost",
    "database": "laravel"
}

try:
    conn = mysql.connector.connect(**db_credentials)
    query = ("insert into users (name, email) values ('jonny', 'jonnygmail.com')")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
except mysql.connector.Error as erro:
    if erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("verifique sua senha")
    elif erro.errno == errorcode.ER_BAD_DB_ERROR:
        print("banco de dados não existe")
    else:
        print(erro)
else:
    print("conexão feita")
finally:
    conn.close()
