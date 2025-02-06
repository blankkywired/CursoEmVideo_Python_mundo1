# Programa que le os comprimentos de dois catetos e que informa o comprimento da hipotenusa
import math  
from math import sqrt
cateto1 = float(input('Informe o comprimento do primeiro cateto: '))
cateto2 = float(input('Informe o comprimento do segundo cateto: '))

hipotenusa = (cateto1 ** 2 ) + (cateto2 ** 2)
comprimento_Hipotenusa = math.sqrt(hipotenusa)
print(f'O comprimento da hipotenusa é : {comprimento_Hipotenusa:.2f}')

