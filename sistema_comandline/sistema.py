import os
import platform
import mysql.connector

dados = {
    "user": "root",
    "password": "",
    "database": "agenda",
    "host": "localhost"
}

# funçoes de ação no sistema
def limpar_tela():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def sair():
    print("Obrigado por utilizar nosso sistema!")
    os._exit(0)


def alterar():
    mensagem_menu_alterar()
    opcao = input("Informe a opção desejada: ")
    try:
        acoes_menu_alterar[opcao]()
    except:
        input("Opção inválida.\nPressione uma tecla para voltar...")
        alterar()

def cadastrar():
    mensagem_cadastrar()
    nome = input("Digite nome do contato: ")
    tel = input("digite telefone do contato: ")
    cel = input("digite celular do contato: ")

    if nome and tel and cel:
        confirmar = input(f"confirmar cadastro do contato {nome}: [s/n] ")

        if confirmar.lower() == 's':
            try:
                contato = []
                contato.append(nome)
                contato.append(tel)
                contato.append(cel)

                conn = mysql.connector.connect(**dados)
                cursor = conn.cursor()
                query = "insert into contatos (nome, telefone, celular) values (%s, %s, %s)"
                cursor.execute(query, contato)
                conn.commit()
                cursor.close()
                conn.close()
            except:
                print("um erro ocorreu")
            else:
                print("Cadastro realizado com sucesso!")
        else:
            input("cadastro cancelado\n pressione qualquer tecla para voltar ao menu principal")
    else:
        input("falta informaçoes para realizar cadastro\n pressione qulquer tecla para voltar ao menu principal")
    menu_principal()

def pesquisar_id(id=""):
    try:
        if not id:
            id = input("informe o id do contato ")
        query = f"select * from contatos where id = '{id}'"
        conn = mysql.connector.connect(**dados)
        cursor = conn.cursor()
        cursor.execute(query)
        contato = []
        for id, nome, telefone, celular in cursor:
            contato = {'id': id, 'nome': nome, 'telefone': telefone, 'celular': celular}
        cursor.close()
        conn.close()
        alterar_contato(contato)
    except:
        print("erro")
        alterar()


def pesquisar_nome(nome=""):
    try:
        if not nome:
            nome = input("digite o nome do contato ")

        conn = mysql.connector.connect(**dados)
        cursor = conn.cursor()
        query = f"select * from contatos where nome = '{nome}'"
        cursor.execute(query)

        contato = []

        for id, nome, telefone, celular in cursor:
            contato = {'id': id, 'nome': nome, 'telefone': telefone, 'celular': celular}

        cursor.close()
        conn.close()
        alterar_contato(contato)

    except Exception as err:
        print("ocorreu um erro na busca", err)
        print("pressione qualquer tecla para voltar ao menu... ")
        alterar()

def pesquisar_telefone(telefone=""):
    try:
        if not telefone:
            telefone = input("digite o telefone do contato")
        conn = mysql.connector.connect(**dados)
        cursor = conn.cursor()
        query = f"select * from contatos where telefone='{telefone}'"
        cursor.execute(query)

        contato = []

        for id, nome, telefone, celular in cursor:
            contato = {'id': id, 'nome': nome, 'telefone': telefone, 'celular': celular}

        cursor.close()
        conn.close()

        alterar_contato(contato)

    except Exception as err:
        print("ocorreu um erro na busca", err)
        print("pressione qualquer tecla para voltar ao menu... ")
        alterar()


def pesquisar_celular(celular=""):
    try:
        if not celular:
            celular = input("digite o celular do contato")

        conn = mysql.connector.connect(**dados)
        cursor = conn.cursor()
        query = f"select * from contatos where celular='{celular}'"
        cursor.execute(query)

        contato = []

        for id, nome, telefone, celular in cursor:
            contato = {'id': id, 'nome': nome, 'telefone': telefone, 'celular': celular}

        cursor.close()
        conn.close()

        alterar_contato(contato)

    except Exception as err:
        print("ocorreu um erro na busca", err)
        print("pressione qualquer tecla para voltar ao menu... ")
        alterar()

def alterar_contato(contato):
    nome = input("digite novo nome para o contato: ")
    tel = input("digite nome telefone para o contato: ")
    cel = input("diegite novo celular para o contato: ")

    confirma = input("deseja realmente alterar esse contato: [s/n] ")

    if confirma.lower() == 's':
        try:
            query = f"update contatos set nome='{nome}', telefone='{tel}', " \
                    f"celular='{cel}' where id= {contato['id']}"
            conn = mysql.connector.connect(**dados)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()
            conn.close()
            input("Contato alterado com sucesso!/\nPressione uma tecla para voltar ao menu")
        except Exception as err:
            print("error", err)
    else:
        input("operação foi cancelada\nPresione uma tecla para voltar ao menu")
        alterar()


