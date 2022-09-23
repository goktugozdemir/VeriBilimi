import numpy as np
a=np.zeros((6,8))
i=0
c=0
for i in range  (6):
    for c in range (8):
     b=np.random.randint(100)
     while ((b in a) == 1):
      b = np.random.randint(100)
     a[i,c]=b
print(a)
