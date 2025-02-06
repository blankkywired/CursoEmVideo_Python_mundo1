# Calculadora de descontos:

valor_produto = float(input('Qual é o valor do produto R$: '))
valor_Desconto = int(input('Qual o valor do desconto que deseja acrescentar? R$: '))

# print(f'O valor do produto é {valor_produto}\nApos o desconto de {valor_Desconto}% ficara por:\nR${valor_produto - (valor_produto * valor_Desconto / 100)}')

desconto = valor_produto - ( valor_produto * valor_Desconto / 100)
print(f'O produto no valor de R$: {valor_produto} com desconto de {valor_Desconto} % ficara pelo preço de:\nR${desconto}')
