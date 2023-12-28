from rply import ParserGenerator, Token
from rply.token import SourcePosition
from myast import *
import exceptions

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
             'IF', 'INPUT', 'WHILE', 'ROUND', 'FUNCTION', 'RETURN'],

            precedence=[
                ('left', ['FUNCTION']),
                ('left', ['UNSIGNED_INTEGER', 'FLOAT']),
                ('left', ['=']),
                ('left', ['IF', 'WHILE']),
                ('left', ['EQUALLY_EQUALLY', 'NOT_EQUAL',
                 'MORE_EQUAL', 'MORE', 'LESS', 'LESS_EQUAL']),
                ('left', ['PLUS', 'MINUS']),
                ('left', ['MUL', 'DIV']),
                # ('left',['FLOAT_NUMBER']),
            ]
        )

    def create_productions(self):
        @self.pg.production('program : ')
        def empty_program(p) -> CodeBlock:
            return Program({})

        @self.pg.production('program : program function')
        def program(p) -> Program:
            # print(f"\n -- Program level: {p}")
            program_stmt = p[0]
            program_stmt.add_function(p[1])
            return program_stmt

        @self.pg.production('function : FUNCTION IDENTIFIER OPEN_PAREN CLOSE_PAREN OPEN_CURLY_STAPLE code_block RETURN expression SEMI_COLON CLOSE_CURLY_STAPLE SEMI_COLON')
        def function(p) -> Function:
            # print(f"\n -- Function level: {p}")
            return Function(p[1].value, p[5], p[7])

        @self.pg.production('code_block : ')
        def empty_code_block(p) -> CodeBlock:
            return CodeBlock([])

        @self.pg.production('code_block : code_block statement')
        def non_empty_code_block(p) -> CodeBlock:
            # print(f" -- We inside of parser: {p}")
            # print(f"      len of p: {len(p)}")
            # print(f"      len of statements: {len(p[0].statements)}")
            code_block: CodeBlock = p[0]
            statement = p[1]
            code_block.add_statement(statement)
            return code_block

        @self.pg.production('statement : INPUT OPEN_PAREN IDENTIFIER CLOSE_PAREN SEMI_COLON')
        def input_statement(p):
            return Input(p[2].value)

        @self.pg.production('statement : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def print_statement(p):
            return Print(p[2])

        @self.pg.production('statement : UNSIGNED_INTEGER IDENTIFIER EQUALLY expression SEMI_COLON')
        def initial_statement(p):
            return InitializingIdentifier(p[0].value, p[1].value, p[3])

        @self.pg.production('statement : FLOAT IDENTIFIER EQUALLY expression SEMI_COLON')
        def initial_statement(p):
            return InitializingIdentifier(p[0].value, p[1].value, p[3])

        @self.pg.production('statement : IDENTIFIER EQUALLY expression SEMI_COLON')
        def reinitial_statement(p):
            return ReinitializingIdentifier(p[0].value, p[2])

        @self.pg.production('statement : WHILE OPEN_PAREN bool_expression CLOSE_PAREN OPEN_CURLY_STAPLE code_block CLOSE_CURLY_STAPLE SEMI_COLON')
        def while_statement(p):
            condition = p[2]
            statement = p[5]
            return WhileStatement(condition, statement)

        @self.pg.production('statement : IF OPEN_PAREN bool_expression CLOSE_PAREN OPEN_CURLY_STAPLE code_block CLOSE_CURLY_STAPLE SEMI_COLON')
        def if_statement(p):
            condition = p[2]
            true_statement = p[5]
            return IfStatement(condition, true_statement)

        @self.pg.production('bool_expression : expression LESS expression')
        @self.pg.production('bool_expression : expression MORE expression')
        @self.pg.production('bool_expression : expression EQUALLY_EQUALLY expression')
        @self.pg.production('bool_expression : expression NOT_EQUAL expression')
        @self.pg.production('bool_expression : expression MORE_EQUAL expression')
        @self.pg.production('bool_expression : expression LESS_EQUAL expression')
        def bool_expression(p):
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

        @self.pg.production('expression : IDENTIFIER OPEN_PAREN CLOSE_PAREN ')
        def call_function(p):
            return CallFunction(p[0].value)

        @self.pg.production('expression : ROUND OPEN_PAREN FLOAT_NUMBER CLOSE_PAREN')
        def input_expression(p):
            return Round(p[2].value)

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
        def number_expression(p):
            num = p[0]
            if num.gettokentype() == 'NUMBER':
                return IntNumber(p[0].value)
            elif num.gettokentype() == 'FLOAT_NUMBER':
                return FloatNumber(p[0].value)
            elif num.gettokentype() == 'IDENTIFIER':
                return UsingIdentifier(p[0].value)

        @self.pg.error
        def error_handle(token: Token):
            import sys

            sys.tracebacklimit = -1
            # print(f" - Error_type: {type(token)}\n - Error value: {token}")
            source_pos: SourcePosition = token.getsourcepos()
            raise exceptions.SyntaxError(source_pos.lineno)
            # error_message = f"Error on line: {source_pos.lineno} symbol: {source_pos.colno}"
            # raise exceptions.SyntaxError(error_message)

    def get_parser(self):
        return self.pg.build()
