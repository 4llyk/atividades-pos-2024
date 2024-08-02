from xml.dom.minidom import parse

dom = parse("cardapio.xml")


# Elemento raiz do XML (cardapio)
cardapio = dom.documentElement

# Recebe uma lista dos elementos com tag "prato"
pratos = cardapio.getElementsByTagName('prato')

# Acessa as informações de cada prato
for prato in pratos:
    categoria = prato.getAttribute('categoria')
    elemento_titulo = prato.getElementsByTagName('título')[0]
    titulo = elemento_titulo.firstChild.nodeValue
    elemento_autor = prato.getElementsByTagName('autor')[0]
    origem = elemento_autor.getAttribute('origem')
    autor = elemento_autor.firstChild.nodeValue
    elemento_ano = prato.getElementsByTagName('ano')[0]
    ano = elemento_ano.firstChild.nodeValue

    print("Categoria:", categoria)
    print("Título:", titulo)
    print(f'Autor: {autor} ({origem})')
    print("Ano:", ano)
    print("---\n")

def mostrar_menu():
    print('-' *50)
    print("Escolha uma refeição:")
    print("1. Café da manhã")
    print("2. Almoço")
    print("3. Jantar")
    print("4. Sair")
    print('-' *50)

def selecionar_refeicao():
    while True:

        mostrar_menu()
        escolha = input("Digite o número da sua escolha: ")
        
        if escolha == "1":
            print("Você escolheu Café da manhã.")
        elif escolha == "2":
            print("Você escolheu Almoço.")
        elif escolha == "3":
            print("Você escolheu Jantar.")
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Escolha inválida, por favor, tente novamente.")

selecionar_refeicao()
