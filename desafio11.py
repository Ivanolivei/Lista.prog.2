x = float(input('Qual a altura da parede ? '))
y = float(input('Qual a largura da parede ? '))
l=(x*y)/3
print(f'A sua parede tem {x}x{y} de dimensão\nA area da parede é de {x*y:.2f}m²\nA quantidade de tinta necessária para pintar a parede é de {(l):.2f}L de tinta\nA quantidade de latas sera de {(l/18):.2f}.')
