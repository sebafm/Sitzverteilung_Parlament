import math

#####################################################################
# Eine beliebige Partei:
#####################################################################
class Partei:

    def __init__(self, name, stimmzahl, direktmandate):
        self.name = name
        self.stimmzahl = stimmzahl
        self.direktmandate = direktmandate
        self.sitze_nach_voller_zahl = 0
        self.sitz_anhand_nachkommastellen = 0
        self.quote = 0
    
    def __str__(self):
        return (f"Name: {self.name}, \n\tStimmzahl: {self.stimmzahl}, \n\tSitze_volle_Zahl: {self.sitze_nach_voller_zahl}, \
            \n\tSitze_Nachkommastellen: {self.sitz_anhand_nachkommastellen}, \n\tDirektmandate: {self.direktmandate}, \n\tQuote im Landtag: {self.quote}")

    def get_sitze_landesliste(self):
        return self.sitze_nach_voller_zahl + self.sitz_anhand_nachkommastellen
    
    def berechne_ueberhangmandate(self):
        if self.direktmandate > self.get_sitze_landesliste():
            return self.direktmandate - self.get_sitze_landesliste()
        else: 
            return 0

######################################################################
# Der Landtag:
######################################################################
class Landtag:
    def __init__(self, landesstimmen, sitze=110):
        self.landesstimmen = landesstimmen
        self.sitze = sitze
        self.parteien = []

    def bestimme_parlamentsparteien(self, parteien):
        for p in parteien:
            if p[1] / self.landesstimmen > 0.05:
                self.parteien.append(Partei(p[0], p[1], p[2]))
    
    def __berechne_gesamtstimmen_parlamentsparteien(self):
        ges = 0
        for p in self.parteien:
            ges += p.stimmzahl
        return ges
    
    def berechne_quoten_parteien(self):
        for p in range(len(self.parteien)):
             self.parteien[p].quote = self.parteien[p].stimmzahl * self.sitze / self.__berechne_gesamtstimmen_parlamentsparteien()

    def berechne_sitze_volle_zahl(self):
        for p in range(len(self.parteien)):
            self.parteien[p].sitze_nach_voller_zahl = math.floor(self.parteien[p].quote)
    
    def assign_sitze_nachkommastellen(self):
        lst = []
        for p in range(len(self.parteien)):
            nkstell = self.parteien[p].quote - math.floor(self.parteien[p].quote)
            name = self.parteien[p].name
            lst.append((nkstell, name))
        


#######################################################################

def main():
    #"""Ergebnisse der Wahl von 2018"""
    landesstimmen = 2881261        
    gesamtstimmenpool = [
        ("CDU", 776910, 40),
        ("SPD", 570446, 10),
        ("GRÜNE", 570512, 5),
        ("LINKE", 181332, 0),
        ("FDP", 215946, 0),
        ("AfD", 378692, 0),
        ("Graue_Panther", 25352, 0),
        ("Oeko_Linx", 32457, 0)
    ]

    hlt = Landtag(landesstimmen)
    hlt.bestimme_parlamentsparteien(gesamtstimmenpool)
    hlt.berechne_quoten_parteien()
    hlt.berechne_sitze_volle_zahl()
    for p in hlt.parteien:
        print(p)


if __name__ == "__main__": main() 
