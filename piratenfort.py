# ==========================================================
# UITLEG PROJECT - HET PIRATENFORT
# ==========================================================
#
# In dit project wordt gecontroleerd welke piratenschepen
# voldoende goud hebben verzameld.
#
# De gegevens van de schepen staan in dictionaries
# die samen in een lijst zijn opgeslagen.
#
# De volledige lijst wordt doorgegeven aan een functie.
# Binnen de functie controleert een for-loop hoeveel
# goud ieder schip heeft verzameld.
#
# Schepen met minder dan 500 goudstukken worden met
# append() toegevoegd aan een aparte lijst.
# Een teller houdt bij hoeveel schepen voldoende goud hebben.
#
# Een tweede for-loop toont de schepen die opnieuw
# op expeditie moeten.
#
# Gebruikte technieken:
# - def en parameters
# - Een lijst doorgeven aan een functie
# - Nesting: dictionaries in een lijst
# - for-loops en if/else
# - Dictionarywaarden opvragen
# - Een lijst vullen met append()
# - Een teller bijhouden met +=
# - f-strings
#
# Het belangrijkste oefendoel was het zelfstandig
# combineren van verschillende technieken binnen
# één functie en het verwerken van lijstgegevens.
# ==========================================================

# Overzicht van een lijst waar dictionaries in staan 
# van de schepen

schepen = [
    {'naam': 'De Zwarte Parel', 'goud': 850},
    {'naam': 'De Zeewolf', 'goud': 320},
    {'naam': 'De Stormvogel', 'goud': 670},
    {'naam': 'De Vliegende Hollander', 'goud': 210},
    {'naam': 'De Gouden Draak', 'goud': 950}
]

# Controleert of de schepen voldoende goud hebben verzameld.
# Plaatst de schepen die onvoldoende goud hebben in een aparte lijst.
# Telt het aantal schepen met voldoende goud.

def schepen_controle(goud_controle):
    nieuwe_expeditie = []
    voldoende_goud = 0

    print("===== HET PIRATENFORT =====")
    print()
    for controle in goud_controle:
        if controle['goud'] < 500:
            nieuwe_expeditie.append(controle)
            print(f"{controle['naam']} ({controle['goud']} goud): nieuwe expeditie nodig!")
        else:
            print(f"{controle['naam']} ({controle['goud']} goud): voldoende goud!")
            voldoende_goud += 1
    print()

    print("===== NIEUWE EXPEDITIES =====")
    print()

    for expeditie in nieuwe_expeditie:
        print(expeditie['naam'])
    print()

    print(f"Aantal schepen met voldoende goud: {voldoende_goud}")
    print()

schepen_controle(schepen)

print("Alle schepen zijn gecontroleerd!")