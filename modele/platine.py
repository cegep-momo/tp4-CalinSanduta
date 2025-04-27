from gpiozero import DistanceSensor, Button

#Ca gerer tout les liaisons avec le materiel, comme le capteur ou le boutons
class Platine:
    def __init__(self):
        self.capteur_distance = DistanceSensor(echo=12, trigger=17, max_distance=3)
        self.bouton_start = Button(16)
        self.bouton_mesure = Button(20)

    def lire_distance(self):
        distance_cm = self.capteur_distance.distance * 100
        distance_cm = round(distance_cm, 1)
        return distance_cm

    def bouton_start_presse(self):
        return self.bouton_start.is_pressed

    def bouton_mesure_presse(self):
        return self.bouton_mesure.is_pressed