# Tool by: kazovsky

import os
from time import sleep
import requests
from termcolor import colored
import json

sleep(0.5)
print("")
ex1 = colored("123.456.789.100", "green")
ex2 = colored("exemplo: ", "yellow")
print(ex2 + ex1)
run = input(colored("digite o ip: ", "yellow"))

url = f"https://ipinfo.io/{run}/json"

response = requests.get(url)

if response.status_code == 200:
    os.system("clear")
    n = colored("Não encontrado :<", "red")
    json = response.json()
    
    ip = json.get("ip", n)
    estado = json.get("region", n)
    cidade = json.get("city", n)
    pais = json.get("country", n)
    loc = json.get("loc", n)
    org = json.get("org", n)
    cep = json.get("postal", n)
    hora = json.get("timezone", n)
    host = json.get("hostname", n)
    api = json.get("readme", n)
    
    
    print(f"IP: {ip}")
    print(f"ESTADO: {estado}")
    print(f"CIDADE: {cidade}")
    print(f"PAÍS: {pais}")
    print(f"LOCALIZAÇÃO: {loc}")
    print(f"ORG: {org}")
    print(f"CEP: {cep}")
    print(f"FUSO HORÁRIO: {hora}")
    print(f"HOSTNAME: {host}")
    print(f"API: {api}")
    print("")
    input(colored("aperte enter para sair: ", "yellow"))
else:
    print("")
    print(colored("algo está errado :< ", "red"))