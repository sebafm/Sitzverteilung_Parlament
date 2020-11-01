import math
import myMathFunctions

#####################################################################
# Eine beliebige Partei:
#####################################################################
class Partei:

    def __init__(self, name, stimmzahl, direktmandate):
        self.name = name
        self.stimmzahl = stimmzahl
        self.direktmandate = direktmandate
        self.sitze_nach_voller_zahl = 0
        self.sitz_anhand_nachkommastellen = 0
        self.quote = 0
    
    def __str__(self):
        return (f"Name: {self.name}, \n\tStimmzahl: {self.stimmzahl}, \n\tSitze_volle_Zahl: {self.sitze_nach_voller_zahl}, \
            \n\tSitze_Nachkommastellen: {self.sitz_anhand_nachkommastellen}, \n\tDirektmandate: {self.direktmandate}, \n\tQuote im Landtag: {self.quote}")

    def get_sitze_landesliste(self):
        return self.sitze_nach_voller_zahl + self.sitz_anhand_nachkommastellen
    
    def berechne_ueberhangmandate(self):
        if self.direktmandate > self.get_sitze_landesliste():
            return self.direktmandate - self.get_sitze_landesliste()
        else: 
            return 0

######################################################################
# Der Landtag:
######################################################################
class Landtag:
    def __init__(self, landesstimmen: int, sitze=110):
        self.landesstimmen = landesstimmen
        self.sitze = sitze
        self.parteien = []

    def bestimme_parlamentsparteien(self, parteien: list):
        for p in parteien:
            if p[1] / self.landesstimmen > 0.05:
                self.parteien.append(Partei(p[0], p[1], p[2]))
    
    def __berechne_gesamtstimmen_parlamentsparteien(self) -> int:
        ges = 0
        for p in self.parteien:
            ges += p.stimmzahl
        return ges
    
    def berechne_quoten_parteien(self):
        """Weist jeder Partei in parteien die jeweilige Quote 
        (=Stimmen / Gesamtstimmen der Landtagsparteien) zu."""
        for p in range(len(self.parteien)):
             self.parteien[p].quote = self.parteien[p].stimmzahl * self.sitze / self.__berechne_gesamtstimmen_parlamentsparteien()

    def berechne_sitze_volle_zahl(self):
        """Weist jeder Partei in parteien die Anzahl Sitze zu, die der vollen Zahl (also ohne Nachkommastellen)
        ihrer Quote im Landtag entsprechen."""
        for p in range(len(self.parteien)):
            self.parteien[p].sitze_nach_voller_zahl = math.floor(self.parteien[p].quote)

    def berechne_nachkommastellen(self):
        """Weist jeder Partei in parteien ein Attribut mit dem Wert der Nachkommastellen aus quote zu"""
        for i in range(len(self.parteien)):
            nkstell = self.parteien[i].quote - math.floor(self.parteien[i].quote)
            setattr(self.parteien[i], "nachkommastellen", nkstell)

    def _get_nicht_verteilte_restsitze(self) -> int:
        """Berechnet die Anzahl der Sitze, die nach der Sitzzuweisung an 
        die Parteien anhand der vollen Zahlen ihrer jew. Quote unverteilt geblieben sind.
        """
        vergebene_sitze = 0
        for p in self.parteien:
            vergebene_sitze += p.sitze_nach_voller_zahl
        return self.sitze - vergebene_sitze
    
    
    def sort_parteien_by_attr(self, attr: str, reverse=True):
        """Ordnet die Liste 'parteien' anhand des angegebenen Attributes."""
        # if not hasattr(self.parteien[0], attr):
        #     return
        self.parteien.sort(key= lambda x: getattr(x, attr, None), reverse=reverse)
        #print(self.parteien)


    def vergebe_restsitze_anhand_nachkommastellen(self):
        """Verteilt die verbleibenden Sitze (zu_verteilende_nachkommasitze) an die Parteien 
        in parteien mit den höchsten Nachkommastellen."""
        for i in range(self._get_nicht_verteilte_restsitze()):
            self.parteien[i].sitz_anhand_nachkommastellen = 1


    def finde_partei_mit_meisten_ueberhangmandaten(self) -> tuple[str, int, float]:
        biggest_ueberhang = 0
        name = ""
        quote = 0
        for partei in self.parteien:
            ueberhang = partei.direktmandate - partei.quote
            if ueberhang > biggest_ueberhang:
                name, biggest_ueberhang, quote  = partei.name, ueberhang, partei.quote
        return (name, biggest_ueberhang, quote)

    def determine_seats_by_ueberhangmandate(self):
        """Bestimmt die neue Anzahl der Sitze des Landtags, ausgehend von den Ueberhangmandaten
        und den entsprechend den anderen Parteien zustehenden Ausgleichsmandaten."""
        ausschlaggebende_partei = self.finde_partei_mit_meisten_ueberhangmandaten()
        if ausschlaggebende_partei[0] == '':
            return None
        else:
            neue_sitzanzahl = ausschlaggebende_partei[1] * 100 / ausschlaggebende_partei[2]
            min_max_sitzanzahl = [ausschlaggebende_partei[0], math.floor(neue_sitzanzahl) + self.sitze , math.ceil(neue_sitzanzahl) + self.sitze ]
            return min_max_sitzanzahl
#######################################################################
