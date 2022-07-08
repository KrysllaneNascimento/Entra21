# plt.title() = Este comando coloca um título no gráfico, o título deve ser colocado dentro dos parênteses e entre aspas.
#                      "plt.title("Título do gráfico")"
# xlabel() e ylabel: esses comandos são usados para definir um título para os eixos x e y.
import numpy as np
import matplotlib.pyplot as plt
x = np.array(['Janeiro', 'Fevereiro', 'Março', 'abril'])
y = np.array([10, 20, 30, 40])
plt.plot(x, y)
plt.ylabel("Lucros", color='red')
plt.xlabel("Meses", color='red')
plt.title("Lucros por mês", color="g")
plt.show()