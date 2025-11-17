# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

valor_soma1 = int(input("Digite valor 1: "))
valor_soma2 = int(input("Digite valor 2: "))

print(f"A soma dos valores é {valor_soma1 + valor_soma2}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

valor_div = int(input("Insira um valor inteiro: "))
divisor = 5

print(valor_div % divisor)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

valor_mult1 = int(input("Digite o valor 1: "))
valor_mult2 = int(input("Digite o valor 2: "))

print(f"O resultado da multiplicação dos valores é {valor_mult1 * valor_mult2}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

valor_div1 = int(input("Digite o valor 1: "))
valor_div2 = int(input("Digite o valor 2: "))

print(f"O resultado da divisão é {valor_div1 / valor_div2}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

valor_exp = int(input("Digite um valor inteiro: "))

print(f"O resultado do valor ao quadrado é {valor_exp ** 2}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

valor_somafloat1 = float(input("Digite o valor 1 com casas decimais: "))
valor_somafloat2 = float(input("Digite o valor 2 com casas decimais: "))

print(f"O resultado da soma dos valores é {valor_somafloat1 + valor_somafloat2}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

import statistics
valor_medfloat1 = float(input("Digite o valor 1 com casas decimais: "))
valor_medfloat2 = float(input("Digite o valor 2 com casas decimais: "))

print(f"O resultado da média dos valores é {statistics.mean([valor_medfloat1, valor_medfloat2])}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

valor_pot1 = int(input("Digite valor base: "))
valor_pot2 = int(input("Digite valor expoente: "))

print(f"O valor da potenciação é {valor_pot1 ** valor_pot2}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

valor_celsius = int(input("Digite a temperatura em ºC: "))

# equação de conversão C > F  
#   F = (C * 9/5) + 32

valor_fahrenheit = (valor_celsius * 9/5) + 32

print(f"A temperatura convertida em Fahrenheint é {valor_fahrenheit}ºF")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

import math
raio = float(input("Informe o raio do círculo: "))

# fórmula da área do círculo >> A = pi * r ** 2
area = round(math.pi * raio ** 2,2)

print(f"A área do círculo é {area}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

nome = input("Informe nome e sobrenome: ")
print(str.upper(nome))

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

nome = input("Informe nome completo: ")
print(str.lower(nome))

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, 
#       imprima esta frase sem espaços em branco no início e no final.

texto = input("Escreve uma frase: ")
print(str.strip(texto))

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, 
#       imprima o dia, o mês e o ano separadamente.

datanasc = input("Informe sua data de nascimento (dd/mm/aaaa): ")
print(str.split(datanasc, "/"))

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

datamesnasc = input("Informe a data do mês em que nasceu: ")
mesnasc = input("Informe o mês em que nasceu: ")

print(f"Quem nasce em {datamesnasc} de {mesnasc} é leonino")

# #### Booleanos (`bool`)
# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário 
#       e retorne o resultado da operação AND entre elas.

metadiaria = 10
volvenda = input("Quantas baterias você vendeu hoje: ")
metavenda = input("Qual a meta do diaria?: ")

metavenda < metadiaria and volvenda < 0 = False

print(resultado)
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
