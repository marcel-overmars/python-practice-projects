# ==========================================================
# UITLEG PROJECT - RUIMTESTATION NOVA
# ==========================================================
#
# In dit project wordt het energieverbruik van een
# ruimtestation bijgehouden.
#
# Een functie bepaalt hoeveel energie een gekozen
# activiteit verbruikt en geeft deze waarde terug
# met return.
#
# Na iedere activiteit wordt het energieverbruik
# afgetrokken van de beschikbare energie.
# Met een while-loop kunnen meerdere activiteiten
# achter elkaar worden uitgevoerd.
#
# Het programma stopt wanneer de gebruiker 'stop'
# invoert en toont vervolgens de resterende energie.
#
# Gebruikte technieken:
# - def en return
# - while-loop met een stopvoorwaarde
# - if- en elif-statements
# - input() en f-strings
# - Berekeningen met -=
# - Variabelen aanpassen en hergebruiken
#
# Het belangrijkste oefendoel was het combineren
# van een functie met een while-loop en het bijhouden
# van een waarde die na iedere ronde verandert.
# ==========================================================

# Startenergie van het ruimtestation.
# Energieverbruik van een gekozen activiteit bepalen.

startenergie = 500

def verbruik(activiteit):
    if activiteit == 'verlichting':
        energieverbruik = 20
    elif activiteit == 'communicatie':
        energieverbruik = 40
    elif activiteit == 'zuurstofsysteem':
        energieverbruik = 60
    return energieverbruik

# Berekening en de eindstand van de energie.

nieuwe_activiteit = ""

while nieuwe_activiteit != 'stop':
    activiteit = input("Welke activiteit wordt uitgevoerd? ")

    energieverbruik = verbruik(activiteit)

    startenergie -= energieverbruik

    print(f"\nEnergieverbruik: {energieverbruik}")
    print(f"Energie over: {startenergie}")

    nieuwe_activiteit = input(f"\nWilt u nog een activiteit uitvoeren? (ja/stop) ")

print(f"\nRuimtestation afgesloten.")
print(f"Energie over: {startenergie}")