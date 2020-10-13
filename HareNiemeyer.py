""" Die Nachkommastellen einer Zahl ohne Auf- oder Abrundung an einer bestimmten Stelle kappen"""
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


class Landtag:
    def __init__(self, gesamtzahl_stimmen, anzahl_sitze=110):
        self.gesamtzahl_stimmen = gesamtzahl_stimmen
        self.anzahl_sitze = anzahl_sitze

    def hare_niemeyer_vor_nachkomma(self, partei):
        return truncate(partei.stimmzahl * self.anzahl_sitze / self.gesamtzahl_stimmen)
    

class Partei:
    def __init__(self, name, stimmzahl, direktmandate=0, ueberhangmandate=0):
        self.name = name
        self.stimmzahl = stimmzahl
        self.direktmandate = direktmandate
        self.ueberhangmandate = ueberhangmandate

class ParlamentsParteien:
    parteien = list()

    def __init__(self, parteien):
        self.parteien = parteien

    def add_parlamentsPartei(partei, landtag):
        if partei.stimmzahl / landtag.anzahl_sitze >= 0.05:
            self.parteien.append(partei)

    def get_parlamentsParteien():
        return self.parteien


class SitzRechner:
    def __init__(self, partei=Partei, landtag=Landtag):
        self.partei = partei
        self.landtag = landtag
    
    def belegte_sitze_nach_vollen_zahlen(partei):
        return truncate(partei.stimmzahl * self.landtag.anzahl_sitze / self.landtag.gesamtzahl_stimmen)

    def zusatzsitz_nachkommastellen():
        pass


gesamtstimmenpool = {
    "CDU": 776910,
    "SPD": 570446,
    "GRUENE": 570512,
    "LINKE": 181332,
    "FDP": 215946,
    "AfD": 378692,
    "GrauePanther": 59553,
    "OekoeLinx": 29338
}

parlamentsParteien = []
for k,v in gesamtstimmenpool.items():
    parlamentsParteien.append(Partei(k, v))

cdu = Partei("CDU", 776.910, 40)
landtag = Landtag(2693838)
sitzRechner = SitzRechner(cdu, landtag)
sitzRechner.belegte_sitze_nach_vollen_zahlen(cdu)
print(sitzRechner)