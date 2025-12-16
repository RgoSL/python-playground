# Exercícios Para Fixar a Recapitulação Das Bases do Python (Listas, Tuplas, Dicionários, Conjuntos)

"""
Exercício 1 — Frequência de Palavras

Enunciado:
Peça ao usuário que digite uma frase.
Crie uma estrutura de dados que armazene cada palavra e quantas vezes ela aparece no texto.
Ao final, exiba a lista de palavras com suas respectivas contagens.


Exercício 2 — Cadastro de Produtos

Enunciado:
Crie um programa que permita cadastrar produtos, cada um com nome, preço e quantidade em estoque.
Use uma estrutura de dados adequada para armazenar vários produtos, mantendo seus atributos organizados.
Depois do cadastro, exiba todos os produtos em formato legível.


Exercício 3 — União e Interseção de Listas

Enunciado:
Peça ao usuário dois conjuntos de números (por exemplo, "números da lista A" e "números da lista B").
Utilize estruturas de dados adequadas para:
- mostrar os números que aparecem em ambas as listas;
- mostrar os números que aparecem em pelo menos uma delas.

"""

# Exercício 2 (Mais Adequado é o Dicionário)

# Entradas Para os Valores do Dicionário
NomeProduto = input("Digite o Nome do Produto :")
PrecoProduto = input("Digite o Preço Unitário :")
Estoque = input("Digite a Quantidade Disponível :")

# Dicionário Dos Produtos, Chaves Fixas e Valores Mutáveis
Produtos = {"Produto": {NomeProduto}, "Preço": {PrecoProduto}, "Em Estoque": {Estoque}}

# Exibição Dos Itens Cadastrados Com o Método Items 
print("Itens Cadastrados no Nosso Programa :")
print(Produtos.items())