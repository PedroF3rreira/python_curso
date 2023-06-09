import mysql.connector
from mysql.connector import errorcode

db_credentials = {
    "user": "root",
    "password": "",
    "host": "localhost",
    "database": "laravel"
}

try:
    nome = input("Digite um nome de usuário ")
    email = input("Digite seu email de usuário ")
    email_confirma = input("Digite novamente seu email ")

    conn = mysql.connector.connect(**db_credentials)
    cursor = conn.cursor()  # cria um cursorpara executar a query

    if email == email_confirma:
        query = (f"insert into users (name, email) values (%s, %s)")
        usuario = (nome, email)
        cursor.execute(query, usuario)  # executa a query
        conn.commit()  # confirma a alteração no banco de dados
    else:
        print("Email não são idênticos")
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
