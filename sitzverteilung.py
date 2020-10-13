GUELTIGE_STIMMEN = 2881261
ANZAHL_SITZE = 110

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

""" Die Nachkommastellen einer Zahl ohne Auf- oder Abrundung an einer bestimmten Stelle kappen"""
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


"""Aus einem Dictionary mit Parteien und Stimmen für diese Parteien werden
diejenigen heraussortiert, die die Schwelle von 5% der Landesstimmen erreicht haben und
somit in den Landtag einziehen""" 
def parlamentarische_parteien(alle_parteien_stimmen=dict()):
    parl_stimmenpool = dict()
    for k,v in alle_parteien_stimmen.items():
        if v / GUELTIGE_STIMMEN >= 0.05:
            parl_stimmenpool[k] = v
    return  parl_stimmenpool   


"""Berechnet die Gesamtzahl der Stimmen, die auf die Parteien entfallen, 
die die 5%-Hürde genommen haben und in den Landtag einziehen."""
def gesamtstimmen_parlamentsparteien(parlamentarische_parteien=dict()):
    stimmen = int()
    for k, v in parlamentarische_parteien.items():
        stimmen += v
    return stimmen


"""Berechnet die Anzahl der Sitze vor Einbeziehung der Nachkommastellen"""
def sitzverteilung_vor_ueberhang(parlamentsparteien, gesamtstimmzahl):
    verteilte_sitze = 0

    for (k, v) in parlamentsparteien.items():
        verteilung_grob[k] = int(truncate(((v * ANZAHL_SITZE) / parl_stimmzahl), 0))
        nachkommastellen[k] = ((v * ANZAHL_SITZE) / parl_stimmzahl) - verteilung_grob[k]
        verteilte_sitze += verteilung_grob[k]

    unverteilte_sitze = ANZAHL_SITZE - verteilte_sitze
    if unverteilte_sitze > 0:
        pass
    








# parlamentsparteien = parlamentarische_parteien(gesamtstimmenpool)
# stimmen_parlamentsparteien = gesamtstimmen_parlamentsparteien(parlamentsparteien)





# print(stimmen_parlamentsparteien)
# print(parlamentsparteien)


# #print("Folgende Parteien sind im Parlament repräsentiert: {}".format(parlamentsparteien))




# # parl_stimmzahl = 0
# # parl_stimmzahl += v

# # verteilung_110 = dict()
# # verteilte_sitze = 0


# # print("Verteilte Sitze: {}".format(verteilte_sitze))
# # print(verteilung_110)
