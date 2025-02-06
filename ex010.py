#Conversor de Moedas

dinheroUsuario = float(input('Qual o valor do seu orçamento?: \n'))
cotacao_Do_Dolar = 5.65 # 1 Dolar = 5.65 reais 

print(f'Com R$:{dinheroUsuario} voce consegue comprar U${dinheroUsuario / cotacao_Do_Dolar:.2f} Dolares')