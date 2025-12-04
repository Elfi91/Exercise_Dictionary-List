'''
Obiettivo: Creare dizionari e accedere ai valori.
'''

from typing import Union

# Creare un dizionario config con le seguenti coppie:
Config: dict[str, Union[str, int]] = {
    "Host" : "192.168.1.1",
    "Port" : 8080,
    "Ssl" : True,
    "Timeout" : 30,
}


# Stampare il valore di "host"
chiave_host = "Host"
valore_host = Config[chiave_host]
print(f"{chiave_host}: {valore_host}")

# Modificare "port" in 443
Config["Port"] = 443

# Aggiungere una nuova chiave "protocol" con valore "https"
Config["Protocol"] = "https"

# Stampare il dizionario completo
print(Config)