from HareNiemeyer import *
from Ueberhangmandatsrechner import *

def main():
    """Wahl von 2018"""
    landesstimmen = 2881261        
    gesamtstimmenpool = {
        "CDU": 776910,
        "SPD": 570446,
        "GRÜNE": 570512,
        "LINKE": 181332,
        "FDP": 215946,
        "AfD": 378692,
        "Graue_Panther": 25352,
        "Oeko_Linx": 32457
    }

    # """Wahl von 2013:"""
    # landesstimmen = 3130781
    # gesamtstimmenpool = {
    #     "CDU": 1199633,
    #     "SPD": 961896,
    #     "FDP": 157451,
    #     "GRÜNE": 348661,
    #     "DIE LINKE": 161488,
    #     "FREIE WÄHLER": 38433
    # }
    anzahl_sitze = input("Bitte geben Sie die Anzahl der Sitze für das Parlament an: ")
    try:
        anzahl_sitze = int(anzahl_sitze)
    except:
        print("Nur ganze Zahlen bitte")

    hlt = Parlament(landesstimmen, anzahl_sitze=anzahl_sitze)
    hlt.bestimme_parlamentsparteien(gesamtstimmenpool)
    hlt.set_direktmandate("CDU", 40)
    hlt.set_direktmandate("SPD", 10)
    hlt.set_direktmandate("GRÜNE", 5)
    hlt.berechne_ueberhangmandate()

    for k, v in hlt.parteien.items():
        print(v)
    print("5%-Hürde liegt bei {:,} Stimmen.\nAnzahl \"Vorkomma\"-Sitze: {}\tAnzahl anhand der Nachkommastellen zu verteilende Sitze: {}".format(hlt.fuenf_prozent_huerde(), hlt.vergebene_sitze_nach_voller_zahl(),\
         hlt.zu_verteilende_nachkommasitze()).replace(",", "."))
    
    ue = Ueberhang()
    ns = ue.neue_sitzanzahl(hlt)
    print(ns)
    neuHLT = Parlament(landesstimmen, ns)
    neuHLT.bestimme_parlamentsparteien(gesamtstimmenpool)
    neuHLT.set_direktmandate("CDU", 40)
    neuHLT.set_direktmandate("SPD", 10)
    neuHLT.set_direktmandate("GRÜNE", 5)
    neuHLT.berechne_ueberhangmandate()

    for k, v in neuHLT.parteien.items():
        print(v)
    print("5%-Hürde liegt bei {:,} Stimmen.\nAnzahl \"Vorkomma\"-Sitze: {}\tAnzahl anhand der Nachkommastellen zu verteilende Sitze: {}".format(hlt.fuenf_prozent_huerde(), hlt.vergebene_sitze_nach_voller_zahl(),\
         hlt.zu_verteilende_nachkommasitze()).replace(",", "."))

if __name__ == "__main__": main()                