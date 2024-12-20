import xml.dom.minidom as minidom
import requests

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

capital_nz = get_capital_country("NZ")
print(f"A capital da Nova Zelândia é: {capital_nz}")

def get_country_population(country_code):
    response = requests.get(f"https://api.example.com/CountryPopulation?countryCode={country_code}")
    if response.status_code == 200:
        return parse_xml(response.text, "Population")
    return "Erro na API"

def get_country_currency(country_code):
    response = requests.get(f"https://api.example.com/CountryCurrency?countryCode={country_code}")
    if response.status_code == 200:
        return parse_xml(response.text, "Currency")
    return "Erro na API"

def get_country_language(country_code):
    response = requests.get(f"https://api.example.com/CountryLanguage?countryCode={country_code}")
    if response.status_code == 200:
        return parse_xml(response.text, "Language")
    return "Erro na API"

population_nz = get_country_population("NZ")
currency_nz = get_country_currency("NZ")
language_nz = get_country_language("NZ")

print(f"A população da Nova Zelândia é: {population_nz}")
print(f"A moeda da Nova Zelândia é: {currency_nz}")
print(f"O idioma principal da Nova Zelândia é: {language_nz}")
