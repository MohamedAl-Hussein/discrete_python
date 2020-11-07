from interpreter.lexer import Lexer
from interpreter.parser_ import Parser

while True:
    text = input("statement > ")
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    tree = parser.parse()
    print(tree)
