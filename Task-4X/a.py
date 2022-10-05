import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


data = pd.read_excel("data.xlsx")
print(data.describe())


x = data ["INDEPEND"]
y = data["SMOKYRS"]
labels = data["CDRGLOB"]
plt.scatter(x, y, s=20, cmap = "viridis", c=labels, alpha=0.5)
plt.xlabel("Independence Level")
plt.ylabel("Smoking Years")
plt.colorbar()
plt.show()

print(data["SEX"].corr(data["NACCICV"]))
"""" (NACCICV=GRAYVOLl + WHITEVOL + CSFVOLl + WMHVOL)  Cinsiyetler arası beyin boyutu  değiştiği için koralasyon yüksektir."""


rsupfrm = pd.qcut(data["RSUPFRM"], 4)
print(data.pivot_table("SEX", index="NACCICV", columns=rsupfrm,aggfunc="count"))

print(data.pivot_table("INDEPEND", index="CDRGLOB", columns=rsupfrm))

print(data.pivot_table("INDEPEND", index="SMOKYRS", columns=rsupfrm))