def listar():
    try:
        query = "select * from contatos"
        conn = mysql.connector.connect(**dados)
        cursor = conn.cursor()
        cursor.execute(query)

        print("****************Contatos********************")
        for id, nome, celular, telefone in cursor:
            print(f"*       nome: {nome}")
            print(f"*       telefone: {telefone}")
            print(f"*       celular: {celular}\n")
        print("********************************************")
        cursor.close()
        conn.close()
        input("pressione uma tecla para voltar ao menu principal...")
    except Exception as err:
        print("ocorreu um erro ", err)
    menu_principal()


def exportar():
    try:
        nome_arquivo = input("Digite o nome do arquivo ")

        conn = mysql.connector.connect(**dados)
        cursor = conn.cursor()
        query = "select * from contatos order by id desc"
        cursor.execute(query)

        contatos = []
        for id, nome, celular, telefone in cursor:
            contatos.append({'id': id, 'nome': nome, 'celular': celular, 'telefone': telefone})
        cursor.close()
        conn.close()

        with open(nome_arquivo+".txt", 'w', encoding="utf-8") as file:
            for contato in contatos:
                registros = []
                registros.append(f"{contato['id']};{contato['nome']};{contato['celular']};"
                                 f"{contato['telefone']}\n")
                file.writelines(registros)

            input("Exportação realizada com sucesso!\npressione qualquer tecla para ir ao menu")
    except Exception as err:
        print(err)
    menu_principal()
def deletar(id=""):
    try:
        if not id:
            id = input("digite o id do contato: ")
        query = f"delete from contatos where id = '{id}'"
        conn = mysql.connector.connect(**dados)
        cursor = conn.cursor()
        cursor.execute(query)

        confirma = input("REALMENTE DESEJA DELETAR ESSE CONTATO? S/N")

        if confirma.lower() == 's':
            conn.commit()
        else:
            input("Operação cancelada\npressione qualquer tecla para voltar ao menu principal")
        cursor.close()
        conn.close()
    except Exception as err:
        print("um erro cocorreu ", err)
        print("pressione qualquer tecla para voltar ao menu principal")
    menu_principal()

#funçoes de apresentação
def messagem_menu_principal():
    limpar_tela()
    print("**************************************************")
    print("*        BEM-VINDO AO SISTEMA DE CADASTRO        *")
    print("*------------------------------------------------*")
    print("*        ESCOLHA UMA DAS OPÇÕES DISPONÍVEIS      *")
    print("*        1 - CADASTRAR UM CONTATO                *")
    print("*        2 - ALTERAR UM CONTATO                  *")
    print("*        3 - LISTAR CONTATOS                     *")
    print("*        4 - EXPORTAR CONTATOS                   *")
    print("*        5 - DELETAR CONTATO                     *")
    print("*        0 - SAIR DO SISTEMA                     *")
    print("**************************************************")

def mensagem_menu_alterar():
    limpar_tela()
    print("**************************************************")
    print("*            ALTERANDO UM CONTATO EXISTENTE      *")
    print("*------------------------------------------------*")
    print("*       ESCOLHA A OPÇÃO PARA LOCALIZAR O CONTATO *")
    print("*        1 - ID                                  *")
    print("*        2 - NOME                                *")
    print("*        3 - TELEFONE                            *")
    print("*        4 - CELULAR                             *")
    print("*        0 - MENU PRINCIPAL                      *")
    print("**************************************************")


def mensagem_cadastrar():
    limpar_tela()
    print("***************************************************")
    print("*         CADASTRANDO UM NOVO CONTATO             *")
    print("***************************************************")


def menu_principal():
    try:
        messagem_menu_principal()
        opcao = input("Informe a opção desejada ")
        acoes_menu_principal[opcao]()
    except:
        print("Opção inválida.")
        input("Pressiona uma tecla para ir pro menu principal..")
        menu_principal()

acoes_menu_principal = {
    '1': cadastrar,
    '2': alterar,
    '3': listar,
    '4': exportar,
    '5': deletar,
    '0': sair
}

acoes_menu_alterar = {
    '1': pesquisar_id,
    '2': pesquisar_nome,
    '3': pesquisar_telefone,
    '4': pesquisar_celular,
    '0': menu_principal
}

if __name__ == "__main__":
    menu_principal()


