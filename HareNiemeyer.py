import math

""" Die Nachkommastellen einer Zahl ohne Auf- oder Abrundung an einer bestimmten Stelle kappen"""
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

#########################################
class Parlament:
    """Beschreibt den Landtag einer Legislaturperiode. Speichert alle Parteien, 
    die die 5%-Hürde genommen haben, in einem Dictionary und weist ihnen anhand der
    Gesamtstimmen der Parlamentsparteien die Anzahl der jeweiligen Sitze zu. 
    
    Attribute:
        :anzahl_sitze = int. Gesamtzahl der Sitze in diesem Landtag
        :parteien = dict. Key: Parteiname, Value: Objekt der Klasse Partei
        :landesstimmen = int. Insgesamt bei der Wahl abgegebene Landesstimmen.
            Notwendig für die Berechnung der 5%-Hürde.
        :gesamtstimmen_parlamentsparteien = int. Anzahl der Wählerstimmen, die auf 
            die Landtagsparteien entfallen.
        
    """
    def __init__(self, landesstimmen, anzahl_sitze=110):
        self.gesamtstimmen_parlamentsparteien = 0
        self.parteien = dict()
        self.landesstimmen = landesstimmen
        self.anzahl_sitze = anzahl_sitze

    def bestimme_parlamentsparteien(self, parteien=dict()):
        """Prüft, ob die Parteien aus einem Dictionary die 5%-Hürde geschafft haben und fügt sie, falls ja, der Klassenvariablen "Parteien" hinzu.
        Das Dictionary muss die Form "parteiname: stimmzahl" haben."""
        for n, p in parteien.items():
            if p >= self.fuenf_prozent_huerde():   #landesstimmen muss außerhalb der Klasse bereits bestimmt sein.
                self.parteien[n] = Partei(n, p)   # fügt dem Dictionary einen neuen Eintrag zu
        self.__berechne_gesamtstimmen_parlamentsparteien()
        self.__berechne_quoten_parteien()
        self.__berechne_sitze_volle_zahl()
        self.__berechne_sitze_anhand_nachkommastellen()

    def __berechne_gesamtstimmen_parlamentsparteien(self):
        """Anhand der befüllten Variablen "Parteien" und der für diese Parteien abgegebenen Stimmen,
        wird die gesamtzahl der Wählerstimmen berechnet, die für die Parlamentsparteien abgegeben wurden.
        Diese Zahl ist wichtig, um die Quote der Parteien im Parlament bestimmen zu können."""
        self.gesamtstimmen_parlamentsparteien = 0
        for n, p in self.parteien.items():
            self.gesamtstimmen_parlamentsparteien += p.stimmzahl
    
    def __berechne_quoten_parteien(self):
        for n, p in self.parteien.items():
            self.parteien[p.name].quote = p.stimmzahl * self.anzahl_sitze / self.gesamtstimmen_parlamentsparteien #Quote berechnen
            
    def __berechne_sitze_volle_zahl(self):
        """Verteilt die Parlamentssitze anhand der jeweils erzielten ganzen 
        Prozentzahlen (die "Vorkommazahlen"), setzt das Attribut sitze_volle_zahl
        einer jeden Parlamentspartei und 
        gibt die Summe der so verteilten Sitze zurück."""
        x = 0
        for name, partei in self.parteien.items():
            a = partei.stimmzahl * self.anzahl_sitze / self.gesamtstimmen_parlamentsparteien #Quote berechnen
            self.parteien[partei.name].sitze_volle_zahl = math.floor(a) #Anzahl Sitze anhand der vollen Quotenzahl vor dem Komma berechnen
            x += a

    def __berechne_sitze_anhand_nachkommastellen(self):
        """Prüft, welche Parteien innerhalb des "Parteien"-Dictionarys die höchsten Nachkommastellen haben
        und setzt das Attribut "sitze_nachkommastellen" einer Partei auf 1, falls diese einen Sitz zugewiesen bekommt.
        Berechnet hierfür zunächst die Zahl der nach den "Vorkommazahl"-Verteilung verbliebenen Sitze und gibt diese Zahl zurück."""
        
        #Berechne Sitze, die anhand Nachkommastellen zu verteilen sind, anhand der Gesamtzahl sowie der Vorkomma-Sitzanzahl.
        vergebene_sitze = self.vergebene_sitze_nach_voller_zahl()
        sitze_verbleibend_fuer_nachkommastellen = self.anzahl_sitze - vergebene_sitze
        a = list()
        for k,v in self.parteien.items():
            a.append(((v.quote - math.floor(v.quote)), self.parteien[k].name))
        b = sorted(a, reverse=True)
        for val, key in b[:sitze_verbleibend_fuer_nachkommastellen]:
            self.parteien[key].sitze_nachkommastellen = 1
            #print(self.parteien[key].name, self.parteien[key].sitze_nachkommastellen)
     #   return sitze_verbleibend_fuer_nachkommastellen

    def fuenf_prozent_huerde(self):
        return math.ceil(self.landesstimmen * 0.05)
    
    def vergebene_sitze_nach_voller_zahl(self):
        """Gibt die Anzahl der Sitze an, die anhand der Vorkommastellen der
        jeweiligen Parteienquote insgesamt vergeben wurden."""
        x = 0
        for name, partei in self.parteien.items():
            x += int(partei.stimmzahl * self.anzahl_sitze / self.gesamtstimmen_parlamentsparteien) #Quote berechnen
        return x

    def zu_verteilende_nachkommasitze(self):
        vergebene_sitze = self.vergebene_sitze_nach_voller_zahl()
        sitze_verbleibend_fuer_nachkommastellen = self.anzahl_sitze - vergebene_sitze
        return sitze_verbleibend_fuer_nachkommastellen

    def set_direktmandate(self, parteiname, direktmandate):
        """Setzt das Attribut "direktmandate" einer Parlamentspartei 
        innerhalb der Dict-Variablen "Parteien" auf den angegebenen Wert."""
        self.parteien[parteiname].direktmandate = direktmandate
        
    def set_ueberhangmandate(self):
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
        self.sitze_nachkommastellen = 0
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
