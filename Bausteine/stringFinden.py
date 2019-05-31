#gefunden = False

anzeige1 = "Wir haben eine Haushaltsauflösung"
anzeige2 = "Wir verkaufen Staubsauger"
anzeige3 = "Kaufe Schmuck"

anzeigenliste = [anzeige1,anzeige2,anzeige3]

begriff1= "Haushaltsauflösung"
begriff2= "Staubsauger"
begriff3= "Schmuck"

begriffsliste = [begriff1,begriff2,begriff3]

#print(begriffsliste)
#print(anzeigenliste[0])

for anzeige in anzeigenliste:
    for begriff in begriffsliste:
        if begriff in anzeige:
            print("gefunden!")
        else:
            print("nicht gefunden!")





