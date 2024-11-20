def caesar_decrypt(ciphertext, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.replace('j', '').replace('k', '').replace('w', '').replace('x', '').replace('y', '').replace('z', '')
    
    decrypted_message = ''
    
    for char in ciphertext:
        if char.lower() in alphabet:
            char_index = alphabet.find(char.lower())
            
            new_index = (char_index - shift) % len(alphabet)
            
            if char.isupper():
                decrypted_message += alphabet[new_index].upper()
            else:
                decrypted_message += alphabet[new_index]
        else:
            decrypted_message += char

    return decrypted_message

ciphertext = input("Inserisci il messaggio cifrato: ")
shift = int(input("Inserisci la chiave utilizzata per cifrare il messaggio: "))

decrypted_message = caesar_decrypt(ciphertext, shift)

print(f"Messaggio decodificato: {decrypted_message}")
