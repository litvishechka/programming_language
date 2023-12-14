from rply import ParserGenerator
from myast import Number, Sum, Sub, Print, Mul, Div, FloatNumber, IntNumber


f = open("output.rch", "w")
variables_dict= {}
class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # Список всех токенов, принятых парсером.
            ['NUMBER', 'FLOAT_NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'MUL', 'DIV', 'EQUALLY', 'IDENTIFIER', 'UNSIGNED_INTEGER'],

            precedence=[
            #('left',['NUMBER']),
            ('left', ['UNSIGNED_INTEGER',]), 
            ('left', ['=']), 
            ('left', ['PLUS', 'MINUS']),
            ('left', ['MUL', 'DIV']),
            #('left',['FLOAT_NUMBER']),
            ]
        )


    def parse(self):
        @self.pg.production('program : statement')
        def program(p):
            f.write(str(p))
            return p[0]
        
            
        @self.pg.production('statement : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def statement(p):
            return Print(p[2])
        
        @self.pg.production('statement : UNSIGNED_INTEGER IDENTIFIER EQUALLY NUMBER SEMI_COLON')
        def number(p):
            variables_dict[p[1].value] = p[3].value
            #print(variables_dict)
            print(p[3].value)
            return IntNumber(p[3].value)
        

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                f.write(str(p[0]))
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'MUL':
                return Mul(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)
           

        @self.pg.production('expression : NUMBER')
        @self.pg.production('expression : FLOAT_NUMBER')
        @self.pg.production('expression : IDENTIFIER')
        def number(p):
            num = p[0]
            if num.gettokentype() == 'NUMBER':
                return IntNumber(p[0].value)
            elif num.gettokentype() == 'FLOAT_NUMBER':
                return FloatNumber(p[0].value)
            elif num.gettokentype() == 'IDENTIFIER':
                return variables_dict.get(p[0].value)
        

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()