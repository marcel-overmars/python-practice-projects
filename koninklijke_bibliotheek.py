# ==========================================================
# UITLEG PROJECT - KONINKLIJKE BIBLIOTHEEK
# ==========================================================
#
# In dit project wordt een lijst met beschikbare
# boeken weergegeven.
#
# De boekenlijst wordt als argument doorgegeven
# aan een functie via de parameter 'titels'.
#
# Binnen de functie doorloopt een for-loop de lijst
# en toont ieder boek afzonderlijk op het scherm.
#
# Gebruikte technieken:
# - def en parameters
# - Een lijst doorgeven aan een functie
# - for-loop
# - Lijsten en f-strings
# - Functies aanroepen
#
# Het belangrijkste oefendoel was leren hoe je
# een volledige lijst aan een functie doorgeeft
# en de elementen binnen die functie verwerkt.
# ==========================================================

# De boekenlijst

boeken = [
    'De Verloren Stad',
    'Het Geheim van de Draak',
    'De Magische Toren',
    'Het Verboden Koninkrijk'
]

# Doorloop de boekenlijst en toon ieder boek afzonderlijk.

print("======= KONINKLIJKE BIBLIOTHEEK =======")
print()

def toon_boeken(titels):
    for titel in titels:
        print(f"Het volgende boek is beschikbaar: {titel}")

toon_boeken(boeken)

print(f"\nHet boekenoverzicht is compleet")