# Aluguel de carro 

quantidade_dias = int(input('Quantos dias o carro esteve sendo alugado?: '))
qtd_Kilometros = float(input('Quantos Kilometros o carro rodou?: '))

#Resultado
 #Valor por dia = RS 60
 #Valor km rodado = R$ 0.15

totalValor = (quantidade_dias * 60) + (qtd_Kilometros * 0.15)
print(f'O valor total a pagar por {quantidade_dias} Dias\n{qtd_Kilometros} Kilometros rodados é de;\nR$ {totalValor:.2f}')

