from rply import ParserGenerator
from myast import *


variables_dict = {}
if_list = []
list_tokens = []


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # Список всех токенов, принятых парсером.
            ['NUMBER', 'FLOAT_NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'MUL', 'DIV', 'EQUALLY', 'IDENTIFIER',
             'UNSIGNED_INTEGER', 'FLOAT', 'EQUALLY_EQUALLY', 'NOT_EQUAL', 'MORE_EQUAL',
             'LESS_EQUAL', 'MORE', 'LESS', 'OPEN_CURLY_STAPLE', 'CLOSE_CURLY_STAPLE',
             'IF'],

            precedence=[
                # ('left',['NUMBER']),
                ('left', ['UNSIGNED_INTEGER', 'FLOAT']),
                ('left', ['=']),
                ('left', ['IF']),
                ('left', ['EQUALLY_EQUALLY', 'NOT_EQUAL',
                 'MORE_EQUAL', 'MORE', 'LESS', 'LESS_EQUAL']),
                ('left', ['PLUS', 'MINUS']),
                ('left', ['MUL', 'DIV']),
                # ('left',['FLOAT_NUMBER']),
            ]
        )

    def create_productions(self):
        @self.pg.production('program : ')
        def empty_program(p) -> Program:
            return Program([])

        # @self.pg.production('program : program statement')
        @self.pg.production('program : program statement')
        def non_empty_program(p) -> Program:
            # print(f" -- We inside of parser: {p}")
            # print(f"      len of p: {len(p)}")
            # print(f"      len of statements: {len(p[0].statements)}")
            # f.write(str(p))
            statements: Program = p[0]
            statement = p[1]
            statements.add_statement(statement)
            return statements

        @self.pg.production('statement : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def statement(p):
            # print(Print(p[2]).get_string_interpretation())
            return Print(p[2])

        @self.pg.production('statement : UNSIGNED_INTEGER IDENTIFIER EQUALLY NUMBER SEMI_COLON')
        def number(p):
            variables_dict[p[1].value] = UsingIdentifier(p[0].value, p[1].value, IntNumber(p[3].value))
            print(f" get_string_interpretation for the InitializingIdentifier for int:\n {InitializingIdentifier(p[0].value, p[1].value, IntNumber(p[3].value)).get_string_interpretation()}")
            # InitializingIdentifier(p[0].value, p[1], IntNumber(p[3].value)).get_string_interpretation()
            return InitializingIdentifier(p[0].value, p[1].value, IntNumber(p[3].value))

        @self.pg.production('statement : IF OPEN_PAREN bool_expression CLOSE_PAREN OPEN_CURLY_STAPLE statement CLOSE_CURLY_STAPLE SEMI_COLON')
        def if_statement(p):
            condition = p[2]
            true_statement = p[5]
            # print(f" get_string_interpretation for the IfStatement:\n {IfStatement(p[2], p[5]).get_string_interpretation()}")
            return IfStatement(condition, true_statement)

        @self.pg.production('statement : FLOAT IDENTIFIER EQUALLY FLOAT_NUMBER SEMI_COLON')
        def number(p):
            variables_dict[p[1].value] = UsingIdentifier(p[0].value, p[1].value, FloatNumber(p[3].value))
            # print(f" get_string_interpretation for the InitializingIdentifier for real:\n {InitializingIdentifier(p[0].value, p[1], FloatNumber(p[3].value)).get_string_interpretation()}")
            return InitializingIdentifier(p[0].value, p[1].value, FloatNumber(p[3].value))

        @self.pg.production('bool_expression : expression LESS expression')
        @self.pg.production('bool_expression : expression MORE expression')
        @self.pg.production('bool_expression : expression EQUALLY_EQUALLY expression')
        @self.pg.production('bool_expression : expression NOT_EQUAL expression')
        @self.pg.production('bool_expression : expression MORE_EQUAL expression')
        @self.pg.production('bool_expression : expression LESS_EQUAL expression')
        def condition(p):
            left = p[0]
            right = p[2]
            logical_operator = p[1]
            if logical_operator.gettokentype() == 'LESS':
                return Less(left, right)
            elif logical_operator.gettokentype() == 'MORE':
                return More(left, right)
            elif logical_operator.gettokentype() == 'EQUALLY_EQUALLY':
                return EquallyEqually(left, right)
            elif logical_operator.gettokentype() == 'NOT_EQUAL':
                return NotEqually(left, right)
            elif logical_operator.gettokentype() == 'MORE_EQUAL':
                return MoreEquall(left, right)
            elif logical_operator.gettokentype() == 'LESS_EQUAL':
                return LessEquall(left, right)

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
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
