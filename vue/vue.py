from vue.LCD1602 import CharLCD1602

#Gere l'affichage pour l'ecran ldc
class LCDVue:
    def __init__(self):
        self.lcd = CharLCD1602()
        self.lcd.init_lcd()
        
    def afficher_message(self, message):
        self.lcd.clear()
        lignes = message.split("\n")
        for i, ligne in enumerate(lignes):
            if i <= 1:
                self.lcd.write(0, i, ligne)