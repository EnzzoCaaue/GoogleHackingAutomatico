#########################################
#       Criado por Ryan Aragão          #
#       Revisado por Enzo C.            #
#            14/02/2019                 #
#  Script para Realizar Google Hacking  #
#               V3.0                    #
#########################################
from googlesearch import search

dominio = str(input("coloque o dominio: "))

# Ataque
email = f'intitle:parceria | intitle:contato | intext:@gmail.com | intext:@contato | intext:@hotmail site:{dominio}'
acesslog = f'inurl:access.log {dominio}'
indexof = f'inurl:“index of” {dominio}'
robotstxt = f'inurl:robots.txt {dominio}'
senha = f'filetype:xls senha | filetype:txt intext:senha site:{dominio}'
tudo = f'intitle:parceria | intitle:contato | intext:@gmail.com | intext:@contato | intext:@hotmail site:{dominio} | inurl:access.log {dominio} | inurl:“index of” {dominio} | inurl:robots.txt {dominio} | filetype:xls senha | filetype:txt intext:senha site:{dominio}'

def options():
    banner = '''
    +-------------------------+-------------------------+
    |             Seja bem vindo a GHPP                 |
    |   Realize o Google Hacking de Forma Automática!   |
    | Criada para economizar tempo e energia no PenTest |
    |           https://github.com/RyanAragao2          |
    +-------------------------+-------------------------+
            '''
    print(banner)
    print("0 - Sair")
    print("1 - Procurar Emails")
    print("2 - Tentar encontrar Log de Acesso")
    print("3 - Tentar encontrar Index OF")
    print("4 - Tentar encontrar ROBOTS")
    print("5 - Tentar roubar senha")
    print("6 - Tentar tudo")

options()
while True:
    menu = int(input("Selecione uma opção: "))
    if menu == 0:
        print("Até a proxima")
        break
    elif menu == 1:
        with open("resultadoemails.txt", "w") as stream:
            for url in search(email, stop=20):
                print(url, file=stream)
                print("Os URLS foram salvos em resultadoemails.txt")
                print("Caso queira, selecione outra opção")
    elif menu == 2:
        with open("resultadoacesslog.txt", "w") as stream:
            for url in search(acesslog, stop=20):
                print(url, file=stream)
                print("Os URLS foram salvos em resultadoacesslog.txt")
                print("Caso queira, selecione outra opção")
    elif menu == 3:
        with open("resultadoindexof.txt", "w") as stream:
            for url in search(indexof, stop=20):
                print(url, file=stream)
                print("Os URLS foram salvos em resultadoindexof.txt")
                print("Caso queira, selecione outra opção")
    elif menu == 4:
        with open("resultadorobots.txt", "w") as stream:
            for url in search(robotstxt, stop=20):
                print(url, file=stream)
                print("Os URLS foram salvos em resultadorobots.txt")
                print("Caso queira, selecione outra opção")
    elif menu == 5:
        with open("resultadosenhas.txt", "w") as stream:
            for url in search(senha, stop=20):
                print(url, file=stream)
                print("Os URLS foram salvos em resultadosenhas.txt")
                print("Caso queria, selecione outra opção")
     elif menu == 6:
        with open("resultadotudo.txt", "w") as stream:
            for url in search(tudo, stop=20):
                print(url, file=stream)
                print("Os URLS foram salvos em resultadotudo.txt")
                print("Caso queria, selecione outra opção")
    else:
        print("Essa opção não existe, tente novamente!")
