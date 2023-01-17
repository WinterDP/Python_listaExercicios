'''
Desafio 014
Faça um programa que leia uma temperatura 
digitada em °C e converta para °F

lembre-se que: T(°F) = T(°C) × 9/5 + 32

'''

temperaturaCelcius = float(input('digite uma temperatura a ser convertida '))
print('A temperatura em Fahrenheit equivalente a temperatura {}°C em Celsius é {}°F'.format(temperaturaCelcius, ( temperaturaCelcius * ( 9 / 5 ) ) + 32))
