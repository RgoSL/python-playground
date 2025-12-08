"""
CONCEITOS CHAVE : 

- O Python Tem Sensibilidade de Variáveis
- A Indentação é Muito Importante Para a Compilação do Código
- O Compilador Interpreta o Tipo da Variável Sozinho 
- O Python Tem Uma Lógica de Precedência Durante a Compilação (Parênteses, Aritméticos, Comparadores, Operadores Lógicos)
- Existe um Tipo de Operador Pouco Explorado em Cursos, o Operador de Atribuição Composto (+=, -=, *=, /=, %=)

"""

# Uso do Operador Aritmético de Exponenciação ->

# Variáveis Int
num1 = 5 
num2 = 2
# Variável Recebendo o Operador
Conta = 5 ** 2
print(Conta) # Resultado Deve Ser 25

# Uso do Operador de Atribuição Composto Aplicando o Operador Módulo ->

X = 5 # Variável Int
X %= 2 # Variável Sofre a Aplicação do Módulo(%)
print(X) # X Passa a Valer 1, Porque o Resto da Divisão de 5/2 é 1