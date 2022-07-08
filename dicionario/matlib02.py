import numpy as np
import matplotlib.pyplot as plt
y = [50, 30, 10, 10]
mylabels = ["TI 50%", "Administração 30%", "Engenharia civil 10%", "Inglês 10%"]
plt.pie(y, labels=mylabels)
plt.show()