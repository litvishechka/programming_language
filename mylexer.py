from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Числа
        self.lexer.add('FLOAT_NUMBER', r'[+-]?[0-9]+\.[0-9]+')
        self.lexer.add('NUMBER', r'\d+')
        # Print
        self.lexer.add('PRINT', r'вывести')
        # Скобки
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Точка с запятой
        self.lexer.add('SEMI_COLON', r'\;')
        # Операторы
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'/')
        # Игнорируем пробелы
        self.lexer.ignore('\s+')
 
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()