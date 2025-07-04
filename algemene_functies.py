def mijn_functie_1():
    Argumenten=[2, 4, 10, 12]
    Teruggeefwaarde=[]
    for a in Argumenten:
        Teruggeefwaarde.append(a*a)
    return Teruggeefwaarde
print (mijn_functie_1())

def mijn_functie_2(a, b):
    uitvoer_lijst = []
    uitvoer_lijst.append(a + b)
    uitvoer_lijst.append(a - b)
    uitvoer_lijst.append(a * b)
    uitvoer_lijst.append(a / b)
    return uitvoer_lijst
print (mijn_functie_2(12,2))