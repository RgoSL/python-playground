# Exercícios Para Fixar a Recapitulação Das Bases do Python (Váriaveis, Condicionais e Loops)

"""
Exercício 1 — Contador de Pares

Enunciado:
Escreva um programa que peça ao usuário um número N e conte quantos números pares existem entre 1 e N (inclusive).
Use um loop for.


Exercício 2 — Adivinhe o Número

Enunciado:
Escreva um programa que gera internamente um número entre 1 e 10 e pede que o usuário tente adivinhar.
Use um loop while que só encerra quando o usuário acertar.
Se o palpite for maior ou menor que o número escondido, informe isso.


Exercício 3 — Soma Acumulada

Enunciado:
Peça ao usuário vários números e vá somando todos eles até que o usuário digite 0.
Quando o 0 for digitado, mostre a soma final.
Use um loop while.

"""


# Exercício 01 (Mostrando os Números Encontrados)

# Input Para Receber o Número do Usuário
NumeroN = int(input("Digite um Valor Qualquer :")) # Conversão do Input Para Int, Por Padrão Ele é String

# Loop For Para Analisar os Números Dentro do Escopo Solicitado
for Num in range(1, NumeroN + 1): # Adição do Operador de Atribuição Para o Número do Usuário Ser Considerado
    if Num % 2 == 0: # Validação de Números Pares
        print(Num)


# Exercício 01 (Mostrando QUANTOS Números Foram Encontrados)

# Variável Crucial Para a Diferenciação da Resolução 
Encontrados = 0

# Input Para Receber o Número do Usuário
NumeroN = int(input("Digite um Valor Qualquer :")) # Conversão do Input Para Int, Por Padrão Ele é String

# Loop For Para Analisar os Números Dentro do Escopo Solicitado
for Num in range(1, NumeroN + 1): # Adição do Operador de Atribuição Para o Número do Usuário Ser Considerado
    if Num % 2 == 0: # Validação de Números Pares
        Encontrados += 1 # Adiciona Mais 1 Sempre que um Par For Encontrado
print(Encontrados) # Agora Exibe o Número de Números Pares Encontrados


# Exercício 02

# Import do Módulo do Python Que Gera Números Aleatórios
from random import randint

# Variável Que Recebe o Número Aleatório Entre 1 e 10
Num_Gerado = randint(1,10)

# Input Que Recebe o Chute do Usuário
Palpite = int(input("Adivinhe o Número Gerado :"))

# Laço de Repetição
while Palpite != Num_Gerado: # Condicional do Laço é "Enquanto o Chute For Diferente do Número Gerado Faça:"
    
    # Condicional Para Avisar se o Chute For Maior
    if Palpite < Num_Gerado:
        print("O Número Gerado é Maior do Que Esse!")
        
    # Condicional Para Avisar se o Chute For Menor
    elif Palpite > Num_Gerado:
        print("O Número Gerado é Menor do Que Esse!")

    # Input Adicionado ao Fim do Laço Para os Chutes Continuarem Até o Usuário Acertar
    Palpite = int(input("Adivinhe o Número Gerado :"))

# Mensagem de Êxito ao Sair do Laço
print("Você Acertou!")

# Exercício 03

Soma = 0 # Variável que Recebe o Acúmulo Dos Valores

# Input que Recebe os Valores Utilizados no Acúmulo
User_Nums = int(input("Digite um Valor :"))

# Laço Durável Enquanto o Usuário Não Digitar 0
while User_Nums != 0:
    Soma += User_Nums # Operador de Atribuição Para Acumular os Valores
    User_Nums = int(input("Digite Mais um Valor :")) # Pedido de Mais Números Para Aumentar o Acúmulo
    
# Condicional Para Exibir o Valor Final do Acúmulo
if User_Nums == 0:
    print(Soma)