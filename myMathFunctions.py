def truncate(n, decimals=0):
    """Schneidet ein Float auf die durch decimals angegebene 
    Anzahl an Nachkommastellen ohne Runden ab.
    ==> float"""
    multiplier = 10**decimals
    return int(n* multiplier)/multiplier