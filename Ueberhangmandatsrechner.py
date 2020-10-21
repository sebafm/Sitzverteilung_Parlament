import math

class Ueberhang:
    def ueberhangs_ausgleichmandate(self, parlament=dict()):
        """ """
        bigcount = 0
        key = ""
        for k,v in parlament.parteien.items():
            if bigcount < v.direktmandate - v.quote:
                bigcount = v.direktmandate - v.quote
                key = k
        ns = bigcount * 100 / parlament.parteien[key].quote
        foo = [key, math.floor(ns), math.ceil(ns)]
#        print(foo)
        return foo
