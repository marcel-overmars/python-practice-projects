# ==========================================================
# UITLEG PROJECT - RUIMTEACADEMIE
# ==========================================================
#
# In dit project voert een astronaut vijf trainingsrondes
# uit en verdient daarbij punten.
#
# Een functie berekent de punten op basis van het aantal
# behaalde sterren en geeft deze terug met return.
#
# Een while-loop houdt bij hoeveel trainingsrondes zijn
# voltooid en stopt automatisch na de vijfde ronde.
#
# De verdiende punten worden met += opgeteld in een
# aparte variabele, zodat het totaal bewaard blijft.
#
# Gebruikte technieken:
# - def en return
# - while-loop met een teller
# - if- en elif-statements
# - input() en f-strings
# - Optellen met +=
# - Variabelen bijhouden en hergebruiken
#
# Het belangrijkste oefendoel was het combineren van
# een functie met een while-loop en het bijhouden van
# zowel een teller als een totaalwaarde.
# ==========================================================

# Bepaal hoeveel punten de astronaut verdient
# op basis van het aantal behaalde sterren.

def sterren(ster):
    if ster == 1:
        punten = 10
    elif ster == 2:
        punten = 20
    elif ster == 3:
        punten = 30
    elif ster == 4:
        punten = 40
    elif ster == 5:
        punten = 50
    return punten

# Voer 5 trainingsrondes uit en tel de
# verdiende punten bij het totaal op.

trainingsrondes = 0
totaal_punten = 0

naam = input("Wat is je naam? ")

while trainingsrondes < 5:
    trainingsrondes += 1

    print(f"Trainingsronde: {trainingsrondes}")
    ster = int(input("Hoeveel sterren zijn er behaald? "))
    punten = sterren(ster)
    totaal_punten += punten

    print(f"Het aantal behaalde punten: {punten}")
    print()

# Toon het eindrapport met de naam van de astronaut,
# het aantal voltooide rondes en de totaalpunten.

print("======== EINDRAPPORT ========")
print()
print(f"Astronaut: {naam.title()}")
print(f"Trainingsrondes voltooid: {trainingsrondes}")
print(f"Totaal aantal punten: {totaal_punten}")
print()
print("Training afgerond")