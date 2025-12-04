'''
Obiettivo: Gestire una lista di dizionari (simile a un database).
'''

# Creare una lista prodotti contenente 4 dizionari, ognuno con chiavi "nome", "prezzo", "quantita":
prodotti: list[dict] = [
    {"nome": "Laptop", "prezzo": 899.99, "quantita": 5},
    {"nome": "Mouse", "prezzo": 25.50, "quantita": 50},
    {"nome": "Tastiera", "prezzo": 75.00, "quantita": 30},
    {"nome": "Monitor", "prezzo": 299.99, "quantita": 15}
]

# Iterare sulla lista e stampare solo i prodotti con prezzo superiore a 100
print("--- Prodotti con Prezzo > 100€ ---")
for prodotto in prodotti:
    if prodotto["prezzo"] > 100:
        # Se la condizione è TRUE, si stampa l'intero dizionario
        print(f"{prodotto['nome']} : {prodotto['prezzo']}")


# Calcolare il valore totale dell'inventario (prezzo × quantità per ogni prodotto)
valore_inventario_totale: float = 0.0

for prodotto in prodotti:
    valore_parziale = prodotto["prezzo"] * prodotto["quantita"]
    
    valore_inventario_totale += valore_parziale

# Stampa il risultato finale
print(f"Valore totale dell'inventario: {valore_inventario_totale:.2f}€")
