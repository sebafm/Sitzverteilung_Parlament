from HareNiemeyer import *
from Ueberhangmandatsrechner import *
import pandas as pd

def make_table(parlament):
    data = dict()
    for k,v in parlament.parteien.items():
        data[k] = [v.stimmzahl, v.quote, v.direktmandate, v.sitze_volle_zahl, v.sitze_nachkommastellen, v.ausgleichsmandate]
    return pd.DataFrame.from_dict(data, orient="index", columns = ["Stimmzahl", "Quote im Landtag", "Direktmandate", "Sitze volle Zahl", "Sitze Nachkommastellen", "Ausgleichsmandate"])

def berechne_ueberhang(parlament):
    ue = Ueberhang()
    i = 1
    while i < 3:
        ns = parlament.anzahl_sitze + ue.ueberhangs_ausgleichmandate(parlament)[i]
        print(ns)
        i += 1

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
    hlt.set_ueberhangmandate()

    for k, v in hlt.parteien.items():
        print(v)
    print("5%-Hürde liegt bei {:,} Stimmen.\nAnzahl \"Vorkomma\"-Sitze: {}\tAnzahl anhand der Nachkommastellen zu verteilende Sitze: {}".format(hlt.fuenf_prozent_huerde(), hlt.vergebene_sitze_nach_voller_zahl(),\
         hlt.zu_verteilende_nachkommasitze()).replace(",", "."))
    

    print("berechne_ueberhang():")
    berechne_ueberhang(hlt)
   
    print("Parlament ohne Überhangmandate:")
    print(make_table(hlt))


if __name__ == "__main__": main()                