'''
Desafio 011
Faça um programa que leia a largura e a altura
de uma parede em metros. Calcule a sua área e 
a quatidade de tinta necessária pra pintá-la

considere que um litro de tinta, pinta uma área
de 2m^2

'''

gastoTinta = 0.5

alturaParede = float(input('digite a altura da parede '))
larguraParede = float(input('digite a largura da parede '))

areaParede = alturaParede*larguraParede

print('A parede de dimensões {} X {} e área {:.3f}m²'.format(larguraParede, alturaParede, areaParede))
print('Portanto, a quantidade de tinta necessária é {:.3f}L'.format(areaParede*gastoTinta))
