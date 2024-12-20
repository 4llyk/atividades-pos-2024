import requests
from prettytable import PrettyTable

def get_boletim_suap(api_key):
    base_url = "https://suap.ifrn.edu.br/api/v2/"
    boletim_endpoint = "minhas-informacoes/boletim/"

    # Cabeçalhos para autenticação com o token de API
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    # Fazer a requisição ao endpoint do boletim
    response = requests.get(base_url + boletim_endpoint, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao acessar o SUAP: {response.status_code} - {response.text}")

# Função para formatar e imprimir o boletim
def formatar_boletim(boletim):
    tabela = PrettyTable()
    tabela.field_names = ["Disciplina", "1ª Unidade", "2ª Unidade", "3ª Unidade", "Média Final"]

    for disciplina, detalhes in boletim.items():
        tabela.add_row([
            disciplina,
            detalhes.get("nota_etapa_1", "-"),
            detalhes.get("nota_etapa_2", "-"),
            detalhes.get("nota_etapa_3", "-"),
            detalhes.get("media_final", "-")
        ])

    print(tabela)

def main():
    api_key = "Chave"

    try:
        boletim = get_boletim_suap(api_key)
        formatar_boletim(boletim)
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
