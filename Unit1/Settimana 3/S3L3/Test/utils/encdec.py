import os
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

''' 
    Funzionamento: Il codice cifra un messaggio utilizzando una di crittografia simmetrica e asimettrica.
                   La chiave simmetrica cifre il messaggio, poi la stessa chiave viene cifrata dalla chiave pubblica.
                   Il destinatario poi con la sua chiave decriptera' la chiave AES per decriptare il messaggio.
'''

def load_keys(private_key_path, public_key_path):
    
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None)
    
    with open(public_key_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())
    
    return private_key, public_key

def encrypt_message(public_key, message):
    symmetric_key = os.urandom(32)  

    iv = os.urandom(16)  
    cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_message = message + ' ' * (16 - len(message) % 16)
    encrypted_message = encryptor.update(padded_message.encode("utf-8")) + encryptor.finalize()

    encrypted_symmetric_key = public_key.encrypt(
        symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return base64.b64encode(encrypted_symmetric_key).decode("utf-8"), base64.b64encode(encrypted_message).decode("utf-8"), base64.b64encode(iv).decode("utf-8")

def decrypt_message(private_key, encrypted_symmetric_key_base64, encrypted_message_base64, iv_base64):
    encrypted_symmetric_key = base64.b64decode(encrypted_symmetric_key_base64)
    encrypted_message = base64.b64decode(encrypted_message_base64)
    iv = base64.b64decode(iv_base64)

    symmetric_key = private_key.decrypt(
        encrypted_symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()

    return decrypted_message.decode("utf-8")
