#Leitura de cor em Pillow
#[1] - Tons entre preto e branco(cinza) - 0-false
#[L] - Variação de  tonalidade das cores branco e preto(0-255)
#[RGG] - Junção das cores red,green e blue- Tem valor de intensidade entre 0 a 255
#
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#Converter a imagem para Branco
# im = Image.open("bita.png")
# im = im.convert("1")
# im.show()

# #Descobrir o tamanho da imagem
# im = Image.open("pintadinha.jpg")
# print(im.size)
# x, y = im.size
# im.show()

#Criar uma imagem do zero:
# im = Image.new("RGB", (150, 150), (230, 162, 200))
# im.save('flor.png')
# im.show('gato.png')

#Criar uma imagem dividida em dois
# im = Image.new('RGB', (150, 150), (0, 0, 0))
# x, y = im.size
# for i in range(x):
#     for j in range(y):
#         if i < x // 2:
#             im.putpixel((i, j), (255, 255, 255))
# im2 = ImageDraw.Draw(im)
# im2.ellipse((x//2-50, y//2-50, x//2+50, y//2+50), fill=(0, 0, 255))
# im.show()

#Pegar as cores de uma imagem

# im = Image.open("pintadinha.jpg")
# x , y = im.size
# im.show()
# for i in range(x):
#     for j in range(y):
#         r, g, b = im.getpixel((i, j))
#         print(r, g, b)
#Mudar o tamanho da imagem
#==========

#Escrever nas imagens com cor sólida
# image = Image.open(r'pintadinha.jpg')
# draw = ImageDraw.Draw(image)
# font = ImageFont.truetype(r'C:\Windows\Fonts\ALGER', 20)
# text = 'PAISAGEM'
# draw.text((10, 10), text, font=font, fill=(25, 100, 100))
# image.show()

#EXERCICIO 01
# im = Image.new('RGB', (150, 150), (250, 250, 250))
# x, y = im.size
# for i in range(x):
#     for j in range(y):
#         if i < x // 3:
#             im.putpixel((i, j), (0, 0, 255))
#         if i > x // 3 * 2:
#             im.putpixel((i, j), (255, 0, 0))
# im.show()
#EXERCICIO 02

# im = Image.new('1', (8, 8), True)
# cor = False
# for i in range(8):
#     if cor:
#         cor = False
#     else:
#         cor = True
#     for j in range(8):
#         im.putpixel((i, j), cor)
#         if cor:
#             cor = False
#         else:
#             cor = True
# im = im.resize((200, 200))
# im.show()


im = Image.new("RGB", (500, 500), (255, 255, 255))
joinha = Image.open("joinha.png")
joinha = joinha.resize((150, 150))
tamx , tamy = joinha.size
im.paste(joinha, (180, 180))
im.show()
