from gpiozero import Button
from time import sleep

bouton = Button(16)

print("appuie sur le bouton")

try:
    while True:
        if bouton.is_pressed:
            print("Bouton Start appuye")
        else:
            print("Bouton pas appuye")
        sleep(0.5)
except KeyboardInterrupt:
    print("Arret du test")