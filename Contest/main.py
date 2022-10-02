import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_excel("data.xlsx")
data["Test"] = (((20-data["NACCMMSE"])/20) * (data["RENTM"]+data["NACCFAM"]/2+(data["ANYMEDS"]/2)+(data["SEX"]/2)) + (data["INDEPEND"]))+1.5
print(data.corr()["CDRGLOB"])
print(data.groupby('CDRGLOB')[['Test']].mean())


x = data ["Test"]
y = data["NACCMMSE"]
labels = data["CDRGLOB"]
plt.scatter(x, y, s=10, cmap = "viridis", c=labels, alpha=0.5)
plt.xlabel("Skor")
plt.ylabel("NACCMMSE")
plt.colorbar()
plt.show()



x = data ["CDRGLOB"]
y = data["Test"]
labels = data["CDRGLOB"]
plt.scatter(x, y, s=10, cmap = "viridis", c=labels, alpha=0.5)
plt.xlabel("CDRGLOB")
plt.ylabel("Skor")
plt.colorbar()
plt.show()



x = data ["INDEPEND"]
y = data["Test"]
labels = data["CDRGLOB"]
plt.scatter(x, y, s=10, cmap = "viridis", c=labels, alpha=0.5)
plt.xlabel("INDEPEND")
plt.ylabel("Skor")
plt.colorbar()
plt.show()
