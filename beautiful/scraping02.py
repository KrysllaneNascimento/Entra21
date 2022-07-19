from bs4 import BeautifulSoup
import requests
from operator import itemgetter
produtos = []
valores = []
geral = []
# for i in range(1):
alvo = 'https://www.kabum.com.br/promocao/MENU_PCGAMER'
resposta = requests.get(alvo)
html = BeautifulSoup(resposta.text, 'html.parser')
    #for produto in html.select('.nameCard'):
    #     produtos.append(produto.text.replace('  ', '').replace('\n', ''))
for valor in html.select('.priceCard'):
    print(valor)
        # valores.append(float(valor.text.replace('.', '').replace(',', '.').replace('R$', '')))
# for i in range(len(produtos)):
#     novo_registro = {'Produto': produtos[i], 'Valor': valores[i]}
#     geral.append(novo_registro)
#
# lista_final = sorted(geral, key=itemgetter('Valor'))
# for i in lista_final:
#    print(i)