# Conversor de Temperatura

#Entrada da temperatura em ceusius
temperatura_c = float(input('Informe a temperatura em graus Ceusius C: '))

#Convertendo a temperatura para Fahrenheint F
fahrenheint = temperatura_c * (9 / 5) + 32
print(f'A temperatura de {temperatura_c} graus Ceusius para fahrenheint é: {fahrenheint} graus F')