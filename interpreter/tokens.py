from dataclasses import dataclass
from enum import Enum


class TokenType(Enum):
    CHARACTER = 0
    DISJUNCTION = 1
    CONJUNCTION = 2
    NEGATION = 3
    EXCLUSIVE_OR = 4
    IMPLICATION = 5
    BI_CONDITIONAL = 6
    FOR_ALL = 6
    EXISTS = 7
    LPAREN = 8
    RPAREN = 9
    EQUIVALENT = 10


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value is not None else '')
