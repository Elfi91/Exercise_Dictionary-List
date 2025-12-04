'''
Obiettivo: Usare dizionari per contare occorrenze.
'''

# Creare una lista voti contenente: ["A", "B", "A", "C", "B", "A", "D", "B", "C", "A"]
lista_voti: list[str] = ["A", "B", "A", "C", "B", "A", "D", "B", "C", "A"]

# Creare un dizionario vuoto conteggio
conteggio: dict[str, int] = {}

# Iterare sulla lista voti e contare quante volte appare ogni voto nel dizionario
for voto in lista_voti:
    # 1. Verifica se il voto è già una chiave nel dizionario
    if voto in conteggio:
        # Se è presente, incrementa il conteggio di 1
        conteggio[voto] += 1
    else:
        # Se non è presente, aggiungi la chiave e inizializza il conteggio a 1
        conteggio[voto] = 1

# Stampare il dizionario finale
print(conteggio)