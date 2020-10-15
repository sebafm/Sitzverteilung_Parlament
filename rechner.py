from HareNiemeyer import *


def main():
    landesstimmen = 2881261        
    gesamtstimmenpool = {
        "CDU": 776910,
        "SPD": 570446,
        "GRUENE": 570512,
        "LINKE": 181332,
        "FDP": 215946,
        "AfD": 378692,
        "Graue_Panther": 25352,
        "Oeko_Linx": 32457
    }

    anzahl_sitze = input("Bitte geben Sie die Anzahl der Sitze für das Parlament an: ")
    try:
        anzahl_sitze = int(anzahl_sitze)
    except:
        print("Nur ganze Zahlen bitte")

    neuParlament = Parlament(anzahl_sitze=anzahl_sitze)
    neuParlament.bestimme_parlamentsparteien(landesstimmen, gesamtstimmenpool)
    neuParlament.berechne_gesamtzahl_parlamentsstimmen()
    neuParlament.berechne_quoten_parteien()
    neuParlament.set_direktmandate("CDU", 40)
    neuParlament.set_direktmandate("SPD", 10)
    neuParlament.set_direktmandate("GRUENE", 5)
    neuParlament.berechne_sitze_volle_zahl()
    neuParlament.sitzverteilung_anhand_nachkommastellen()
    neuParlament.berechne_ueberhangmandate()

    print("Anzahl \"Vorkomma\"-Sitze: {}\tAnzahl anhand der Nachkommastellen zu verteilende Sitze: {}".format(neuParlament.berechne_sitze_volle_zahl(),\
         neuParlament.sitzverteilung_anhand_nachkommastellen()))
    for k, v in neuParlament.parteien.items():
        print(v)

if __name__ == "__main__": main()
