import datetime

from controleur.controleur import Controleur
from modele.moduleTP4 import Mesure

# fichier qui permet de gerer le tout, tout demarrer
if __name__ == "__main__":
    app = Controleur()
    app.boucle_principale()