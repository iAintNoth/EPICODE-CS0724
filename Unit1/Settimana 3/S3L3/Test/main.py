from utils.encdec import load_keys, encrypt_message, decrypt_message
from utils.firma import sign_message, verify_signature

PRIVATE_KEY_PATH = "../private_key.pem"
PUBLIC_KEY_PATH = "../public_key.pem"

private_key, public_key = load_keys(PRIVATE_KEY_PATH, PUBLIC_KEY_PATH)

def ask_to_continue():
    while True:
        choice = input("Vuoi fare altro? [Y/n] ").strip().lower()
        if choice in ("y", "yes", ""):
            return True
        elif choice in ("n", "no"):
            return False
        else:
            print("Risposta non valida. Inserisci 'Y' per sì o 'n' per no.")

while True:
    print("\nScegli un'operazione:")
    print("1. Cripta un messaggio")
    print("2. Decripta un messaggio")
    print("3. Firma un messaggio")
    print("4. Verifica la firma di un messaggio")
    print("5. Esci")

    choice = input("Inserisci il numero dell'operazione: ")

    if choice == "1":
       
        message = input("Inserisci il messaggio da criptare: ")
        encrypted_symmetric_key, encrypted_message, iv = encrypt_message(public_key, message)
        print(f"\nMessaggio criptato: {encrypted_message} \n")
        print(f"Chiave simmetrica cifrata: {encrypted_symmetric_key} \n")
        print(f"IV: {iv}\n")

    elif choice == "2":
       
        encrypted_symmetric_key = input("Inserisci la chiave simmetrica cifrata in base64: ")
        encrypted_message = input("Inserisci il messaggio criptato in base64: ")
        iv = input("Inserisci l'IV in base64: ")

        try:
            decrypted = decrypt_message(private_key, encrypted_symmetric_key, encrypted_message, iv)
            print(f"Messaggio decriptato: {decrypted}\n")
        except Exception as e:
            print(f"Errore nella decriptazione: {e}")

    elif choice == "3":
      
        message = input("Inserisci il messaggio da firmare: ")
        signature = sign_message(private_key, message)
        print(f"Firma (in base64): {signature}")

    elif choice == "4":

        message = input("Inserisci il messaggio originale: ")
        signature = input("Inserisci la firma in base64: ")
        is_valid = verify_signature(public_key, message, signature)
        if is_valid:
            print("La firma è valida.")
        else:
            print("La firma NON è valida.")

    elif choice == "5":
       
        print("Uscita dal programma.")
        break

    else:
        print("Scelta non valida. Riprova.")

    if not ask_to_continue():
        print("Grazie per aver usato il programma. Uscita.")
        break
