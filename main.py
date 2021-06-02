from Parlament import Landtag
import pandas as pd
import myMathFunctions
import wahlergebnisse


landesstimmen = wahlergebnisse.landesstimmen
gesamtstimmenpool = wahlergebnisse.gesamtstimmenpool

def berechne_landtagskennzahlen(ltg: Landtag):
    ltg.bestimme_parlamentsparteien(gesamtstimmenpool)
    ltg.berechne_quoten_parteien()
    ltg.berechne_sitze_volle_zahl()
    ltg.berechne_nachkommastellen()
    ltg.sort_parteien_by_attr("nachkommastellen")
    ltg.vergebe_restsitze_anhand_nachkommastellen()
    ltg.sort_parteien_by_attr("stimmzahl")

def main():
    #Berechnung des "Standard"-ltg mit 110 Sitzen
    hlt = Landtag(landesstimmen)
    berechne_landtagskennzahlen(hlt)    
    data = [vars(p) for p in hlt.parteien]
    print(pd.DataFrame.from_dict(data))
    print()


   #Bestimme zwei mögliche Größen für die Gesamtsitze des Landtags anhand 
    #der Überhangmandate
    min_max_sitze = hlt.determine_seats_by_ueberhangmandate()
    
    if min_max_sitze == None:
        print ("Keine Überhangmandate, das Parlament bleibt bei 110 Sitzen.")   
    else:
        #Berechnung des ltg mit Überhangmandaten: die Min-Variante
        hltMin = Landtag(landesstimmen, min_max_sitze[1])
        berechne_landtagskennzahlen(hltMin)
        # for p in ltgMin.parteien:
        #     print(p)
        data = [vars(p) for p in hltMin.parteien]
        print(pd.DataFrame.from_dict(data))
        print()

        hltMax = Landtag(landesstimmen, min_max_sitze[2])
        berechne_landtagskennzahlen(hltMax)
        
        # for p in hltMax.parteien:
        #     print(p)
        data = [vars(p) for p in hltMax.parteien]
        print(pd.DataFrame.from_dict(data))


if __name__ == "__main__": main() 
