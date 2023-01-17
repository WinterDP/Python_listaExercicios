'''
Desafio 013
Faça um programa que leia o salario
de um funcionário e mostre seu novo 
salário, com 15% de aumento

'''

aumentoSalario = 0.15
salarioInicial = float(input('Qual o salário do funcionário? R$'))
print('O funcionário que tem o salário igual a R${:.2f} com {}% de aumento terá um salário de R${:.2f}'.format(salarioInicial, aumentoSalario * 100, salarioInicial*(1+aumentoSalario)))
