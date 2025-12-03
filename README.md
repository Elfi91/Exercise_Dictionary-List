# ESERCIZI LISTA #

## Esercizio 1.1: Manipolazione Base
Obiettivo: Familiarizzare con i metodi base delle liste.

Consegna:
- Creare una lista server contenente: ["web01", "db01", "cache01"]
- Aggiungere "backup01" alla fine
- Inserire "proxy01" all'inizio (indice 0)
- Rimuovere "cache01"
- Stampare la lista finale e la sua lunghezza

Output Atteso:

['proxy01', 'web01', 'db01', 'backup01']
Numero server: 4

## Esercizio 1.2: Slicing e Accesso
Obiettivo: Praticare l'accesso agli elementi e lo slicing.

Consegna:
- Creare una lista temperature contenente: [15, 18, 22, 25, 28, 30, 27, 24, 20]
- Stampare la prima temperatura
- Stampare l'ultima temperatura
- Stampare le temperature dalla posizione 2 alla 5 (esclusa)
- Stampare tutte le temperature con step 2 (saltando una ogni due)

Output Atteso:

Prima temperatura: 15
Ultima temperatura: 20
Temperature [2:5]: [22, 25, 28]
Ogni due: [15, 22, 28, 27, 20]

## Esercizio 1.3: Ordinamento e Ricerca
Obiettivo: Ordinare liste e verificare esistenza elementi.

Consegna:
- Creare una lista prezzi contenente: [45.5, 12.0, 78.3, 23.1, 56.7]
- Creare una copia ordinata della lista (usando sorted())
- Trovare il prezzo minimo e massimo
- Verificare se 23.1 è nella lista
- Contare quanti prezzi sono maggiori di 50

Output Atteso:

Prezzi originali: [45.5, 12.0, 78.3, 23.1, 56.7]
Prezzi ordinati: [12.0, 23.1, 45.5, 56.7, 78.3]
Minimo: 12.0
Massimo: 78.3
23.1 presente: True
Prezzi > 50: 2

# ESERCIZI DIZIONARI #

## Esercizio 2.1: Creazione e Accesso
Obiettivo: Creare dizionari e accedere ai valori.

Consegna:
- Creare un dizionario config con le seguenti coppie:
    "host": "192.168.1.1"
    "port": 8080
    "ssl": True
    "timeout": 30
- Stampare il valore di "host"
- Modificare "port" in 443
- Aggiungere una nuova chiave "protocol" con valore "https"
- Stampare il dizionario completo

Output Atteso:

Host: 192.168.1.1
{'host': '192.168.1.1', 'port': 443, 'ssl': True, 'timeout': 30, 'protocol': 'https'}

## Esercizio 2.2: Iterazione
Obiettivo: Iterare su dizionari.

Consegna:
- Creare un dizionario utenti con le seguenti coppie:
    "alice": "admin"
    "bob": "user"
    "charlie": "guest"
- Iterare sul dizionario e stampare ogni coppia nel formato: "Username: alice, Ruolo: admin"
- Verificare se "bob" è una chiave presente
- Stampare tutte le chiavi (usernames)
- Stampare tutti i valori (ruoli)

Output Atteso:

Username: alice, Ruolo: admin
Username: bob, Ruolo: user
Username: charlie, Ruolo: guest
bob presente: True
Usernames: dict_keys(['alice', 'bob', 'charlie'])
Ruoli: dict_values(['admin', 'user', 'guest'])

