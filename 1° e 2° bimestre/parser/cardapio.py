from xml.dom.minidom import parse

dom = parse("xml_schema/cardapio.xml")


cardapio = dom.documentElement

pratos = cardapio.getElementsByTagName('prato')

for prato in pratos:
    id = prato.getAttribute('id')
    nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
    ingredientes = prato.getElementsByTagName('ingrediente')[0].firstChild.nodeValue
    preco = prato.getElementsByTagName('preco')[0].firstChild.nodeValue
    calorias = prato.getElementsByTagName('calorias')[0].firstChild.nodeValue
    tempop = prato.getElementsByTagName('tempoPreparo')[0].firstChild.nodeValue


    print("id:", id)
    print("Nome:", nome)
    print("Ingrediente:", ingredientes)
    print("Preço:", preco)
    print("Calorias:", calorias)
    print("Tempo de Preparo:", tempop)
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