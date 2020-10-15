""" Die Nachkommastellen einer Zahl ohne Auf- oder Abrundung an einer bestimmten Stelle kappen"""
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

#########################################
class Parlament:
    """Speichert alle Parteien, die die 5%-Hürde genommen haben, in einem Dictionary und berechnet deren Sitze, Überhangmandate, etc."""
    def __init__(self, anzahl_sitze=110):
        self.gesamtzahl_stimmen = 0
        self.parteien = dict()
        self.anzahl_sitze = anzahl_sitze

    def bestimme_parlamentsparteien(self, landesstimmen, parteien=dict()):
        """Prüft, ob die Parteien aus einem Dictionary die 5%-Hürde geschafft haben und fügt sie, falls ja, der Klassenvariablen "Parteien" hinzu.
        Das Dictionary muss die Form "parteiname: stimmzahl" haben."""
        for n, p in parteien.items():
            if p / landesstimmen >= 0.05: #landesstimmen muss außerhalb der Klasse bereits bestimmt sein.
                self.parteien[n] = Partei(n, p)   # fügt dem Dictionary einen neuen Eintrag zu

    def berechne_gesamtzahl_parlamentsstimmen(self):
        """Anhand der befüllten Klassenvariablen "Parteien" und der für diese Parteien abgegebenen Stimmen,
        wird die gesamtzahl der Wählerstimmen berechnet, die für die Parlamentsparteien abgegeben wurden.
        Diese Zahl ist wichtig, um die Quote der Parteien im Parlament bestimmen zu können."""
        self.gesamtzahl_stimmen = 0
        for n, p in self.parteien.items():
            self.gesamtzahl_stimmen += p.stimmzahl
    
    def berechne_quoten_parteien(self):
        for n, p in self.parteien.items():
            self.parteien[p.name].quote = p.stimmzahl * self.anzahl_sitze / self.gesamtzahl_stimmen #Quote berechnen
            
    def berechne_sitze_volle_zahl(self):
        for name, partei in self.parteien.items():
            a = int(partei.stimmzahl * self.anzahl_sitze / self.gesamtzahl_stimmen) #Quote berechnen
            self.parteien[partei.name].sitze_volle_zahl = truncate(a) #Anzahl Sitze anhand der vollen Quotenzahl vor dem Komma berechnen

    def set_direktmandate(self, parteiname, direktmandate):
        """Setzt das Attribut "direktmandate" einer Partei innerhalb der Dict-Klassenvariablen "Parteien" """
        self.parteien[parteiname].direktmandate = direktmandate
    
    def sitzverteilung_anhand_nachkommastellen(self):
        """Prüft, welche Parteien innerhalb des "Parteien"-Dictionarys die höchsten Nachkommastellen haben
        und setzt das Attrut "sitze_nachkommastellen" einer Partei auf 1, falls diese einen Sitz zugewiesen bekommt.
        Benötigt als Parameter die Anzahl der Sitze, die es noch zu verteilen gibt."""
        #Berechne Sitze, die anhand Nachkommastellen zu verteilen sind, anhand der Gesamtzahl sowie der Vorkomma-Sitzanzahl.
        
        vergebene_sitze = 0
        for k,v in self.parteien.items():
            vergebene_sitze += int(self.parteien[k].sitze_volle_zahl)
        sitze_verbleibend_fuer_nachkommastellen = self.anzahl_sitze - vergebene_sitze
        a = list()
        for k,v in self.parteien.items():
            a.append(((v.quote - truncate(v.quote)), self.parteien[k].name))
        b = sorted(a, reverse=True)
        for val, key in b[:sitze_verbleibend_fuer_nachkommastellen]:
            self.parteien[key].sitze_nachkommastellen = 1
            #print(self.parteien[key].name, self.parteien[key].sitze_nachkommastellen)

    
    def berechne_ueberhangmandate(self):
        for k,v in self.parteien.items():
            a = int(v.direktmandate - (v.sitze_volle_zahl + v.sitze_nachkommastellen))
            if a > 0:
                self.parteien[k].ueberhangmandate = a
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
        self.sitze_nachkommastellen = truncate(quote)
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


