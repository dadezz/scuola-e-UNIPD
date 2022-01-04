#Davide Zambon
def usdeur (Mi, Mf, Passo):
    tabellaeuro = []
    tabelladollari = []
    tabellasterline = []
    for i in range (Mi, Mf, Passo):
        tabelladollari.append(i)
        a = i/1.37
        tabellasterline.append(a)
        b = a/0.88
        tabellaeuro.append(b)
    tabellatotale = []
    for i in range(len(tabellaeuro)):
        listaprovvisoria = [tabellaeuro[i], tabelladollari[i], tabellasterline[i]]
        tabellatotale.append(listaprovvisoria)
    print(tabellatotale)
        
    

usdeur(0, 200, 10)
