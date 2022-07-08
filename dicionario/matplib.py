import matplotlib
import matplotlib.pyplot as plt
import  numpy as np

#Comando plot é usado para desenhar os marcadores do gráfico

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16 ])-(x, y)
# plt.show()

#Importando numpy e ja utilizando a abreviação np, pode se usar as listas no plot

# eixoX = np.array([1, 8])
# eixoY = np.array([3, 10])
# plt.plot(eixoX, eixoY)
# plt.show()
#==================
# subplot: Com o comando subplot, pode ser desenhado mais de um gráfico na mesma imagem.
#plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(1, 2, 1)
# plt.plot(x, y)
# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(1, 2, 2)
# plt.plot(x, y)
# plt.show()
#=====================
# Bar: É possível criar gráfico de barra usando o comando bar: plt.bar(x,y)
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x, y)
# plt.show()
#=====================
# pie: comando pie cria uma gráfico de pizza:
# y = [35, 25, 25, 15]
# plt.pie(y)
# plt.show()
#===========
# label: comando label é usado para criar títulos ou legendas para as fatias.
# y = [35, 25, 25, 15]
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# plt.pie(y, labels=mylabels)
# plt.show()
#======================
# explode:  Este comando só é usado para gráficos do tipo pizza.Ele serve para destacar uma porção no gráfico de pizza
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# myexplode = [0.2, 0, 0, 0] #Aqui se define a distancia que irá ser destacada
# plt.pie(y, labels=mylabels, explode=myexplode)
# plt.show()
#======================
# shadow() : Este comando coloca uma sombra no gráfico de pizza
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# myexplode = [0.2, 0, 0, 0]
# plt.pie(y, labels = mylabels, explode = myexplode, shadow = True) # Ele deve ser colocado junto ao comando que cria o gráfico e junto a ele deve se escrever "True"
# plt.show()
#==================
# plt.title() = Este comando coloca um título no gráfico,
# o título deve ser colocado dentro dos parênteses e entre aspas.
#                      "plt.title("Título do gráfico")"
# xlabel() e ylabel: esses comandos são usados para definir
# um título para os eixos x e y.
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.plot(x, y)
# plt.xlabel("Eixo X")
# plt.ylabel("Eixo Y")
# plt.title("Título do gráfico")
# plt.show()
#==================
# plt.suptitle() = Este comando coloca um super título,
# é usado quando deseja mostrar um título mais importante.
# Ex: plt.suptitle("Minha loja")
#plot 1:
plt.suptitle("Minha loja")
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("Vendas")
#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("Encomendas")
plt.show()

#=================

# plt.legend() = Esta função mostra uma legenda sobre o gráfico no gráfico, ela pode ser colocada em um lugar específico do gráfico.A legenda se não for indicada a posição, ela vem como padrão no canto superior esquerdo.

# Ex1

y1 = [2, 3, 4.5]
y2 = [1, 1.5, 5]
plt.subplot(1, 1, 1)
plt.plot(y1)
plt.plot(y2)
plt.legend(["Azul", "Laranja"], loc="lower right") # Aqui com o "loc" voce define em qual lugar a legenda deve aparecer
plt.show()

# Ex2 apenas uma leganda
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.legend(['Legenda'])
plt.show()
#===========
# plt.figure(figsize=()) : Esse comando aumenta ou diminui o dashbord que o gráfico é mostrado
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.figure(figsize=(20, 20)) # Se difine o eixo x e o eixo y dentro dos parenteses
plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.legend(['Legenda'])
plt.show()
#===========
# Color = É o comando usado para dar cor a algo, pode ser usado em praticamente todos os outros comandos.A cor  deve ser digitada entre aspas e em inglês.
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y, color="red")
plt.show()
#===========
# plt.brah(x, y) : Este comando deita as barras do gráfico de barras
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x,y)
plt.show()
#===========
# Size = Altera o tamanho do texto, ele deve ser usado junto a algum comando que indica um texto.
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.xlabel("Eixo X",size=15, color="blue")
plt.ylabel("Eixo Y")
plt.show()
#===========
# plt.grid() = O comando que colocará grades no gráfico, facilitando a visualização.Você pode alterar a linha.

# Ex1:
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 1, 1)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()

# Ex2: colorindo o grid
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 1, 1)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)

plt.grid(color = 'red', linestyle = '--', linewidth = 0.5)

plt.show()
#==========
# Ex1: grid no eixo x
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.subplot(1, 1, 1)
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.plot(x, y)
#
# plt.grid(axis = 'x')
#
# plt.show()

# Ex2: grid no eixo y
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.subplot(1, 1, 1)
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.plot(x, y)
#
# plt.grid(axis = 'y')
#
# plt.show()

#===========
# plt.box(True) : Este comando coloca o gráfico dentro de uma caixinha, assim deixando o gráfico mais bonito
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.subplot(1, 1, 1)
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
#
# plt.box(True) # Se usa o "True" para colocalo
# # plt.box(False)
#
# plt.plot(x, y)
# # plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
# plt.show()

