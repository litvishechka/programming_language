class Number():
    def get_string_interpretation(self) -> str:
        return str(self.value)

    def __init__(self, value):
        self.value = value


class IntNumber(Number):
    def run(self, variables_dict):
        return int(self.value)


class FloatNumber(Number):
    def run(self, variables_dict):
        return float(self.value)


class BinaryOp():
    def __init__(self, left: Number, right: Number):
        self.left = left
        self.right = right
        # print(left.value)


class Sum(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " + " + self.right.get_string_interpretation()

    def run(self, variables_dict):
        return self.left.run(variables_dict) + self.right.run(variables_dict)


class Sub(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " - " + self.right.get_string_interpretation()

    def run(self, variables_dict):
        return self.left.run(variables_dict) - self.right.run(variables_dict)


class Mul(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " * " + self.right.get_string_interpretation()

    def run(self, variables_dict):
        return self.left.run(variables_dict) * self.right.run(variables_dict)


class Div(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " / " + self.right.get_string_interpretation()

    def run(self, variables_dict):
        return self.left.run(variables_dict) / self.right.run(variables_dict)


class Less(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " < " + self.right.get_string_interpretation()

    def run(self, variables_dict):
        return self.left.run(variables_dict) < self.right.run(variables_dict)


class More(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " > " + self.right.get_string_interpretation()

    def run(self, variables_dict):
        return self.left.run(variables_dict) > self.right.run(variables_dict)


class EquallyEqually(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " == " + self.right.get_string_interpretation()

    def run(self, variables_dict):
        return self.left.run(variables_dict) == self.right.run(variables_dict)


class NotEqually(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " != " + self.right.get_string_interpretation()

    def run(self, variables_dict):
        return self.left.run(variables_dict) == self.right.run(variables_dict)


class MoreEquall(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " >= " + self.right.get_string_interpretation()

    def run(self, variables_dict):
        return self.left.run(variables_dict) >= self.right.run(variables_dict)


class LessEquall(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " <= " + self.right.get_string_interpretation()

    def run(self, variables_dict):
        return self.left.run(variables_dict) <= self.right.run(variables_dict)


class Print():
    def __init__(self, value):
        self.value = value

    def get_string_interpretation(self) -> str:
        return "print(" + self.value.get_string_interpretation() + ")"

    def run(self, variables_dict):
        print(self.value.run(variables_dict))


class Input():
    def __init__(self, name):
        self.name = name

    def get_string_interpretation(self) -> str:
        return self.name + " = float(input())"

    def run(self, variables_dict):
        input_value = input()
        point = '.'
        if point in input_value:
           variables_dict[self.name] = FloatNumber(float(input_value))
        else: 
            variables_dict[self.name] = IntNumber(int(input_value))                                           
        return variables_dict[self.name]


class IfStatement():
    def __init__(self, condition, true_statement) -> None:
        self.condition = condition
        self.true_statement = true_statement

    def get_string_interpretation(self) -> str:
        condition = f"if ({self.condition.get_string_interpretation()}):\n\t"
        if_true = '\n\t'.join(self.true_statement.get_string_interpretation().split('\n'))
        return condition + if_true

    def run(self, variables_dict):
        if self.condition.run(variables_dict):
            self.true_statement.run(variables_dict)


class CodeBlock():
    def __init__(self, statements) -> None:
        self.statements = statements

    def add_statement(self, value):
        '''
        Эта функция добавляет новый statement в statements.
        Она просто изменяет внутреннее состояние объекта, но не возвращает его.
        '''
        self.statements.append(value)

    def get_string_interpretation(self):
        list_statements = []
        for statement in self.statements:
            list_statements.append(statement.get_string_interpretation())
        return '\n'.join(list_statements)

    def run(self, variables_dict):
        for statement in self.statements:
            statement.run(variables_dict)


class Program():
    def __init__(self, code_block) -> None:
        self.code_block = code_block

    def get_string_interpretation(self):
        return self.code_block.get_string_interpretation()

    def run(self, variables_dict):
        self.code_block.run(variables_dict)


class InitializingIdentifier():
    def __init__(self, type, name, value) -> None:
        self.type = type
        self.name = name
        self.value = value

    def get_string_interpretation(self) -> str:
        return f"{self.name} = {self.value.get_string_interpretation()}"

    def run(self, variables_dict):
        variables_dict[self.name] = self.value
        return self.value.run(variables_dict)


class ReinitializingIdentifier():
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value
        print(
            f" -- -- Reinitialize variable {self.name} with value {self.value}")

    def get_string_interpretation(self) -> str:
        return f"{self.name} = {self.value.get_string_interpretation()}"

    def run(self, variables_dict):
        variables_dict[self.name] = self.value
        return self.value.run(variables_dict)


class UsingIdentifier():
    def __init__(self, name) -> None:
        self.name = name

    def get_string_interpretation(self) -> str:
        return self.name

    def run(self, variables_dict):
        # return variables_dict[self.name]
        return variables_dict[self.name].run(variables_dict)


class Program():
    def __init__(self, code_block) -> None:
        self.code_block = code_block

    def run(self):
        variables_dict = {}
        return self.code_block.run(variables_dict)

    def get_string_interpretation(self):
        return self.code_block.get_string_interpretation()
    

class WhileStatement():
    def __init__(self, condition, statement) -> None:
        self.condition = condition
        self.statement = statement

    def get_string_interpretation(self) -> str:
        condition = f"while ({self.condition.get_string_interpretation()}):\n\t"
        while_true = '\n\t'.join(self.statement.get_string_interpretation().split('\n'))
        return condition + while_true

    def run(self, variables_dict):
        while self.condition.run(variables_dict):
            self.statement.run(variables_dict)
        # return self.condition.run(variables_dict)