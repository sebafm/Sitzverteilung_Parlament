from Parlament import Landtag
import pandas as pd
from util import myMathFunctions

def main():
    # """Ergebnisse der Wahl von 2013:"""
    # landesstimmen = 3130781
    # gesamtstimmenpool = {
    #     "CDU": 1199633,
    #     "SPD": 961896,
    #     "FDP": 157451,
    #     "GRÜNE": 348661,
    #     "DIE LINKE": 161488,
    #     "FREIE WÄHLER": 38433
    # }

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
        ("Öko_Linx", 32457, 0)
    ]

    #Berechnung des "Standard"-HLT mit 110 Sitzen
    hlt = Landtag(landesstimmen)
    hlt.bestimme_parlamentsparteien(gesamtstimmenpool)
    hlt.berechne_quoten_parteien()
    hlt.berechne_sitze_volle_zahl()
    hlt.assign_restsitze()
    
    #Bestimme zwei mögliche Größen für die Gesamtsitze des Landtags anhand 
    #der Überhangmandate
    min_max_sitze = hlt.determine_seats_by_ueberhangmandate()

    #Berechnung des HLT mit Überhangmandaten: die Max-Variante
    hltMin = Landtag(landesstimmen, min_max_sitze[1])
    hltMin.bestimme_parlamentsparteien(gesamtstimmenpool)
    hltMin.berechne_quoten_parteien()
    hltMin.berechne_sitze_volle_zahl()
    hltMin.assign_restsitze()
    # for p in hltMin.parteien:
    #     print(p)

    data = [vars(p) for p in hltMin.parteien]
    print(pd.DataFrame.from_dict(data))

    hltMax = Landtag(landesstimmen, min_max_sitze[2])
    hltMax.bestimme_parlamentsparteien(gesamtstimmenpool)
    hltMax.berechne_quoten_parteien()
    hltMax.berechne_sitze_volle_zahl()
    hltMax.assign_restsitze()
    # for p in hltMax.parteien:
    #     print(p)

    data = [vars(p) for p in hltMax.parteien]
    print(pd.DataFrame.from_dict(data))


if __name__ == "__main__": main() 
