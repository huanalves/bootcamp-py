# 1) Solicita ao usuário que digite seu nome

Q1 = "Digite seu nome: "
nome = input(Q1)

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

Q2 = "Digite o valor da sua remuneração: "
salario = float(input(Q2))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

Q3 = "Digite o valor do seu bônus: "
bonus = float(input(Q3))

# 4) Calcule o valor do bônus final

CONSTANTE_BONUS = 1000
valor_bonus = round(CONSTANTE_BONUS + salario * bonus,2)

# 5) Imprima cálculo do KPI para o usuário

valor_total = (salario + valor_bonus)

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

print(f"{nome}, sua remuneração total é de {valor_total}")
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?