# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array(["Aprendizado Mínimo", "Aprendizado Médio", "Aprendizado Completo"])
# y = np.array([5, 20, 10])
# plt.bar(x, y, color="grey")
# plt.title("Educação para Menores", size=20, color='r')
# plt.xlabel("Aprendizado", size=8, color='g')
# plt.ylabel("Alunos", size=8, color='g')
# plt.grid(linestyle='-', linewidth=0.5)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
x  = np.array(['janeiro' , 'fevereiro', 'março', 'abril', 'maio'])
y1 = np.array([10000,20000,30000,2000,12000])
y2 = np.array([20000,10000,40000,5,8.50])

plt.figure(figsize=(10, 10))
plt.grid(axis ='y')
plt.title('Grafico de lucro por mes das empresas Jonas')
plt.subplot(1, 1, 1)

plt.xlabel('meses',color='r')
plt.ylabel('lucro',color='r')
plt.legend(['empresas Jonas','empresas Reiter'], loc="lower right")

plt.plot(x,y1,y2)
plt.plot(y1)
plt.plot(y2)
plt.show()
