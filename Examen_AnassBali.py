"""
categorie_a = ["Ford Fiesta (1), Volkswagen Polo (2)"]
categorie_b = ["Ford Focus (3), Audi A3 (4), Mercedes A klasse (5)"]
categorie_c = ["Audi A4 (6), BMW 3 (7), Mercedes C klasse 95 (8)"]
totaalprijs = []
btw = 121 / 100
print(categorie_a, categorie_b,categorie_c)
keuze = int(input("Voer de nummer in die bij de auto hoort die je wilt!"))
aantal_dagen = int(input("Hoeveel dagen wil je deze auto gebruiken?"))
auto = []
if keuze == 1 or 2:
    auto = 45
    totaalprijs.append(45 * aantal_dagen)
elif keuze == 3 or 4 or 5:
    auto = 55
    totaalprijs.append(55 * aantal_dagen)
elif keuze == 6 or 7 or 8:
    auto == 75
    totaalprijs.append(75 * aantal_dagen)
verzekering = input("Welke verzekering wil je: Standaard of Omnium")
if verzekering.lower() == "standaard":
    verzekering_kosten = 0.2 * keuze + 20
    totaalprijs.append(verzekering_kosten)
elif verzekering.lower() == 'omnium':
    verzekering_kosten = 0.3 * keuze + 25
    totaalprijs.append(verzekering_kosten)
kilometer = int(input("Hoeveel km heb je gereden?"))
if kilometer > 100:
    totaalprijs.append((kilometer - 100) * int(btw))

totaalprijs = sum(totaalprijs)
print("De auto kost:",auto, "euro")
print("De verzekering kost:",verzekering_kosten, "euro")
print("De aantal dagen zijn:",aantal_dagen, "dagen")
print("De aantal gereden kilometers zijn:",kilometer)
print("De totaal prijs zonder btw is:",totaalprijs, "euro")
print("De Totale prijs inc btw is:", totaalprijs * btw, "euro")
"""


"""
for i in range(1, 13):
    for j in range(i, i + 1):
        print(j, end=' ')
    if i % 4 == 0:
        print(' ')
"""

"""
def triatlon_m(geslacht, fietsen, lopen, zwemmen):
    if geslacht == 'man':
        if fietsen >= 20 and lopen >= 10 and zwemmen >= 3:
            print("Je bent geslaagd")
        elif fietsen >= 50 and lopen >= 5 and zwemmen >= 2:
            print("Je bent geslaagd")
        elif fietsen >= 45 and lopen >= 7 and zwemmen >= 2:
            print("Je bent geslaagd")
        else:
            print("Je bent niet geslaagd")
    elif geslacht == 'vrouw':
        if fietsen >= 15 and lopen >= 8 and zwemmen >= 3:
            print("Je bent geslaagd")
        elif fietsen >= 25 and lopen >= 10 and zwemmen >= 2:
            print("Je bent geslaagd")
        elif fietsen >= 40 and lopen >= 8 and zwemmen >= 2:
            print("Je bent geslaagd")
        else:
            print("Je bent niet geslaagd")


triatlon_m("man", 20, 50, 10)
"""