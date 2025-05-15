compteur=0
try:
    with open("client","r") as fichier:
        for ligne in fichier:
            compteur+=1
    print("Nombre total de lignes:",compteur)
except FileNotFoundError:
    print("❌ Erreur : le fichier est introuvable!")