import pandas as pd
nüf = {'Bursa': 3056120,'Ankara': 563907,'İstanbul': 15519267,'Antalya': 2511700,'İzmir': 4367251,'Çanakkale':542157,'Denizli':1037208}
alan = {'Bursa': 10813,'Ankara': 25632,'İstanbul': 5461,'Antalya': 20177,'İzmir': 11891,'Çanakkale':9817,'Denizli':12134	}
şehir = pd.DataFrame({'Nüfus': pd.Series(nüf),'Alan': pd.Series(alan)})
print(şehir)