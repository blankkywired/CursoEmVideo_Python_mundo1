# Reajuste Salarial

salario_funcionario = float(input('salario atual do funcionario R$: '))
aumento_salario = int(input('Valor do aumento %: '))

novoSalario = salario_funcionario + (salario_funcionario * aumento_salario / 100)
print(f'O salario do funcionario é R$:{salario_funcionario}\nApos o aumento de {aumento_salario}% será de: R${novoSalario}')