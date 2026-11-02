# ==========================================================
# UITLEG PROJECT - DE ROBOTWERKPLAATS
# ==========================================================
#
# In dit project worden kapotte robots gerepareerd en
# verplaatst naar een lijst met gerepareerde robots.
# Hiervoor werken twee functies samen.
#
# Gebruikte technieken:
# - def: twee functies maken met verschillende taken.
# - Parameters: lijsten doorgeven aan functies.
# - while: robots verwerken zolang de lijst niet leeg is.
# - pop(): een robot uit de oorspronkelijke lijst halen.
# - append(): de robot aan een andere lijst toevoegen.
# - for: alle gerepareerde robots in een overzicht tonen.
#
# Het belangrijkste oefendoel was begrijpen hoe twee
# functies samenwerken met dezelfde lijst en hoe een
# lijst binnen een functie aangepast kan worden zonder
# return te gebruiken.
#
# Daarnaast wordt de variabele 'gerepareerd' tijdens
# iedere ronde van de while-loop opnieuw ingevuld,
# terwijl de lijst alle toegevoegde robots bewaart.
# ==========================================================

# Maak een lijst met kapotte robots en een lege lijst
# waarin de gerepareerde robots worden opgeslagen.

kapotte_robots = [
    'RX-100',
    'Titan-7',
    'Mecha-3',
    'Nova-9'
]

gerepareerde_robots = []

# Toon welke robots gerepareerd worden en verplaats
# ze daarna naar de lijst met gerepareerde robots.

def reperatie_robots(kapotte_robots, gerepareerde_robots):
    print("======== ROBOTWERKPLAATS ========")
    print()

    while kapotte_robots:
        gerepareerd = kapotte_robots.pop()
        print(f"{gerepareerd} wordt gerepareerd!")
        gerepareerde_robots.append(gerepareerd)
    print()

# Toont alle gerepareerde robots uit de bijgewerkte lijst.

def gemaakte_robots(gerepareerde_robots):
    print("======== REPARATIES VOLTOOID ==========")
    print()

    for gerepareerd in gerepareerde_robots:
        print(f"{gerepareerd} is weer operationeel!")
    print()

reperatie_robots(kapotte_robots, gerepareerde_robots)
gemaakte_robots(gerepareerde_robots) 