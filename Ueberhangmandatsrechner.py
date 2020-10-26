import math

class Ueberhang:
    def get_neue_sitzanzahl_nach_hare_niemeyer(self, parlament=dict()):
        """ """
        bigcount = 0
        key = ""
        for k,v in parlament.parteien.items():
            if bigcount < v.direktmandate - v.quote:
                bigcount = v.direktmandate - v.quote
                key = k
        neue_sitzanzahl = bigcount * 100 / parlament.parteien[key].quote
        min_max_sitzanzahl = [key, math.floor(neue_sitzanzahl), math.ceil(neue_sitzanzahl)]
        return min_max_sitzanzahl