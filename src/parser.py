
"""
ANALISADOR SINTÁTICO

Verifica se o programa possui a estrutura:

ID = NUMBER

ou

ID = ID + NUMBER
"""

class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self, token_type):
        token = self.current()

        if token and token[0] == token_type:
            self.pos += 1
            return token

        raise SyntaxError(
            f"Esperado {token_type}, encontrado {token}"
        )

    def parse_assignment(self):
        self.eat('ID')
        self.eat('ASSIGN')

        token = self.current()

        if token[0] in ('NUMBER', 'ID'):
            self.pos += 1
        else:
            raise SyntaxError("Valor inválido")

        if self.current() and self.current()[0] == 'PLUS':
            self.eat('PLUS')

            token = self.current()

            if token[0] in ('NUMBER', 'ID'):
                self.pos += 1
            else:
                raise SyntaxError("Operando inválido")

        return True

    def parse(self):
        while self.current():
            self.parse_assignment()

            if self.current() and self.current()[0] == 'NEWLINE':
                self.eat('NEWLINE')

        return True
