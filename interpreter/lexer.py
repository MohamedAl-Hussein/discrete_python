import re
from interpreter.tokens import Token, TokenType

WHITESPACE = ' \n\t'
CHARACTERS = r"[a-zA-Z]"
SYMBOLS = ['&', '|', '-', '>', '<', '=', '^']


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.current_char = None
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char is not None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif re.search(CHARACTERS, self.current_char):
                yield self.generate_variable()
            elif self.current_char == '~':
                # FIXME: currently breaks when negating a quantifier
                self.advance()
                yield Token(TokenType.NEGATION)
            elif self.current_char in SYMBOLS:
                yield self.generate_symbol()
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            else:
                raise Exception(f"Illegal Character '{self.current_char}'")

    def generate_variable(self):
        variable_str = self.current_char
        self.advance()

        while self.current_char is not None and (re.search(CHARACTERS, self.current_char)):
            variable_str += self.current_char
            self.advance()

        if variable_str == "forall":
            return Token(TokenType.FOR_ALL)
        elif variable_str == "exists":
            return Token(TokenType.EXISTS)

        return Token(TokenType.CHARACTER, variable_str)

    def generate_symbol(self):
        symbol_str = self.current_char
        self.advance()

        while self.current_char is not None and (self.current_char in SYMBOLS):
            symbol_str += self.current_char
            self.advance()

        if symbol_str == "&&":
            return Token(TokenType.CONJUNCTION)
        elif symbol_str == "||":
            return Token(TokenType.DISJUNCTION)
        elif symbol_str == '^':
            return Token(TokenType.EXCLUSIVE_OR)
        elif symbol_str == "-->":
            return Token(TokenType.IMPLICATION)
        elif symbol_str == "<-->":
            return Token(TokenType.BI_CONDITIONAL)
        elif symbol_str == "==":
            return Token(TokenType.EQUIVALENT)
        else:
            raise Exception(f"Illegal Symbol '{symbol_str}'")
