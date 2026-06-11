"""
PROGRAMA PRINCIPAL

Executa:

1. Análise Léxica
2. Análise Sintática
3. Geração de Código
"""

from lexer import tokenize
from parser import Parser
from codegen import generate

with open("../exemplos/programa.txt", "r") as file:
    source = file.read()

print("\n=== CÓDIGO FONTE ===")
print(source)

tokens = tokenize(source)

print("\n=== TOKENS ===")
for token in tokens:
    print(token)

parser = Parser(tokens)

try:
    parser.parse()
    print("\nAnálise sintática: OK")
except Exception as e:
    print("\nErro:", e)

generated = generate(tokens)

print("\n=== CÓDIGO INTERMEDIÁRIO ===")

for line in generated:
    print(line)
