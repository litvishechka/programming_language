from rply import ParserGenerator
from myast import Number, Sum, Sub, Print, Mul, Div, FloatNumber, IntNumber, Less


f = open("output.rch", "w")
variables_dict = {}
if_list = []


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # Список всех токенов, принятых парсером.
            ['NUMBER', 'FLOAT_NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'MUL', 'DIV', 'EQUALLY', 'IDENTIFIER',
             'UNSIGNED_INTEGER', 'FLOAT', 'EQUALLY_EQUALLY', 'NOT_EQUAL', 'MORE_EQUAL',
             'LESS_EQUAL', 'MORE', 'LESS', 'OPEN_CURLY_STAPLE', 'CLOSE_CURLY_STAPLE',
             'BOOLEAN', 'IF'],

            precedence=[
                # ('left',['NUMBER']),
                ('left', ['UNSIGNED_INTEGER', 'FLOAT']),
                ('left', ['=']),
                ('left', ['IF']),
                ('left', ['EQUALLY_EQUALLY', 'NOT_EQUAL', 'MORE_EQUAL', 'MORE', 'LESS', 'LESS_EQUAL']),
                ('left', ['PLUS', 'MINUS']),
                ('left', ['MUL', 'DIV']),
                # ('left',['FLOAT_NUMBER']),
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
            variables_dict[p[1].value] = IntNumber(p[3].value)
            return IntNumber(p[3].value)

        @self.pg.production('statement : IF expression SEMI_COLON')
        def expression(p):
            #print(p)
            return p[1]
        @self.pg.production('expression : OPEN_PAREN bool_expression CLOSE_PAREN OPEN_CURLY_STAPLE exp CLOSE_CURLY_STAPLE')
        def bool_expression(p):
            #print(p)
            return p[4]
        @self.pg.production('bool_expression : IDENTIFIER LESS NUMBER')
        def bool_expression(p):
            #print(p)
            left = variables_dict.get(p[0].value)
            right = IntNumber(p[2].value)
            if_list.append(Less(left, right).eval())
            #print(if_list)
            return Less(variables_dict.get(p[0].value), IntNumber(p[2].value))
        
        @self.pg.production('exp : PRINT OPEN_PAREN expression CLOSE_PAREN')
        def exp(p):
            if if_list[0] == True:
                # print("+")
                return Print(p[2])

        @self.pg.production('statement : FLOAT IDENTIFIER EQUALLY FLOAT_NUMBER SEMI_COLON')
        def number(p):
            variables_dict[p[1].value] = FloatNumber(p[3].value)
            return FloatNumber(p[3].value)

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
            # print(num)
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
