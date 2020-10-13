""" Die Nachkommastellen einer Zahl ohne Auf- oder Abrundung an einer bestimmten Stelle kappen"""
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


class ParlamentsParteien:
    def __init__(self, parteien=None):
        self.parteien = parteien

    def add_parlamentsPartei(partei, landtag):
        if partei.stimmzahl / landtag.anzahl_sitze >= 0.05:
            self.parteien["partei.name"] = partei

    def get_parlamentsParteien():
        return self.parteien

class Landtag:
    def __init__(self, gesamtzahl_stimmen, parlamentsparteien=ParlamentsParteien, anzahl_sitze=110):
        self.parlamentsparteien = parlamentsparteien
        self.gesamtzahl_stimmen = gesamtzahl_stimmen
        self.anzahl_sitze = anzahl_sitze
    
    def sitzanteil(self, partei):
        return partei.stimmzahl * self.anzahl_sitze / self.gesamtzahl_stimmen
    
    def belegte_sitze_nach_vollen_zahlen(self, partei):
        return truncate(self.sitzanteil(partei))

    def nachkommastellen(self, partei):
        return self.sitzanteil(partei) - self.belegte_sitze_nach_vollen_zahlen(partei)
    
    def sitze_verbleibend_fuer_nachkommastellen():
        pass

    def zuordnung_sitze_nachkommastellen():
        pass


class Partei:
    def __init__(self, name, stimmzahl, direktmandate=0, ueberhangmandate=0, sitze_volle_zahl=0, nachkommastellen = 0.0):
        self.name = name
        self.stimmzahl = stimmzahl
        self.direktmandate = direktmandate
        self.ueberhangmandate = ueberhangmandate
        self.sitze_volle_zahl = sitze_volle_zahl
        self.nachkommastellen = nachkommastellen



gesamtstimmenpool = {
    "CDU": 776910,
    "SPD": 570446,
    "GRUENE": 570512,
    "LINKE": 181332,
    "FDP": 215946,
    "AfD": 378692,
}

parlamentsParteien = []
for k,v in gesamtstimmenpool.items():
    parlamentsParteien.append(Partei(k, v))

# cdu = Partei("CDU", 776910, 40)
# landtag = Landtag(2693838)
# sitzRechner = SitzRechner(landtag)
# for i in range(len(parlamentsParteien)):
#     print(sitzRechner.belegte_sitze_nach_vollen_zahlen(parlamentsParteien[i]))
# for i in range(len(parlamentsParteien)):
#     print(sitzRechner.nachkommastellen(parlamentsParteien[i]))
