'''
Desafio 012
Faça um programa que leia o preço 
de um produto e mostre seu novo preço
com 5% de desconto

'''

desconto = 0.05
preco = float(input('digite o preço do produto R$'))
print('o preço do produto que vale R${:.2f} com  desconto de {}% vai custar R${:.2f}'.format(preco, desconto*100, preco * ( 1 - desconto )))
