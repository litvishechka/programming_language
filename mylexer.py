from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        #Тип числа
        #self.lexer.add('UNSIGNED_INTEGER',  r'целое')
        # Числа
        self.lexer.add('FLOAT_NUMBER', r'[+-]?[0-9]+\.[0-9]+')
        self.lexer.add('NUMBER', r'\d+')
        #Тип числа
        self.lexer.add('UNSIGNED_INTEGER',  r'целое')
        #Идентификатор
        #self.lexer.add('IDENTIFIER',r'\w*[a-zA-Zа-яА-ЯёЁ]+\w*')
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
        self.lexer.add('EQUALLY', r'=')
        #Идентификатор
        self.lexer.add('IDENTIFIER',r'\w*[a-zA-Zа-яА-ЯёЁ]+\w*')
        # Игнорируем пробелы
        self.lexer.ignore('\s+')
 
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()