import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data_all = pd.read_csv("MRI_and_CDRinfo_Values_X_train.csv")
for col in data_all.columns:
    print(col)
data_all2=pd.read_csv("DR_Values_y_train.csv")
son=pd.concat([data_all["HIPPOVOL"],data_all2["CDRGLOB"]],axis=1)
print(son)
print(son.groupby("HIPPOVOL")("CDRGLOB").mean())
print(son.groupby('HIPPOVOL')('CDRGLOB').std())
son.groupby('CDRGLOB').agg({
    'HIP_VOL': ['mean','std']
}).plot(kind='bar')