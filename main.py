from mylexer import Lexer
from myparser import Parser

fname = "input.rch"
with open(fname) as f:
    text_input = f.read()
    print(f"Input of file {fname}:\n{text_input}\n")

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
pg = Parser()
pg.create_productions()
parser = pg.get_parser()
res = parser.parse(tokens)
print(f"Result of parser.parse = {res}")
# first_statement_interpretation = res.statements[0].get_string_interpretation()
# print(f"First statement string interpretation: {first_statement_interpretation}")
res.run()
