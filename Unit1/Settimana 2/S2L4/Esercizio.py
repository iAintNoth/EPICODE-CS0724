import math

def richiedi_input(messaggio):
    while True:
        try:
            valore = float(input(messaggio))
            if valore <= 0:
                print("Per favore, inserisci un numero positivo maggiore di zero.")
            else:
                return valore
        except ValueError:
            print("Input non valido. Inserisci un numero positivo maggiore di zero.")

def perimetro_quadrato():
    lato = richiedi_input("Inserisci il lato del quadrato: ")
    perimetro = lato * 4
    print(f"Il perimetro del quadrato è: {perimetro}")

def perimetro_cerchio():
    raggio = richiedi_input("Inserisci il raggio del cerchio: ")
    perimetro = 2 * math.pi * raggio
    print(f"La circonferenza del cerchio è: {perimetro}")

def perimetro_rettangolo():
    base = richiedi_input("Inserisci la base del rettangolo: ")
    altezza = richiedi_input("Inserisci l'altezza del rettangolo: ")
    perimetro = 2 * (base + altezza)
    print(f"Il perimetro del rettangolo è: {perimetro}")


def perimetro_triangolo():
    lato1 = richiedi_input("Inserisci il primo lato del triangolo: ")
    lato2 = richiedi_input("Inserisci il secondo lato del triangolo: ")
    lato3 = richiedi_input("Inserisci il terzo lato del triangolo: ")
    perimetro = lato1 + lato2 + lato3
    print(f"Il perimetro del triangolo è: {perimetro}")

def perimetro_poligono():
    lato = richiedi_input("Inserisci la lunghezza del lato del poligono regolare: ")
    num_lati = int(input("Inserisci il numero di lati del poligono regolare: "))
    
    if num_lati <= 0:
        print("Il numero di lati deve essere maggiore di zero.")
        return

    perimetro = lato * num_lati
    print(f"Il perimetro del poligono regolare è: {perimetro}")

def menu_perimetro():
    print("Scegli una figura per calcolare il perimetro:")
    print("1. Quadrato")
    print("2. Cerchio")
    print("3. Rettangolo")
    print("4. Triangolo")
    print("5. Poligono regolare")

    scelta = input("Inserisci il numero corrispondente alla tua scelta (1/2/3/4/5): ")

    if scelta == "1":
        perimetro_quadrato()
    elif scelta == "2":
        perimetro_cerchio()
    elif scelta == "3":
        perimetro_rettangolo()
    elif scelta == "4":
        perimetro_triangolo()
    elif scelta == "5":
        perimetro_poligono()
    else:
        print("Scelta non valida. Riprova.")

menu_perimetro()
