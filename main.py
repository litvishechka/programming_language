from mylexer import Lexer
from myparser import Parser

fname = "input.rch"
with open(fname, encoding='utf-8') as f:
    text_input = f.read()
    print(f"Input of file {fname}:\n{text_input}\n") 

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
pg = Parser()
pg.create_productions()
parser = pg.get_parser()
res = parser.parse(tokens)
print(f"Result of parser.parse = {res}")
res.run()
with  open("output.py", "w", encoding='utf-8') as f:
    f.write(res.get_string_interpretation())
