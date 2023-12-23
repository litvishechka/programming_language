class Number():
    def get_string_interpretation(self) -> str:
        return str(self.value)

    def __init__(self, value):
        self.value = value


class IntNumber(Number):
    def run(self):
        return int(self.value)


class FloatNumber(Number):
    def run(self):
        return float(self.value)


class BinaryOp():
    def __init__(self, left: Number, right: Number):
        self.left = left
        self.right = right
        # print(left.value)


class Sum(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " + " + self.right.get_string_interpretation()

    def run(self):
        return self.left.run() + self.right.run()


class Sub(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " - " + self.right.get_string_interpretation()

    def run(self):
        return self.left.run() - self.right.run ()


class Mul(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " * " + self.right.get_string_interpretation()

    def run(self):
        return self.left.run() * self.right.run()


class Div(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " / " + self.right.get_string_interpretation()

    def run(self):
        return self.left.run() / self.right.run()


class Less(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " < " + self.right.get_string_interpretation()

    def run(self):
        return self.left.run() < self.right.run()


class More(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " > " + self.right.get_string_interpretation()

    def run(self):
        return self.left.run() > self.right.run()


class EquallyEqually(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " == " + self.right.get_string_interpretation()

    def run(self):
        return self.left.run() == self.right.run()


class NotEqually(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " != " + self.right.get_string_interpretation()

    def run(self):
        return self.left.run () == self.right.run ()


class MoreEquall(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " >= " + self.right.get_string_interpretation()

    def run(self):
        return self.left.run() >= self.right.run()


class LessEquall(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " <= " + self.right.get_string_interpretation()

    def run(self):
        return self.left.run() <= self.right.run()


class Print():
    def __init__(self, value):
        self.value = value

    def get_string_interpretation(self) -> str:
        return "print(" + self.value.get_string_interpretation() + ")"

    def run(self):
        print(self.value.run())


class IfStatement():
    def get_string_interpretation(self) -> str:
        return "if (" + self.condition.get_string_interpretation() + "):\n\t" + str(self.true_statement.get_string_interpretation())

    def __init__(self, condition, true_statement) -> None:
        self.condition = condition
        self.true_statement = true_statement

    def run(self):
        if self.condition:
            return self.true_statement.run()


class Program():
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

    def run(self):
        # print(f"  Evauate all statements: {self.statements}")
        for statement in self.statements:
            statement.run()


class Identifier():
    def __init__(self, type, name, value) -> None:
        self.type = type
        self.name = name
        self.value = value

    def get_string_interpretation(self) -> str:
        return self.type + ' ' + self.name + ' = ' + str(self.value.run())

    def run(self):
        return self.value.run()
