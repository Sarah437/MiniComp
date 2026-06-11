
"""
GERADOR DE CÓDIGO

Traduz instruções da linguagem para um código intermediário.

Exemplo:

x = 10

gera:

LOAD 10
STORE x
"""

def generate(tokens):

    output = []

    i = 0

    while i < len(tokens):

        if tokens[i][0] == 'ID':

            variable = tokens[i][1]

            if i + 2 < len(tokens):

                value = tokens[i + 2][1]

                output.append(f"LOAD {value}")
                output.append(f"STORE {variable}")

        i += 1

    return output
