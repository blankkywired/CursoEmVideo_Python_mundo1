entradaUsuario = input('Digite alguma coisa:\n>')

print('Qual é o tipo de dado?:' , type(entradaUsuario))
print('O conteudo do usuario so tem espaços?' , entradaUsuario.isspace())
print('O dado é um numero?' , entradaUsuario.isnumeric()) # So contem numeros
print('O dado é alfabetico?' , entradaUsuario.isalpha()) # Alfabetico = So contem letras
print('O dado é alfanumerico?' , entradaUsuario.isalnum())# Alfanumerico = Contem letras E numeros
print('Esta em maisculas?  ', entradaUsuario.isupper())
print('Esta em minusculas?', entradaUsuario.islower())
print('Está capitalizada?' , entradaUsuario.istitle()) #Capitalizada = Começa com letra maiuscula

