from mylexer import Lexer
from myparser import Parser

#text_input = """
#вывести(4 + 4 - 2);
#"""
fname = "input.rch"
with open(fname) as f:
    text_input = f.read()
    print(text_input)

lexer = Lexer().get_lexer()
for token in text_input.split('\n'):
    tokens = lexer.lex(token)
    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    parser.parse(tokens).eval()

'''pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()'''