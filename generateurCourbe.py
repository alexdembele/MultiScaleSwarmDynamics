import numpy as np
import matplotlib.pyplot as plt
import csv

nom_fichier = r'data/multiscale.csv'

# Déclarer une liste vide pour stocker les données
donnees = []

# Ouvrir le fichier CSV en mode lecture
with open(nom_fichier, 'r') as fichier_csv:
    # Créer un objet lecteur CSV
    lecteur_csv = csv.reader(fichier_csv)

    # Parcourir chaque ligne du fichier CSV
    for ligne in lecteur_csv:
        # Ajouter chaque ligne dans la liste de données
        donnees.append(ligne)

#conversion en array d'entier pour calcul
data = np.array(donnees,dtype=np.uint32)

Maximum=np.max(data,axis=0)
Minimum=np.min(data,axis=0)
Moyenne=np.mean(data,axis=0)

yfin = Moyenne[-1]
ydebut = Moyenne[6]


A=range(len(Maximum))
y5 = [yfin + abs(yfin-ydebut)*0.05 for i in A]
y_5 = [yfin - abs(yfin-ydebut)*0.05 for i in A]

i=10
while Moyenne[i]>y5[i]:
    i+=1


plt.plot(A,Maximum,label="maximum")
plt.plot(A,Minimum,label="minimum")
plt.plot(A,Moyenne,label="moyenne")
plt.plot(A,y5,'--',color='gray',alpha=0.5)
plt.plot(A,y_5,'--',color='gray',alpha=0.5)
plt.plot([i,i],[0,300],'--',color='gray',alpha=0.5)
plt.annotate("{}".format(i),(i,0),xytext=(i,-0))

plt.title("Number of Swarms, multiscale")
plt.legend()
plt.show()