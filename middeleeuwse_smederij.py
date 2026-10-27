# ==========================================================
# UITLEG PROJECT - MIDDELEEUWSE SMEDERIJ
# ==========================================================
#
# In dit project kunnen klanten verschillende wapens
# bestellen bij een middeleeuwse smederij.
#
# Een functie berekent de totale kosten op basis van
# het gekozen wapen en het aantal exemplaren.
# De berekende prijs wordt teruggegeven met return.
#
# Met een while-loop kunnen meerdere bestellingen
# achter elkaar worden geplaatst. Het programma
# stopt wanneer de klant geen bestelling meer wil doen.
#
# Gebruikte technieken:
# - def en return
# - while-loop met een flag
# - if- en elif-statements
# - input() en int()
# - Berekeningen en f-strings
#
# Het belangrijkste oefendoel was het aanroepen van
# een functie binnen een while-loop en het gebruiken
# van de teruggegeven waarde voor iedere bestelling.
# ==========================================================

# ========================
# MIDDELEEUWSE SMEDERIJ
# ========================

# prijs berekening van een bestelling

def bestelling(wapen, aantal):
    if wapen == 'zwaard':
        prijs = 50
    elif wapen == 'bijl':
        prijs = 40
    elif wapen == 'dolk':
        prijs = 25
    totaal_prijs = prijs * aantal
    return totaal_prijs

# Verwerk bestellingen totdat de klant aangeeft te willen stoppen.
# Bereken en toon voor iedere bestelling de totale kosten.

bestellen_active = True

while bestellen_active:
    wapen = input(f"\nWelk wapen wil je bestellen? ")

    print(f"U heeft het volgende wapen besteld: {wapen}")

    aantal = int(input("Hoeveel exemplaren wilt u? "))

    print(f"\nU wilt {aantal}x {wapen} bestellen.")

    prijs = bestelling(wapen, aantal)

    print(f"De totale kosten bedragen: €{prijs:.2f}")

    herhaling = input(f"Wilt u nog een bestelling plaatsen? (ja/nee) ")

    if herhaling == 'nee':
        bestellen_active = False

print("Smederij gesloten")