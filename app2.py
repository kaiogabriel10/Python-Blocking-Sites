import subprocess
import mysql.connector

# Conectar ao MySQL
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin04',
    database='LOGIN'
)
cursor = connection.cursor()

def block_site():
    print("Please enter your Login and Password")
    login = input("Login: ")
    password = input("Password: ")

    # Consultar o banco de dados para verificar as credenciais do usuário
    comando = 'SELECT * FROM DADOS WHERE LOGIN = %s AND PASSWORD = %s'
    cursor.execute(comando, (login, password))
    result = cursor.fetchone()

    # Verificar se o login e a senha são válidos
    if result:
        nome_do_site = input("Digite o nome do site: ")
        ip_site = input("Digite o IP do site: ")

        # Comando PowerShell para bloquear o site
        comando_powershell = f'New-NetFirewallRule -DisplayName "Bloquear endereço IP do {nome_do_site}.com" -Direction Outbound -LocalPort Any -Protocol TCP -Action Block -RemoteAddress {ip_site}'
        
        # Executar o comando PowerShell usando subprocess
        subprocess.call(comando_powershell, shell=True)
    else:
        print("Login or Password incorrect!")

    # Fechar a conexão com o banco de dados
    cursor.close()
    connection.close()

block_site()
