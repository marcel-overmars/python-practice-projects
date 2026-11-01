# ==========================================================
# UITLEG PROJECT - DRAKENACADEMIE
# ==========================================================
#
# In dit project wordt gecontroleerd welke draken
# geschikt zijn om aan een missie deel te nemen.
#
# De gegevens van iedere draak worden opgeslagen
# in een dictionary en samengevoegd in een lijst.
#
# De volledige lijst wordt doorgegeven aan een functie.
# Binnen de functie controleert een for-loop het
# trainingsniveau van iedere draak.
#
# Met een if/else-statement wordt bepaald of een
# draak geschikt is voor de missie (niveau 5 of hoger).
# Een teller houdt het aantal geschikte draken bij.
#
# Gebruikte technieken:
# - def en parameters
# - Een lijst doorgeven aan een functie
# - Nesting: dictionaries in een lijst
# - for-loop en if/else
# - Dictionarywaarden opvragen
# - Een teller bijhouden met +=
# - f-strings
#
# Het belangrijkste oefendoel was het combineren
# van een functie met een lijst van dictionaries,
# voorwaardelijke controles en een teller.
# ==========================================================

# Maak voor iedere draak een dictionary aan
# En sla alle dictionaries op in een lijst.

draak_1 = {
    'naam': 'Ignis',
    'niveau': 7
}

draak_2 = {
    'naam': 'Frost',
    'niveau': 3
}

draak_3 = {
    'naam': 'Shadow',
    'niveau': 5
}

draak_4 = {
    'naam': 'Ember',
    'niveau': 2
}

draak_5 = {
    'naam': 'Storm',
    'niveau': 8
}

draken = [
    draak_1,
    draak_2,
    draak_3,
    draak_4,
    draak_5
]

# Controleer het trainingsniveau van iedere draak
# en toon of deze klaar is voor de missie.

print("===== DRAKENACADEMIE =====")
print()

def controleer_draken(draken_niveau):
    aantal_geschikt = 0
    for draak in draken_niveau:
        if draak['niveau'] >= 5:
            print(f"{draak['naam']} (niveau {draak['niveau']}): klaar voor de missie.")
            aantal_geschikt += 1
        else:
            print(f"{draak['naam']} (niveau {draak['niveau']}): moet verder trainen.")
    print(f"\nAantal draken geschikt voor de missie: {aantal_geschikt}")

controleer_draken(draken)

print(f"\nAlle draken zijn gecontroleerd!")