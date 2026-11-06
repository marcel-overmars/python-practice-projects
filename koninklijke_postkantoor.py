# ==========================================================
# UITLEG PROJECT - HET KONINKLIJKE POSTKANTOOR
# ==========================================================
#
# In dit project worden binnengekomen poststukken
# gecontroleerd op voldoende porto. Alleen goedgekeurde
# poststukken worden toegevoegd aan de verzendlijst.
# Twee functies werken samen om de post te verwerken
# en vervolgens een verzendoverzicht te tonen.
#
# Gebruikte technieken:
# - def: twee functies maken met verschillende taken.
# - Parameters: lijsten doorgeven aan functies.
# - for: een lijst met dictionaries doorlopen.
# - if/else: controleren of er voldoende porto is betaald.
# - >=: controleren of de porto minimaal 4 bedraagt.
# - append(): goedgekeurde poststukken toevoegen aan een lijst.
# - Dictionary keys: ontvanger en porto afzonderlijk uitlezen.
# - f-strings: gegevens overzichtelijk weergeven.
# - len(): het aantal verzonden poststukken tellen.
#
# Het belangrijkste oefendoel was het combineren van
# lijsten, dictionaries en voorwaarden binnen twee
# samenwerkende functies. De eerste functie verwerkt
# de poststukken en de tweede toont de resultaten.
# De aangepaste lijst blijft behouden zonder return.
# ==========================================================

# Maakt een lijst met dictionaries voor de poststukken en een
# lijst waar de goedgekeurde poststukken in komen.

poststukken = [
    {'ontvanger': 'Kasteel Drakenburg', 'porto': 5},
    {'ontvanger': 'Kasteel Stormwind', 'porto': 2},
    {'ontvanger': 'Kasteel Ravenstein', 'porto': 8},
    {'ontvanger': 'Kasteel Ijzerberg', 'porto': 3},
    {'ontvanger': 'Kasteel Zilvermaan', 'porto': 6}
]

verzonden_post = []

# Controleert alle binnen gekomen poststukken
# en voegt ze aan de lege lijst toe

def controle_poststukken(controles, verzonden):
    print("======== KONINKLIJKE POSTKANTOOR ========")
    print()

    for controle in controles:
        if controle['porto'] >= 4:
            verzonden.append(controle)
            print(f"{controle['ontvanger']}: verzending goedgekeurd!")
        else:
            print(f"{controle['ontvanger']}: onvoldoende porto!")
    print()

# Toont de lijst met verzonden poststukken.

def versturen(verzonden):
    print(f"======== VERZENDOVERZICHT ========")
    print()
    for zending in verzonden:
        print(f"{zending['ontvanger']} - Porto: {zending['porto']} goudstukken")
    print()

    print(f"Totaal verzonden poststukken: {len(verzonden)}")

controle_poststukken(poststukken, verzonden_post)
versturen(verzonden_post)