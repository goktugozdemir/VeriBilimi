
import pandas as pd
data = pd.read_csv("heights.csv")
height = np.array(data["height(cm)"])
son1 = np.where((data["height(cm)"]==height.min()))
son2 = np.where((data["height(cm)"]==height.max()))
in1=son1[0]
in2=son2[0]
print(data["name"][in1])
print(data["order"][in1])
print()
print(data["name"][in2])
print(data["order"][in2])

