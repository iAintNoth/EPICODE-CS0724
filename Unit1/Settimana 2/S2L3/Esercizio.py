

city = input("Inserisci la tua città: ")
while not all(c.isalpha() or c.isspace() for c in city) or city.strip() == "":     # Controllo se il nome contiene solo lettere e non sia una stringa vuota
    print("Per favore, inserisci un nome di citta' valido(Usa solo lettere).")
    city = input("Inserisci la tua città: ")

animal = input("Inserisci il nome del tuo animale: ")
while animal.strip() == "":                                                         #  Controllo se il nome non sia una stringa vuota
    print("Per favore, inserisci il nome del tuo animale.")
    animal = input("Inserisci il nome del tuo animale: ")


band_name = city + " " + animal



print(f"Il nome della band e': {band_name}")

