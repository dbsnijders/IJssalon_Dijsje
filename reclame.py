def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = (prijs * (1 - korting))
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro."
    return uitvoer
print (aanbieding_1 ("aardbei", 4, 0.1))


def inkomsten_totaal(inkomsten,btw):
    totaal=sum (inkomsten)
    bedrag = (totaal * btw)
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
    return uitvoer
week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.09
print(inkomsten_totaal(week_inkomsten, btw_percentage))

def laag_en_hoog(mijn_lijst):
    return [min(mijn_lijst), max(mijn_lijst)]
week_inkomsten = [220, 430, 125, 160, 205, 90, 345] 
print (laag_en_hoog(week_inkomsten))   


def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    gemiddelde_waarde =(totaal / aantal)
    uitvoer = f"De gemiddelde inkomsten deze week zijn {gemiddelde_waarde} euro."
    return uitvoer
week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
print (gemiddelde (week_inkomsten))

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
getallen=[10,5,3,2,1,2,9]
print(meervoudig(getallen))

from algemene_functies import mijn_functie_2

def combinatie(invoer_lijst_2):
    korte_lijst= laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst)
print (combinatie)