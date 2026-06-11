"""
ANALISADOR LÉXICO

Responsável por converter o código-fonte em tokens.

Exemplo:

x = 10

gera:

ID(x)
ASSIGN(=)
NUMBER(10)
"""

import re

TOKEN_SPECIFICATION = [
    ('NUMBER', r'\d+'),
    ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('ASSIGN', r'='),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('MULT', r'\*'),
    ('DIV', r'/'),
    ('NEWLINE', r'\n'),
    ('SKIP', r'[ \t]+'),
]

def tokenize(code):
    tokens = []

    token_regex = '|'.join(
        f'(?P<{name}>{regex})'
        for name, regex in TOKEN_SPECIFICATION
    )

    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()

        if kind == 'SKIP':
            continue

        tokens.append((kind, value))

    return tokens
