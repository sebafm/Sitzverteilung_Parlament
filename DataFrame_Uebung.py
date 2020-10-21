import pandas as pd
from HareNiemeyer import *

data = dict()
for k,v in Parlament.parteien.items():
    data[k] = [v.name, v.stimmzahl. v.quote]

print(pd.DataFrame.from_dict(data))

