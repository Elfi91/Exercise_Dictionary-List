'''
Obiettivo: Ordinare liste e verificare esistenza elementi.
'''
from typing import List

# Creare una lista prezzi contenente: [45.5, 12.0, 78.3, 23.1, 56.7]
# lista_prezzi_originale = ["45.5", "12.0", "78.3", "23.2", "56.7"]

lista_prezzi_originale: list[int] = ["45.5", "12.0", "78.3", "23.2", "56.7"]

prezzi_float: list[float] = [float(prezzo) for prezzo in lista_prezzi_originale]

#Creare una copia ordinata della lista (usando sorted())
lista_prezzi_ordinata = sorted(prezzi_float)

# Contare quanti prezzi sono maggiori di 50
limite = 50
conteggio_maggiore_di_50 = sum(prezzo > limite for prezzo in prezzi_float)

# Trovare il prezzo minimo e massimo
prezzo_minimo = min(lista_prezzi_ordinata)
prezzo_massimo = max(lista_prezzi_ordinata)

# Stampa la lista ordinata
print("--- Risultati Analisi ---")
print(f"Lista Prezzi Ordinata: {lista_prezzi_ordinata}")
print(f"Prezzo Minimo: {prezzo_minimo}€\nPrezzo Massimo: {prezzo_massimo}")

#Verificare se 23.1 è nella lista
if 23.1 in lista_prezzi_ordinata:
    print("Si, 23.1 è nella lista")
else:
    print("No, 23.1 non è nella lista")

print(f"I numeri maggiori di 50 sono: {conteggio_maggiore_di_50}")