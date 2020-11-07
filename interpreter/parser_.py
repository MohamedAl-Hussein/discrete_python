from interpreter.tokens import TokenType
from interpreter.nodes import *

CONDITIONAL_OPERATORS = [TokenType.BI_CONDITIONAL, TokenType.IMPLICATION]
BINARY_OPERATORS = [TokenType.CONJUNCTION, TokenType.DISJUNCTION, TokenType.EXCLUSIVE_OR]


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.current_token = None
        self.advance()

    def raise_error(self):
        raise Exception("Invalid syntax")

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token is None:
            return None

        result = self.logical_equivalence()

        if self.current_token is not None:
            self.raise_error()

        return result

    def logical_equivalence(self):
        result = self.conditional_expr()

        self.advance()
        result = EquivalenceNode(result, self.conditional_expr())

        return result

    def conditional_expr(self):
        result = self.binary_expr()

        while self.current_token is not None and self.current_token.type in CONDITIONAL_OPERATORS:
            if self.current_token.type == TokenType.BI_CONDITIONAL:
                self.advance()
                result = BiConditionalNode(result, self.binary_expr())
            elif self.current_token.type == TokenType.IMPLICATION:
                self.advance()
                result = ImplicationNode(result, self.binary_expr())

        return result

    def binary_expr(self):
        result = self.factor()

        while self.current_token is not None and self.current_token.type in BINARY_OPERATORS:
            if self.current_token.type == TokenType.CONJUNCTION:
                self.advance()
                result = AndNode(result, self.factor())
            elif self.current_token.type == TokenType.DISJUNCTION:
                self.advance()
                result = OrNode(result, self.factor())
            elif self.current_token.type == TokenType.EXCLUSIVE_OR:
                self.advance()
                result = ExclusiveOrNode(result, self.factor())

        return result

    def factor(self):
        token = self.current_token

        if token.type == TokenType.LPAREN:
            self.advance()
            result = self.conditional_expr()
            if self.current_token.type != TokenType.RPAREN:
                self.raise_error()
            self.advance()
            return result
        elif token.type == TokenType.CHARACTER:
            self.advance()
            return CharacterNode(token.value)
        elif token.type == TokenType.NEGATION:
            self.advance()
            return NegationNode(self.factor())
        elif token.type == TokenType.FOR_ALL:
            self.advance()
            return ForAllNode(self.factor())
        elif token.type == TokenType.EXISTS:
            self.advance()
            return ExistsNode(self.factor())
        else:
            self.raise_error()
