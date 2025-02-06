#Conversor de medidas

valorMetro_usuario = float(input('Uma distancia em metros: \n'))
kilometro = valorMetro_usuario / 1000
hectometro = valorMetro_usuario / 100
decametro = valorMetro_usuario / 10
decimetro = valorMetro_usuario * 10
centimetro = valorMetro_usuario * 100
milimetro = valorMetro_usuario * 1000

#Saida de dados
print(f"O valor em metros é {valorMetro_usuario} metros.\nEm Kilometros é: {kilometro}km.\nEm hectometro é: {hectometro}hm\nEm decametro é: {decametro}dam.\nEm decimetro: {decimetro}dm\nEm centimetro: {centimetro}cm\nEm milimetros: {milimetro}mm")