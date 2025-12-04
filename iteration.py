'''
Obiettivo: Iterare su dizionari.
'''

# Creare un dizionario utenti con le seguenti coppie:
utenti: dict[str, str] = {
    "Alice" : "admin",
    "Bob" : "user",
    "Charlie" : "guest"
}

# Iterare sul dizionario e stampare ogni coppia nel formato: "Username: alice, Ruolo: admin"
for username, ruolo in utenti.items():
    print(f"Username: {username} - Ruolo: {ruolo}")

# Verificare se "Bob" è una chiave presente
is_bob_presente = "Bob" in utenti
print(f"Bob è presente: {is_bob_presente}")

# Stampare tutte le chiavi (usernames)
print(f"Usernames: {utenti.keys()}")

# Stampare tutti i valori (ruoli)
print(f"Ruoli: {utenti.values()}")