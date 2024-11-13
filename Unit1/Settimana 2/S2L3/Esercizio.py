

city = input("Inserisci la tua città: ")
while not city.isalpha() or city.strip() == "":
    print("Per favore, inserisci un nome di citta' valido(Usa solo lettere)")
    city = input("Inserisci la tua città: ")

animal = input("Inserisci il nome del tuo animale: ")
while animal.strip() == "":
    print("Per favore, inserisci il nome del tuo animale")
    animal = input("Inserisci il nome del tuo animale: ")

    
band_name = city + " " + animal



print("Il nome della band e':", band_name)

