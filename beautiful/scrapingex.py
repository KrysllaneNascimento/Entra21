from bs4 import BeautifulSoup
import requests
from operator import itemgetter

produtos = []
valores = []
geral = []
for i in range(10):
    alvo = f'https://www.mercadolivre.com.br/ofertas?container_id=MLB779362-1&page={i+1}'
    resposta = requests.get(alvo)
    html = BeautifulSoup(resposta.text, 'html.parser')
    for produto in html.select('.promotion-item__title'):
        produtos.append(produto.text.replace('  ', ''))
    for valor in html.select('.promotion-item__price span'):
        valores.append(float(valor.text.replace('.', '').replace(',', '.').replace('R$', '')))

for i in range(len(produtos)):
    novo_registro = {'Produto': produtos[i], 'Valor': valores[i]}
    geral.append(novo_registro)

lista_final = sorted(geral, key=itemgetter('Valor'))
c = 0
for i in lista_final:
    print(i)
    c += 1
print(c)
