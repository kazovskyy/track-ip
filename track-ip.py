# Tool by: kazovsky

import requests
import time
from termcolor import colored
import os

os.system("clear")
time.sleep(0.50)

ascii_art = """
                          ++################                                    
                        ########################                                
                    ##############################--                            
                  ##################################MM                          
                ######################################                          
                ########################################                        
              ################            ################                      
              ###############                ##############                      
             ##############                  @@############                      
             #############                    ##############                    
            #############                      #############                   
            #############                       ############                    
            #############                      #############                    
            #############                      #############                    
            ##############                    ##############                    
            ################                ################                    
              ################             ################                      
               ############################################                      
               ..########################################                        
                  ######################################                        
                   ###################################                         
                   ##################################                          
                    ################################                            
                    ..############################                              
                       ##########################                              
                        ########################                                
                         ######################                                  
                          ####################                                  
                            ################                                    
                             ##############                                    
                              ############                                      
                               ##########                                        
                                ########                                        
                                  ####
                                   ##

"""
cor = colored(ascii_art, color="red")

print(cor)

txt = input(colored("digite o endereço ip: ", "yellow"))

response = requests.get(f"https://ipapi.co/{txt}/json/")

n = colored("não encontrado!", "red")

data = response.json()

if response.status_code == 200:
    os.system("clear")
    data = response.json()
    
    ip = data.get("ip", n)
    nw = data.get("network", n)
    vrs = data.get("version", n)
    pais = data.get("country_name", n)
    cdp2 = data.get("country_code_iso3", n)
    ctdp = data.get("country_capital", n)
    cdd = data.get("city", n)
    rg = data.get("region", n)
    cdr = data.get("region_code", n)
    cdc = data.get("continent_code", n)
    eu = data.get("in_eu", n)
    cep = data.get("postal", n)
    lttd = data.get("latitude", n)
    lgtd = data.get("longitude", n)
    dddpais = data.get("country_calling_code", n)
    moeda = data.get("currency", n)
    nomemoeda = data.get("currency_name", n)
    asn = data.get("asn", n)
    org = data.get("org", n)
    hora = data.get("timezone", n)
    
    
    print(colored(f"ip: {ip}", "green"))
    print(colored(f"network: {nw}", "green"))
    print(colored(f"versão: {vrs}", "green"))
    print(colored(f"país: {pais}", "green"))
    print(colored(f"capital: {ctdp}", "green"))
    print(colored(f"código do país: {cdp2}", "green"))
    print(colored(f"código do continente: {cdc}", "green"))
    print(colored(f"Estado: {rg}", "green"))
    print(colored(f"código do estado: {cdr}", "green"))
    print(colored(f"cidade: {cdd}", "green"))
    print(colored(f"horário: {hora}", "green"))
    print(colored(f"europa: {eu}", "green"))
    print(colored(f"código postal: {cep}", "green"))
    print(colored(f"latitude: {lttd}", "green"))
    print(colored(f"longitude: {lgtd}", "green"))
    print(colored(f"código do país (telefone): {dddpais}", "green"))
    print(colored(f"moeda: {moeda}", "green"))
    print(colored(f"nome da moeda: {nomemoeda}", "green"))
    print(colored(f"asn: {asn}", "green"))
    print(colored(f"org: {org}", "green"))
    
    print("")
    
    sair = colored("sair: ", "red")
    
    fim = colored("aperte enter para ", "yellow")
    
    end = fim + sair
    
    input(end)
    
    if end == end:
        quit