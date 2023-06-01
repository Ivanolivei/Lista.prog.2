import math
ltrslata = 18
prclata = 80.00
ltrsgalao = 3.6
prcgalao = 25.00
parede = float(input("Qual o tamanho da área a ser pintada em metros quadrados? "))
qtdlatas = math.ceil(parede / 6 / ltrslata)  # Arredonda para cima
prclatastotal = qtdlatas * prclata
qtdgaloes = math.ceil(parede / 6 / ltrsgalao)  # Arredonda para cima
prcgalaototal = qtdgaloes * prcgalao
qtdlatasmistura = math.ceil((parede / 6 * 1.1) / ltrslata)  # Considerando 10% de folga e arredonda para cima
qtdgaloesmistura = math.ceil(((parede / 6 * 1.1) - (qtdlatasmistura * ltrslata)) / ltrsgalao)  # Arredonda para cima
prcmisturatotal= (qtdlatasmistura * prclata) + (qtdgaloesmistura * prcgalao)
print(f'Tamanho da área a ser pintada: {parede:.2f} metros quadrados.')
print(f"Situação 1:\nQuantidade de latas necessárias: {qtdlatas} latas.\nPreço total: R$ {prclatastotal:.2f}\n")
print(f"Situação 2:\nQuantidade de galões necessários: {qtdgaloes} galões.\nPreço total: R$ {prcgalaototal:.2f}\n")
print(f"Situação 3:\nQuantidade de latas necessárias: {qtdlatasmistura} latas.\nQuantidade de galões necessários: {qtdgaloesmistura} galões.\nPreço total: R$ {prcmisturatotal:.2f}")