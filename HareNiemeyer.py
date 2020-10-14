""" Die Nachkommastellen einer Zahl ohne Auf- oder Abrundung an einer bestimmten Stelle kappen"""
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

#########################################
class Parlament:
    """Speichert alle Parteien, die die 5%-Hürde genommen haben, in einem Dictionary und brechnet deren Sitze, Überhangmandate, etc."""
    def __init__(self, gesamtzahl_stimmen=0, parteien=dict(), anzahl_sitze=110):
        self.gesamtzahl_stimmen = gesamtzahl_stimmen
        self.parteien = parteien
        self.anzahl_sitze = anzahl_sitze

    def fuege_parlamentsPartei_hinzu(self, partei):
        if partei.stimmzahl / landesstimmen >= 0.05:
            self.parteien[partei.name] = partei   
            a = partei.stimmzahl * self.anzahl_sitze / self.gesamtzahl_stimmen
            self.parteien[partei.name].quote = a
            self.parteien[partei.name].sitze_volle_zahl = truncate(a)

    def set_direktmandate(self, parteiname, direktmandate):
        self.parteien[parteiname].direktmandate = direktmandate
    
    def sitzverteilung_nachkommastellen(self, sitze_verbleibend_fuer_nachkommastellen):
        a = list()
        for k,v in self.parteien.items():
            a.append(((v.quote - truncate(v.quote)), self.parteien[k].name))
        b = sorted(a, reverse=True)
        for val, key in b[:sitze_verbleibend_fuer_nachkommastellen]:
            self.parteien[key].sitze_nachkommastellen = 1
            #print(self.parteien[key].name, self.parteien[key].sitze_nachkommastellen)

        
#########################################


class Partei:
    def __init__(self, name, stimmzahl, quote=0, direktmandate=0, ueberhangmandate=0, sitze_volle_zahl=0, \
                nachkommastellen = 0.0, sitze_nachkommastellen=0, ausgleichsmandate=0):
        self.name = name
        self.stimmzahl = stimmzahl
        self.quote = quote
        self.direktmandate = direktmandate
        self.ueberhangmandate = ueberhangmandate
        self.sitze_volle_zahl = sitze_volle_zahl
        self.nachkommastellen = nachkommastellen
        self.sitze_nachkommastellen = sitze_nachkommastellen
        self.ausgleichsmandate = ausgleichsmandate

    def __str__(self):
        return ("Name: {}, \n\tStimmzahl: {}, \n\tQuote: {}, \n\tSitze_volle_Zahl: {}, \n\tSitze_Nachkommastellen: {}, "\
                "\n\tDirektmandate: {}, \n\tÜberhangmandate: {}, \n\tAusgleichsmandate: {}".format(self.name, self.stimmzahl, self.quote, \
                self.sitze_volle_zahl, self.sitze_nachkommastellen, self.direktmandate, self.ueberhangmandate, self.ausgleichsmandate))

###############################################################################################

class Wahl:
    """Beinhaltet alle Eckdaten einer Wahl"""
    def __init__(self, landesstimmen, gesamtstimmenpool=dict()):
        self.landesstimmen = landesstimmen # Anzahl der abgegebenen Stimmen bei der Wahl
        self.gesamtstimmenpool = gesamtstimmenpool


################################################################################################

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

#wahl = Wahl(landesstimmen, gesamtstimmenpool)
parlament = Parlament(2693838)

#Fülle die Parlament-Klasenvariable "parteien" mit denjenigen Parteien, die ins Parlament einziehen
for k,v in gesamtstimmenpool.items():
    parlament.fuege_parlamentsPartei_hinzu(Partei(k, v))
            

parlament.set_direktmandate("CDU", 40)
parlament.set_direktmandate("SPD", 10)
parlament.set_direktmandate("GRUENE", 5)
parlament.sitzverteilung_nachkommastellen(3)
for k,v in parlament.parteien.items():
    print(v)

