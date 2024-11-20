from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
import base64


with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
    )

with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read()
    )

choice = input("Vuoi criptare (1) o decriptare (2) un messaggio? Inserisci 1 o 2: ")

if choice == "1":
    
    message = input("Inserisci il messaggio da criptare: ").encode("utf-8")
    
    encrypted_message = public_key.encrypt(
        message,
        padding.PKCS1v15()  
    )
    
    encrypted_base64 = base64.b64encode(encrypted_message).decode("utf-8")
    print(f"Messaggio criptato: {encrypted_base64}")

elif choice == "2":
    encrypted_base64 = input("Inserisci il messaggio criptato in base64: ")
    encrypted_message = base64.b64decode(encrypted_base64)
    
    try:
        decrypted_message = private_key.decrypt(
            encrypted_message,
            padding.PKCS1v15()  
        )
        print(f"Messaggio decriptato: {decrypted_message.decode('utf-8')}")
    except Exception as e:
        print(f"Errore durante la decriptazione: {e}")

else:
    print("Scelta non valida. Inserisci 1 per criptare o 2 per decriptare.")
