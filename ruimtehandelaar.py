# ==========================================================
# UITLEG PROJECT - DE RUIMTEHANDELAAR
# ==========================================================
#
# In dit project worden binnengekomen goederen gecontroleerd.
# Alleen toegestane goederen worden toegevoegd aan de opslag.
# Twee functies werken samen om de goederen te verwerken
# en vervolgens een overzicht te tonen.
#
# Gebruikte technieken:
# - def: twee functies maken met verschillende taken.
# - Parameters: lijsten doorgeven aan functies.
# - for: alle binnengekomen goederen controleren.
# - if/else: bepalen of een levering wordt geaccepteerd.
# - in: controleren of een goed op de toegestane lijst staat.
# - append(): geaccepteerde goederen toevoegen aan de opslag.
# - len(): het totale aantal opgeslagen goederen tellen.
#
# Het belangrijkste oefendoel was leren hoe twee functies
# samenwerken, waarbij de eerste functie een lijst aanpast
# en de tweede functie de bijgewerkte gegevens gebruikt.
# Hiervoor is geen return nodig.
# ==========================================================

# Maak de lijsten met leveringen, toegestane goederen
# en een lege opslaglijst.

leveringen = [
    'titanium',
    'ruimtestof',
    'kristallen',
    'alien-eieren',
    'brandstof',
    'goud'
]

toegestane_goederen = [
    'titanium',
    'kristallen',
    'brandstof',
    'goud'
]

opslag = []

# Controleert alle binnengekomen leveringen.

def controle_goederen(leveringen, toegestaan, opslag):
    print("======== RUIMTESTATION NOVA ========")
    print()

    for levering in leveringen:
        if levering in toegestaan:
            opslag.append(levering)
            print(f"{levering} is geaccepteerd!")
        else:
            print(f"{levering} is geweigerd!")
    print()

# Toont de huidige goederen in de opslag.

def opgeslagen(opslag):
    print("======== OVERZICHT OPSLAG ========")
    print()

    for goederen in opslag:
        print(goederen)
    print()

    print(f"Totaal geaccepteerde goederen: {len(opslag)}")

controle_goederen(leveringen, toegestane_goederen, opslag)
opgeslagen(opslag)