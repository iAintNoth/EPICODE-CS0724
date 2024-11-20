from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
import base64

def sign_message(private_key, message):
    """Firma il messaggio usando la chiave privata e PSS padding"""
    signature = private_key.sign(
        message.encode("utf-8"),  
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()), 
            salt_length=padding.PSS.MAX_LENGTH  
        ),
        hashes.SHA256()  
    )
    return base64.b64encode(signature).decode("utf-8")  

def verify_signature(public_key, message, signature_base64):
    """Verifica la firma di un messaggio usando la chiave pubblica"""
    signature = base64.b64decode(signature_base64)  
    try:
      
        public_key.verify(
            signature,
            message.encode("utf-8"), 
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),  
                salt_length=padding.PSS.MAX_LENGTH  
            ),
            hashes.SHA256()  
        )
        return True  
    except Exception: 
        return False 
