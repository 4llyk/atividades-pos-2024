import xml.dom.minidom as minidom
import requests
from zeep import Client
# use o Pip install zeep

def parse_xml(xml_data, tag_name):
    dom = minidom.parseString(xml_data)
    elements = dom.getElementsByTagName(tag_name)
    if elements and elements[0].firstChild:
        return elements[0].firstChild.nodeValue
    return None


def get_capital_country(country_code):
    response = requests.get(f"https://api.example.com/CapitalCity?countryCode={country_code}")
    if response.status_code == 200:
        return parse_xml(response.text, "CapitalCity")
    return "Erro na API"

capital_no = get_capital_country("NO")
print(f"A capital da Noruega é: {capital_no}")

def number_to_words(number):
    wsdl_url = "https://api.example.com/NumberConversion?wsdl"
    client = Client(wsdl=wsdl_url)
    try:
        response = client.service.NumberToWords(ubiNum=number)
        return response
    except Exception as e:
        return f"Erro ao converter número: {e}"

number = 223
number_in_words = number_to_words(number)
print(f"O número {number} por extenso em inglês é: {number_in_words}")
