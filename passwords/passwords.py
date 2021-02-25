# Importando o banco de dados;
import sqlite3

import os # Biblioteca usada (neste caso) apenas para limpar a tela;

# Criando a senha para o projeto;
MASTER_PASSWORD = "123456"

# Verificando a senha ao entrarmos no programa;
senha = input("Insira sua senha mestre: ")
if (senha != MASTER_PASSWORD):
    print("Senha Inválida! Encerrando...")
    exit()
else:
    os.system("cls")

# Conectando ao banco de dados;
conn = sqlite3.connect("passwords.db")

cursor = conn.cursor()

# Criar tabela se uma não existir;
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

# Definindo a função que escreverá nosso menu;
def menu():
    print("=============================")
    print("| i: inserir nova senha     |")
    print("| l: listar serviços salvos |")
    print("| r: recuperar uma senha    |")
    print("| s: sair                   |")
    print("|===========================|")

# Função que recebe o nome do serviço, o nome de usuário e a senha; 
def insert_password(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}','{password}')
    ''')
    conn.commit()

# Função que nos mostra os serviços armazenados;
def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)

# Função que nos devolve a senha do serviço (se existente);
def get_password(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')

    if (cursor.rowcount == 0):
        print("Serviço não cadastrado (use \"l\" para verificar os serviços)")
    else:
        for user in cursor.fetchall():
            print(user)


# Laço de repetição; 
while True:
    # print(cursor.rowcount)
    menu()
    op = input("\nO que deseja fazer? ")   
    os.system("cls")


    if op not in ["i", "l", "r", "s"]:
        print("Opção Inválida!")
        continue
    
    if (op == "i"):
        print("--- Cadastramento ---")
        service = input("Digite o nome do serviço: ")
        username = input("Digite o nome de usuário: ")
        password = input("Digite a senha: ")
        insert_password(service, username, password)
        os.system("cls")
        print("Cadastrado com sucesso!")

    if (op == "l"):
        print("Serviços Salvos:")
        show_services()

    if (op == "r"):
        service = input("Serviço para o qual quer a senha: ")
        os.system("cls")
        print("Senhas: (usuário - senha)")
        get_password(service)

    if (op == "s"):
        print("Saindo...")
        break

# Fecha a conexão com o banco de dados.
conn.close()