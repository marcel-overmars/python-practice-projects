# ==========================================================
# UITLEG PROJECT - MUSEUMBEHEER
# ==========================================================
#
# In dit project maak ik een registratiesysteem voor een
# museum met historische voorwerpen. De voorwerpen worden
# geregistreerd, opgeslagen en beheerd in een collectie.
#
# Gebruikte onderdelen:
# - Functies met def en return
# - Een dictionary teruggeven vanuit een functie
# - Optionele parameters met None
# - Dictionaries opslaan in een lijst
# - Voorwerpen verwijderen met remove()
# - For-loops en if-statements
# - Gegevens controleren en vergelijken
# - Het aantal voorwerpen bepalen met len()
#
# Het belangrijkste oefenonderdeel was het teruggeven
# van dictionaries met return en het zelfstandig
# combineren van eerder geleerde technieken.
# ==========================================================

# ================================================
# Museumbeheer historische voorwerpen collectie
# ================================================

def museumcollectie(voorwerp, herkomst, leeftijd, bijzonderheden=None):
    collectie = {
        'voorwerp': voorwerp,
        'herkomst': herkomst,
        'leeftijd': leeftijd
    }

    if bijzonderheden:
        collectie['bijzonderheden'] = bijzonderheden
    return collectie

voorwerp_1 = museumcollectie('Romeins zwaard', 'Italië', 1800)
voorwerp_2 = museumcollectie('Gouden masker', 'Egypte', 3200, 'koninklijk')
voorwerp_3 = museumcollectie('Vikingschild', 'Noorwegen', 1100)
voorwerp_4 = museumcollectie('Oude vaas', 'Griekenland', 2400, 'beschadigd')

voorwerpen = [
    voorwerp_1,
    voorwerp_2,
    voorwerp_3,
    voorwerp_4
]

for voorwerp in voorwerpen:
    print(voorwerp)
print()

# ====================================================
# Verwijdering van beschadigd stuk uit de collectie
# ====================================================

voorwerpen.remove(voorwerp_4)

for voorwerp in voorwerpen:
    print(voorwerp)
print()

# ==================
# Eindrapport
# ==================

print("========================")
print("=== MUSEUM COLLECTIE ===")
print("========================")
print()

for voorwerp in voorwerpen:
    print(voorwerp)
print()

print(f"Totaal aantal voorwerpen: {len(voorwerpen)}")
print()
print("Ouder dan 3000 jaar:")

for voorwerp in voorwerpen:
    if voorwerp['leeftijd'] >= 3000:
        print(voorwerp['voorwerp'])