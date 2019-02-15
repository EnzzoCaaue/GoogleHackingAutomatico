#########################################
#       Criado por Ryan Aragão          #
#            14/02/2019                 #
#   Script para auxiliar no PenTest     #
#               V1.0                    #
#########################################
from googlesearch import search

# Apresentação
print("Seja bem-vindo ao Google Hacking Automatico!")
print("O Script buscara por URLS onde tiver o que foi pedido")
print("Após encontrar ele vai guardar os resultados em um TXT")
print("Feito para economizar tempo e energia!")
print("Criado por Ryan Aragão")
input("Pressione ENTER para continuar")

dominio = str(input("coloque o dominio:"))

# Ataque
email = f'intitle:parceria | intitle:contato | intext:@gmail.com | intext:@contato | intext:@hotmail site:{dominio}'
acesslog = f'inurl:access.log {dominio}'
indexof = f'inurl:“index of” {dominio}'
robotstxt = f'inurl:robots.txt {dominio}'


def menu():
    print("0 - Sair")
    print("1 - Procurar Emails")
    print("2 - Tentar encontrar Log de Acesso")
    print("3 - Tentar encontrar Index OF")
    print("4 - Tentar encontrar ROBOTS")


while True:
    menu()
    menuzinho = int(input("Selecione uma opção: "))
    if menuzinho == 0:
        print("Até a proxima")
        break
    elif menuzinho == 1:
        with open("resultadoemails.txt", "w") as stream:
            for url in search(email, stop=20):
                print(url, file=stream)
                print("Os URLS foram salvos em resultadoemails.txt")
                print("Caso queira, selecione outra opção")
    elif menuzinho == 2:
        with open("resultadoacesslog.txt", "w") as stream:
            for url in search(acesslog, stop=20):
                print(url, file=stream)
                print("Os URLS foram salvos em resultadoacesslog.txt")
                print("Caso queira, selecione outra opção")
    elif menuzinho == 3:
        with open("resultadoindexof.txt", "w") as stream:
            for url in search(indexof, stop=20):
                print(url, file=stream)
                print("Os URLS foram salvos em resultadoindexof.txt")
                print("Caso queira, selecione outra opção")
    elif menuzinho == 4:
        with open("resultadorobots.txt", "w") as stream:
            for url in search(robotstxt, stop=20):
                print(url, file=stream)
                print("Os URLS foram salvos em resultadorobots.txt")
                print("Caso queira, selecione outra opção")
    else:
        print("Essa opção não existe, tente novamente!")
