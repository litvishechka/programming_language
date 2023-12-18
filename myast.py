class Number():
    def __init__(self, value):
        self.value = value


class IntNumber(Number):
    def eval(self):
        return int(self.value)


class FloatNumber(Number):
    def eval(self):
        return float(self.value)


class BinaryOp():
    def __init__(self, left: Number, right: Number):
        self.left = left
        self.right = right
        # print(left.value)


class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " - " + self.right.get_string_interpretation()

    def eval(self):
        return self.left.eval() - self.right.eval()


class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()


class Less(BinaryOp):
    def eval(self):
        return self.left.eval() < self.right.eval()


class More(BinaryOp):
    def eval(self):
        return self.left.eval() > self.right.eval()


class EquallyEqually(BinaryOp):
    def eval(self):
        return self.left.eval() == self.right.eval()


class NotEqually(BinaryOp):
    def eval(self):
        return self.left.eval() == self.right.eval()


class MoreEquall(BinaryOp):
    def eval(self):
        return self.left.eval() >= self.right.eval()


class LessEquall(BinaryOp):
    def eval(self):
        return self.left.eval() <= self.right.eval()


class Print():
    def __init__(self, value):
        self.value = value

    def get_string_interpretation(self) -> str:
        return "print(" + self.value.get_string_interpretation() + ")"

    def eval(self):
        print(self.value.eval())

class IfStatement():
    def __init__(self, condition, true_statement) -> None:
        self.condition = condition
        self.true_statement = true_statement

    def eval(self):
        if self.condition:
            return self.true_statement.eval()


class Statements():
    def __init__(self, statements) -> None:
        self.statements = statements

    def add_statement(self, value):
        '''
        Эта функция добавляет новый statement в statements.
        Она просто изменяет внутреннее состояние объекта, но не возвращает его.
        '''
        self.statements.append(value)

    def get_string_interpretation(self):
        pass

    def eval(self):
        print(f"  Evauate all statements: {self.statements}")
        for statement in self.statements:
            statement.eval()
