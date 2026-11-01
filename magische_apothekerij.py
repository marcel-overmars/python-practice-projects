# ==========================================================
# UITLEG PROJECT - MAGISCHE APOTHEKERIJ
# ==========================================================
#
# In dit project worden bestellingen van toverdranken
# gecontroleerd op urgentie.
#
# Twee lijsten worden doorgegeven aan een functie:
# een bestellijst en een lijst met dringende dranken.
#
# De eerste for-loop controleert iedere bestelling
# met if/else en verzamelt dringende bestellingen
# met append() in een nieuwe, aparte lijst.
#
# De tweede for-loop doorloopt deze nieuwe lijst
# en toont alle dringende bestellingen in een overzicht.
#
# Gebruikte technieken:
# - def en parameters
# - Meerdere lijsten doorgeven aan een functie
# - Twee for-loops binnen één functie
# - if/else en de in-operator
# - Een lege lijst aanmaken en vullen met append()
# - f-strings
#
# Het belangrijkste oefendoel was het combineren
# van meerdere handelingen binnen één functie
# en het verzamelen en verwerken van lijstgegevens.
# ==========================================================

# Lijst van bestellingen en dringende dranken.

bestellingen = [
    'heeldrank',
    'mana-elixer',
    'onzichtbaarheidsdrank',
    'antigif',
    'krachtelixer'
]

dringende_dranken = [
    'heeldrank',
    'antigif'
]

# Controleer iedere bestelling en verzamel
# de dringende bestellingen in een aparte lijst.
# Toon daarna het volledige spoedoverzicht.

print("======== MAGISCHE APOTHEKERIJ =========")
print()

def controleer_bestellingen(normale, dringende):
    dringende_dranken_gecontroleerd = []
    for normaal in normale:
        if normaal in dringende:
            print(f"{normaal}: DRINGENDE BESTELLING!")
            dringende_dranken_gecontroleerd.append(normaal)
        else:
            print(f"{normaal}: gewone bestelling")
    print()
    print("======== SPOEDOVERZICHT ========")
    print()
    print("Dringende bestellingen:")
    for gecontroleerd in dringende_dranken_gecontroleerd:
        print(gecontroleerd)

controleer_bestellingen(bestellingen, dringende_dranken)

print(f"\nAlle bestellingen zijn gecontroleerd.")