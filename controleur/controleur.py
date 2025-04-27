import json
import time
import datetime
from modele.platine import Platine
from modele.moduleTP4 import Mesure
from vue.vue import LCDVue

#Le controleur gere toute la logique du projet 
class Controleur:
    def __init__(self):
        self.platine = Platine()
        self.lcd = LCDVue()
        self.systeme_actif = False
        self.dernier_affichage = time.time()

    def sauvegarder_mesure(self, mesure):
        try:
            with open("mesures.json", "a") as fichier:
                json.dump(mesure.__dict__, fichier)
                fichier.write("\n")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde : {e}")

    def boucle_principale(self):
        print("Le système est prêt.")
        while True:
            if self.platine.bouton_start_presse():
                if not self.systeme_actif:
                    self.systeme_actif = True
                    self.lcd.afficher_message("Systeme\ndemarre")
                    print("Système démarré.")
                    time.sleep(1)
                else:
                    self.systeme_actif = False
                    self.lcd.afficher_message("Systeme\narrete")
                    print("Système arrêté.")
                    time.sleep(1)
                    self.lcd.afficher_message("")

            if self.systeme_actif:
                if time.time() - self.dernier_affichage >= 5:
                    distance = self.platine.lire_distance()
                    self.lcd.afficher_message(f"Distance:\n{distance:.1f} cm")
                    print(f"Distance actuelle : {distance:.1f} cm")
                    self.dernier_affichage = time.time()

                if self.platine.bouton_mesure_presse():
                    distance = self.platine.lire_distance()
                    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    mesure = Mesure(date, distance)
                    self.sauvegarder_mesure(mesure)
                    self.lcd.afficher_message("Mesure\nprise!")
                    print(f"Mesure capturée : {distance:.1f} cm")
                    time.sleep(1)

            time.sleep(0.1)