'''
Desafio 004
Faça um programa que leia algo pelo teclado 
e mostre na tela o seu tipo primitivo e todas 
as informações possíveis sobre ele

'''

variavel = input('digite algo: ')

print('Tipo: {}'.format(type(variavel)))
print('É numérico: {}'.format(variavel.isnumeric()))
print('É alfabetico: {}'.format(variavel.isalpha()))
print('É alfanumerico: {}'.format(variavel.isalnum()))
print('Está em caixa alta: {}'.format(variavel.isupper()))
print('Está em caixa baixa: {}'.format(variavel.islower()))
print('Está capitalizado: {}'.format(variavel.istitle()))
      