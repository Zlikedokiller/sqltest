import datetime
import socket

# Adresse IP et port du serveur de temps public
time_server = "time.nist.gov"
port = 13

# Création d'un objet socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur de temps public
sock.connect((time_server, port))

# Récupération de la réponse du serveur de temps public
response = sock.recv(1024).decode("utf-8")

# Fermeture de la connexion au serveur de temps public
sock.close()

# Traitement de la réponse pour récupérer l'heure
time_str = response.split(" ")[2]
time_list = time_str.split(":")
current_time = datetime.datetime.utcnow().replace(hour=int(time_list[0]), minute=int(time_list[1]), second=int(time_list[2]))

print("L'heure publique est :", current_time)
