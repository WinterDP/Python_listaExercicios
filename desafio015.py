'''
Desafio 015
Faça um programa que pergunte a quantidade
de Km percorridos por um carro alugado e a 
quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro 
custa R$60,00 por dia e R$0,15 por Km rodado

'''

precoDia = 60
precoKm = 0.15
diasAlugados = float(input('Digite o número de dias alugados '))
KmRodados = float(input('Digite o número de kilometros rodados '))

precoTotal = diasAlugados*precoDia + precoKm*KmRodados

print('O preco do aluguel, para {} dias e {}kms rodados, é de R${:.2f}'.format(diasAlugados, KmRodados, precoTotal))
