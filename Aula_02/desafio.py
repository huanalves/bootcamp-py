## Checando erros e validando exceções das condições

# 1) Solicita ao usuário que digite seu nome

Q1 = "Digite seu nome: "

while True:
    nome = input(Q1)
    
    if  nome.isdigit(): #checa se valor inserido é apenas número ou string contendo número
        print("Nome inserido inválido")
    elif not nome.strip(): #checa se valor inserido não contém carácter
        print("O campo está vazio")
        continue
    else: print(nome)
    break

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

Q2 = "Digite o valor da sua remuneração: "
CONSTANTE_BONUS = 1000

salario = None #variável entra com valor nulo
while salario is None:
    try:
        salario = float(input(Q2))
        print(f"Sua remuneração este mês é de R$ {salario + CONSTANTE_BONUS}, com adição do bônus.") 
    except ValueError:
        print("Erro: Insira um valor válido (ex: 3254, 5614.25).")

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

Q3 = "Digite o valor do seu bônus multiplicador (ex: 1.5, 1.9, 1.1): "
Q4 = "Ditige seu atingimento de meta (%) no mês anterior (ex: 97, 95, 100): "

bonus = None
while bonus is None:
    try:
        multiplicador = float(input(Q3))
        atingimento = int(input(Q4))
        bonus = round(multiplicador * (atingimento / 100), 2)
        print(f"Seu fator bônus este mês é de {bonus}")
        break
    except ValueError:
        print("Erro: Valor do bônus multiplicador é inválido (ex: 1.0, 0.8)")


# 4) Imprima cálculo do KPI para o usuário

print(f"Olá, {nome}! Sua remuneração este mês é composto por: Salário: R${salario} + Bonificação: {CONSTANTE_BONUS} x {bonus}")