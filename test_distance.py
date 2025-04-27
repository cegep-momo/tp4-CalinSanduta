from gpiozero import DistanceSensor
from time import sleep 

capteur = DistanceSensor(echo=12, trigger=17, max_distance=3)

try:
    while True:
        distance_cm = capteur.distance * 100
        distance_cm = round(distance_cm, 1)
        print(f"Distance mesuree : {distance_cm} cm")
        sleep(1)
except KeyboardInterrupt:
    print("Arret programme ")