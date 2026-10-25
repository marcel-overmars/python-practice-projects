# ==========================================================
# UITLEG PROJECT - AUTOGARAGE
# ==========================================================
#
# In dit project worden drie auto's geregistreerd met
# behulp van een functie die een dictionary teruggeeft.
# De auto's worden opgeslagen in een lijst, waarna de
# kilometerstand van één auto wordt aangepast.
# Tot slot worden alle auto's en het totaal weergegeven.
#
# Gebruikte technieken:
# - def en return
# - Dictionaries maken, uitlezen en aanpassen
# - Dictionaries opslaan in een lijst
# - f-strings, .title() en len()
#
# Het belangrijkste oefendoel was het teruggeven van
# dictionaries met return en het verder gebruiken
# van deze gegevens in het programma.
# ==========================================================


# =========================================================
# Gebruik van functie voor het registreren van auto's
# =========================================================

def garage(merk, model, kilometerstand):
    auto = {
        'merk': merk,
        'model': model,
        'kilometerstand': kilometerstand
    }
    return auto

auto_1 = garage('toyota', 'yaris', 85_000)
auto_2 = garage('volkswagen', 'golf', 120_000)
auto_3 = garage('citroën', 'c1', 65_000)

automobiel = [
    auto_1,
    auto_2,
    auto_3
]

auto_2['kilometerstand'] = 125_000

# ==================
# Eindrapport
# ==================

print("==================")
print("=== AUTOGARAGE ===")
print("==================")
print()
print(f"{auto_1['merk'].title()} {auto_1['model'].title()} - {auto_1['kilometerstand']} km")
print(f"{auto_2['merk'].title()} {auto_2['model'].title()} - {auto_2['kilometerstand']} km")
print(f"{auto_3['merk'].title()} {auto_3['model'].title()} - {auto_3['kilometerstand']} km")
print()
print(f"Totaal geregistreerde auto's: {len(automobiel)}")