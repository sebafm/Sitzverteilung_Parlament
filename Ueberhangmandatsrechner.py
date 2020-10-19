import math

class Ueberhang:
    def neue_sitzanzahl(self, parlament=dict()):
        bigcount = 0
        key = ""
        for k,v in parlament.parteien.items():
            if bigcount < v.direktmandate - v.quote:
                bigcount = v.direktmandate - v.quote
                key = k
        ns = bigcount * 100 / parlament.parteien[key].quote
        return parlament.anzahl_sitze + math.floor(ns)
