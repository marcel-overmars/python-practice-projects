# ==========================================================
# UITLEG PROJECT - MAGISCHE BOEKWINKEL
# ==========================================================
#
# In dit project worden drie magische boeken geregistreerd
# met behulp van een functie die een dictionary teruggeeft.
# De boeken worden opgeslagen in een lijst, waarna de
# voorraad en prijzen worden aangepast.
#
# Vervolgens toont het programma alle boeken, controleert
# welke boeken een lage voorraad hebben en berekent het
# totaal aantal geregistreerde boektitels.
#
# Gebruikte technieken:
# - def en return
# - Dictionaries maken, uitlezen en aanpassen
# - Lijsten en append()
# - for-loops en if-statements
# - f-strings en len()
#
# Het belangrijkste oefendoel was het combineren van
# functies en dictionaries met eenvoudige controles
# en het verwerken van gegevens uit een lijst.
# ==========================================================

# ======================
# MAGISCHE BOEKWINKEL
# ======================

# Functie om de boeken te registreren

def registratie(boek, prijs, voorraad):
    boeken = {
        'boek': boek,
        'prijs': prijs,
        'voorraad': voorraad
    }
    return boeken

vuurmagie = registratie('Vuurmagie', 25, 8)
ijsmagie = registratie('Ijsmagie', 30, 5)
genezing = registratie('Genezing', 20, 12)

# Lijst om de dictionaries in te bewaren

magisch_boek =[]

magisch_boek.append(vuurmagie)
magisch_boek.append(ijsmagie)
magisch_boek.append(genezing)

# Aanpassing van de voorraad in de dictionary

vuurmagie['voorraad'] -= 3 # verkocht

# Stijging van de prijs van ijsmagie bijwerken in de dictionary

ijsmagie['prijs'] = 35

# =====================
# EINDRAPPORT
#======================

print("================================")
print(f"\tMAGISCHE BOEKWINKEL")
print("================================")
print()

# Tonen van de boeken en de gegevens via een for-loop

for boek in magisch_boek:
    print(boek)
print()

# Via een for-loop en een if-statement kijken welke boeken
# minder dan 10 exemplaren hebben
print("Lage voorraad")

for boek in magisch_boek:
    if boek['voorraad'] < 10:
        print(boek['boek'])
print()

# Totaal aantal boeken tonen met len()

print(f"Totaal aantal boektitels: {len(magisch_boek)}")