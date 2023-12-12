from lexer import Lexer
from parser1 import Parser

#text_input = """
#вывести(4 + 4 - 2);
#"""
fname = "input.rch"
with open(fname) as f:
    text_input = f.read()
    print(text_input)

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()