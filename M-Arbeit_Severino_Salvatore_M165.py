import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=client["spiele"]
mycol=mydb["pcgames"]


def finden(suchen8,titel8): #Suchen funktion Normal für String / Für 1
    s = mycol.find_one({suchen8:titel8})
    print(s)

def findenInt(suchen,titel): #Suchen funktion INT / Für 1
    s = mycol.find_one({suchen:(int(titel))})
    print(s)

def insert(titell,ausgabejahrr,verkaufszahlenn,altersgrenzee,artt,wertungg): #Einfügen in die Collection / Insert
    docsa ={"titel":titell,"ausgabejahr":ausgabejahrr,"verkaufszahlen":verkaufszahlenn,"altersgrenze":altersgrenzee,"art":[artt],"wertung":wertungg}
    i = mycol.insert_one(docsa)
    ausgabeprint = mycol.find_one({"titel":titell})
    print(ausgabeprint, "document successfully created")

def mehreresuchen(suchen3,titel3): #Suchen funktion Normal für String / Für mehrere
    mysa = {suchen3:titel3}
    docsa =  mycol.find(mysa,{ "_id": 0})
    for s in docsa:
        print(s)

def mehreresuchenINT(suchen5,titel5): #Suchen funktion INT / Für mehrere
    mysa = {suchen5:(int(titel5))}
    docsa =  mycol.find(mysa,{ "_id": 0})
    for s in docsa:
        print(s)

def loeschendatensatz(löschenD, wNameloeschen): #Suchen funktion für Buchstaben (String) / Für mehrere
    loeschenvariable = {löschenD : wNameloeschen}
    x = mycol.delete_many(loeschenvariable)
    print(x.deleted_count, " documents deleted.")

def loeschendatensatzINT(löschenI, wNameloeschenI): #Suchen funktion für INT / Für mehrere
    loeschenvariable = {löschenI:(int(wNameloeschenI))}
    x = mycol.delete_many(loeschenvariable)
    print(x.deleted_count, " documents deleted.")

def regexsuche(regexx):
    sasa = mycol.find({"titel": {"$regex": regexx}}, {"_id" : 0})
    for s in mycol.find(regexend, {"_id": 0}):
        print(s)


print("\nWILLKOMMEN IN DER DATENBANK SPIELE. WAS MÖCHTEN SIE MACHEN?\n\n1)Nach einem Eintrag suchen\n2)Etwas in die Collection hinzufügen\n3)einen Datensatz löschen\nProgramm beenden? (Gebe 'beenden' ein)")
eingabe = input("--->")
#Ab hier Beginnt meine While-Schleife, es beginnt immer wieder von vorne. 
while eingabe != "beenden": #Unterbruch, wenn ich dieses Wort(beenden) eingebe.
    if eingabe == "1": 
        print("NACH WAS MÖCHTEN SIE SUCHEN?")
        frage=input("1) ein Datensatz suchen\n2) mehrere Datensätze suchen\n3) mit Regex suchen?\n--->")
        if frage == "1": #es sucht nur nach 1 Datensatz
             print("NACH WELCHEN KRITERIEN MÖCHTEN SIE SUCHEN?")
             print("titel\nausgabejahr\nverkaufszahlen\naltersgrenze\nart\nwertung")
             eingabe8= input("--> ")
             print("Wie heisst Ihr Objekt, nachdem Sie suchen?: ")
             salvi=input("---> ")
             if salvi.isdigit():
                 findenInt(eingabe8,salvi)
             else:
                 finden(eingabe8,salvi)
        elif frage =="2": #es sucht nach mehreren Datensätzen
            print("NACH WELCHEN KRITERIEN MÖCHTEN SIE SUCHEN?")
            print("titel\nausgabejahr\nverkaufszahlen\naltersgrenze\nart\nwertung")
            eingabe8= input("---> ")
            print("Wie heisst Ihr Objekt, nachdem Sie suchen?: ")
            salvi=input("---> ")
            if salvi.isdigit():
                 mehreresuchenINT(eingabe8,salvi)
            else:
                 mehreresuchen(eingabe8,salvi)
        elif frage == "3": #Regex
            print("ANFANGSBUCHSTABE EINGEBEN, NACHDEM SIE SUCHEN MÖCHTEN.")
            regexxfrage = "titel"
            regextext = input()
            regexend = {regexxfrage: {'$regex': regextext}}
            for s in mycol.find(regexend, {"_id": 0}):
                print(s)

    elif eingabe =="3": #Löschen, nach was möchte ich löschen
        frage = input("Welchen Datensatz möchtest du löschen?\ntitel\nausgabejahr\nverkaufszahlen\naltersgrenze\nart\nwertung\n---> ") 
        wNameloeschen = input("Geben Sie ein, was Sie Löschen möchten. ---> ") 
        if  wNameloeschen.isdigit(): # Löschen INT
            loeschendatensatzINT(frage, wNameloeschen)
        else: # Löschen 
            loeschendatensatz(frage, wNameloeschen)
    elif eingabe =="2": #Etwas in die Collection einfügen.
        print("Füllen Sie die Untenstehende Informationen aus und der Eintrag wird erstellt.")
        titell = input("titel: ") #String
        ausgabejahrr = int(input("ausgabejahr: ")) #INT
        verkaufszahlenn = int(input("verkaufszahlen: ")) #INT
        altersgrenzee = int(input("altersgrenze: ")) #INT
        artt=input("art: ") #Array
        wertungg = int(input("wertung: ")) #INT
        insert(titell,ausgabejahrr,verkaufszahlenn,altersgrenzee,artt,wertungg) #Mit diesem Befehl kann ich sagen, dass es in MongoDbCompass eingefügt wird.
        
    print("\nMöchten Sie nochmals nach etwas suchen?\n\n1)Nach einem Eintrag suchen\n2)Etwas in die Collection hinzufügen\n3)Einen Datensatz löschen\nProgramm beenden? (Gebe 'beenden' ein)")
    eingabe=input()

