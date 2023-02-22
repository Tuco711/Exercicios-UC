import numpy as np


temp = np.loadtxt("temperaturas.txt")

# Utilizando o NumPy
"""np.where(temp < 0)"""

idx = 0


while temp[idx] > 0:
    idx +=1

print("O valor é:", temp[idx], "e o indice", idx)
print(temp)
