'''
Desafio 007
Faça um programa que leia as duas notas de um 
aluno e calcule e mostre a sua média

'''

nota1 = float(input('digite a primeira nota do aluno '))
nota2 = float(input('digite a segunda nota do aluno '))

print('as médias das notas {:.1f} e {:.1f} do aluno é {:.1f}'.format(nota1, nota2, ( ( nota1 + nota2 )/ 2 )))