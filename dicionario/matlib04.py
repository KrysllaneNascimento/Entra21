import matplotlib.pyplot as plt
import numpy as np
x = np.array(["Janeiro", "Fevereiro", "Março"])
y = np.array([3, 8, 1])
plt.barh(x, y, color="red")
plt.title("JonasExProfessor", color='blue')
plt.xlabel("Meses", size=10, color='y')
plt.ylabel("Pessoas", size=10, color='y')
plt.grid(linestyle='-', linewidth=0.5)

plt.show()