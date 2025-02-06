#Pintando uma parede

largura_parede = float(input('LARGURA: '))
altura_parede = float(input('ALTURA: '))

areaTotal_parede = largura_parede * altura_parede


# 1 litro de tinta = pinta 2m quadrados 
# Quantidade Litros de tinta necessarios = (AreaTotal / 2)
print(f'Sua parede {largura_parede} x {altura_parede } tem dimensao de {areaTotal_parede} metros quadrados')
print(f'Para pintar essa parede sera necessario {(areaTotal_parede / 2):.2f} Litros de Tinta ')

