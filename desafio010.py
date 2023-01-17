'''
Desafio 010
Faça um programa que leia quanto dinheiro
uma pessoa tem na carteira e mostre quantos 
dolares ela pode comprar

considere $ 1.00 = R$ 5.108

'''
custoDolar = 5.108
carteira = float(input('Digite o valor de sua carteira '))
print('Com R${:.2f} você pode comprar um total de ${:.2f} dolares'.format(carteira, carteira/custoDolar))
