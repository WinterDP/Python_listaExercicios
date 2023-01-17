'''
Desafio 007
Faça um programa que leia um valor em metros 
e o exiba em kilometros, decametros, centimetros 
e milimetros 

'''

metros = float(input('digite um valor em metros '))
kilometros = metros/10**3
decametros = metros/10**1
centimetros = metros*10**2
milimetros = metros*10**3

print('para o valor em metros = {} temos'.format(metros))
print('kilometros = {} km'.format(kilometros))
print('decametros = {} dah'.format(decametros))
print('centimetros = {}'.format(centimetros))
print('milimetros = {}'.format(milimetros))