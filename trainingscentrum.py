# ==========================================================
# UITLEG PROJECT - TRAININGSCENTRUM
# ==========================================================
#
# In dit project worden sporters geregistreerd en wordt
# berekend hoeveel calorieën zij tijdens hun training
# hebben verbrand.
#
# Een functie berekent de calorieën en geeft het resultaat
# terug met return. Met een while-loop kunnen meerdere
# sporters achter elkaar worden geregistreerd.
#
# Het programma toont de trainingsresultaten en kan
# worden afgesloten door 'stop' in te voeren.
#
# Gebruikte technieken:
# - def en return
# - while True en break
# - input() en int()
# - Berekeningen met variabelen
# - if-statements en f-strings
#
# Het belangrijkste oefendoel was het combineren van
# een functie met een while-loop en het hergebruiken
# van de teruggegeven waarde binnen de loop.
# ==========================================================

# ===================
# TRAININGSCENTRUM
# ===================

# Berekening colorieën

"""1 minuut is 5 calorieën"""
def training(trainingstijd):
    calorieën = trainingstijd * 5
    return calorieën

print("===== TRAININGSCENTRUM =====")

# Registratie naam en trainingstijd

while True:
    naam = input("Wat is je naam? ")
    tijd = int(input("Hoeveel minuten heb je getraind? "))

    calorieën_verbrand = training(tijd)

    print(f"\nNaam sporter: {naam.title()}")
    print(f"Aantal trainingsminuten: {tijd}")
    print()
    print(f"{naam.title()} heeft ongeveer {calorieën_verbrand} calorieën verbrand.")
    
    nieuw = input("Nieuwe sporter registreren? ")

    if nieuw == 'stop':
        break

print("Programma afgesloten")