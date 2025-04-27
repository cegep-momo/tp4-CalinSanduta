
#Stocke la date et la distance 
class Mesure: 
    def __init__(self, dateHeureMesure, dataMesure):
        self.dateHeureMesure = dateHeureMesure
        self.dataMesure = dataMesure
    
    def __repr__(self):
        return f"Mesure({self.dateHeureMesure}, {self.dataMesure})"
    
    def afficherMesure(self):
        return f"Date et Heure: {self.dateHeureMesure}\nDistance: {self.dataMesure} cm"