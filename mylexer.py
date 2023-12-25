from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Числа
        self.lexer.add('FLOAT_NUMBER', r'[-]?[0-9]+\.[0-9]+')
        self.lexer.add('NUMBER', r'\d+')
        # булевые переменные
        # self.lexer.add('BOOLEAN', r'true(?!\w)|false(?!\w)')
        # условие
        self.lexer.add('IF', r'если')
        #цикл
        self.lexer.add('WHILE', r'пока')
        #округлить
        self.lexer.add('ROUND', r'округлить')
        # Тип числа
        self.lexer.add('FLOAT',  r'вещественное')
        self.lexer.add('UNSIGNED_INTEGER',  r'целое')
        # Print
        self.lexer.add('PRINT', r'вывести')
        #ввести
        self.lexer.add('INPUT', r'считать')
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
        self.lexer.add('EQUALLY_EQUALLY', r'==')
        self.lexer.add('NOT_EQUAL', r'!=')
        self.lexer.add('MORE_EQUAL', r'>=')
        self.lexer.add('LESS_EQUAL', r'<=')
        self.lexer.add('MORE', r'>')
        self.lexer.add('LESS', r'<')
        self.lexer.add('EQUALLY', r'=')
        self.lexer.add('OPEN_CURLY_STAPLE', r'{')
        self.lexer.add('CLOSE_CURLY_STAPLE', r'}')
        # Идентификатор
        self.lexer.add('IDENTIFIER', r'\w*[a-zA-Zа-яА-ЯёЁ]+\w*')
        # Игнорируем пробелы
        self.lexer.ignore('\s+')
        self.lexer.ignore('\n+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()