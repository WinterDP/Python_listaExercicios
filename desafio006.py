'''
Desafio 006
Faça um programa que leia um número e mostre 
o seu dobro, triplo e raiz quadrada

'''

numero = float(input('digite um número inteiro '))
dobro = numero*2
triplo = numero*3
raiz = numero**(1/2)
print('o dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.3f}'.format(numero, dobro, triplo, raiz))