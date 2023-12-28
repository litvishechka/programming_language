import sys
import exceptions


class Number():
    def get_string_interpretation(self) -> str:
        return str(self.value)


class IntNumber(Number):
    def __init__(self, value: int):
        self.value = value

    def run(self, variables_dict, function_dict):
        return int(self.value)


class FloatNumber(Number):
    def __init__(self, value: float):
        self.value = value

    def run(self, variables_dict, function_dict):
        return float(self.value)


class BinaryOp():
    def __init__(self, left: Number, right: Number):
        self.left = left
        self.right = right
        # print(left.value)


class Sum(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " + " + self.right.get_string_interpretation()

    def run(self, variables_dict, function_dict):
        return self.left.run(variables_dict, function_dict) + self.right.run(variables_dict, function_dict)


class Sub(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " - " + self.right.get_string_interpretation()

    def run(self, variables_dict, function_dict):
        return self.left.run(variables_dict, function_dict) - self.right.run(variables_dict, function_dict)


class Mul(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " * " + self.right.get_string_interpretation()

    def run(self, variables_dict, function_dict):
        return self.left.run(variables_dict, function_dict) * self.right.run(variables_dict, function_dict)


class Div(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " / " + self.right.get_string_interpretation()

    def run(self, variables_dict, function_dict):
        return self.left.run(variables_dict, function_dict) / self.right.run(variables_dict, function_dict)


class Less(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " < " + self.right.get_string_interpretation()

    def run(self, variables_dict, function_dict):
        return self.left.run(variables_dict, function_dict) < self.right.run(variables_dict, function_dict)


class More(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " > " + self.right.get_string_interpretation()

    def run(self, variables_dict, function_dict):
        return self.left.run(variables_dict, function_dict) > self.right.run(variables_dict, function_dict)


class EquallyEqually(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " == " + self.right.get_string_interpretation()

    def run(self, variables_dict, function_dict):
        return self.left.run(variables_dict, function_dict) == self.right.run(variables_dict, function_dict)


class NotEqually(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " != " + self.right.get_string_interpretation()

    def run(self, variables_dict, function_dict):
        return self.left.run(variables_dict, function_dict) != self.right.run(variables_dict, function_dict)


class MoreEquall(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " >= " + self.right.get_string_interpretation()

    def run(self, variables_dict, function_dict):
        return self.left.run(variables_dict, function_dict) >= self.right.run(variables_dict, function_dict)


class LessEquall(BinaryOp):
    def get_string_interpretation(self) -> str:
        return self.left.get_string_interpretation() + " <= " + self.right.get_string_interpretation()

    def run(self, variables_dict, function_dict):
        return self.left.run(variables_dict, function_dict) <= self.right.run(variables_dict, function_dict)


class Print():
    def __init__(self, value):
        self.value = value

    def get_string_interpretation(self) -> str:
        return "print(" + self.value.get_string_interpretation() + ")"

    def run(self, variables_dict, function_dict):
        print(self.value.run(variables_dict, function_dict))


class Input():
    def __init__(self, name):
        self.name = name

    def get_string_interpretation(self) -> str:
        return self.name + " = float(input())"

    def run(self, variables_dict, function_dict):
        if not self.name in variables_dict.keys():
            sys.tracebacklimit = -1
            raise exceptions.VariableNotFoundError(self.name)

        input_value = input()
        point = '.'
        if point in input_value:
            if isinstance(variables_dict[self.name], IntNumber):
                sys.tracebacklimit = -1
                raise exceptions.VariableNotFloatError(self.name)
            else:
                variables_dict[self.name] = FloatNumber(float(input_value))
        else:
            if '-' in input_value:
                sys.tracebacklimit = -1
                raise exceptions.NotPositiveValueError(self.name)
            else:
                variables_dict[self.name] = IntNumber(int(input_value))
        return variables_dict[self.name]


class IfStatement():
    def __init__(self, condition, true_statement) -> None:
        self.condition = condition
        self.true_statement = true_statement

    def get_string_interpretation(self) -> str:
        condition = f"if ({self.condition.get_string_interpretation()}):\n\t"
        if_true = '\n\t'.join(
            self.true_statement.get_string_interpretation().split('\n'))
        return condition + if_true

    def run(self, variables_dict, function_dict):
        if self.condition.run(variables_dict, function_dict):
            self.true_statement.run(variables_dict, function_dict)


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

    def run(self, variables_dict, function_dict):
        for statement in self.statements:
            statement.run(variables_dict, function_dict)


class Function():
    def __init__(self, name, code_block: CodeBlock, return_statement) -> None:
        self.name = name
        self.code_block = code_block
        self.return_statement = return_statement

    def get_string_interpretation(self):
        def_name = "def " + self.name + "():\n\t"
        code_block = self.code_block.get_string_interpretation()
        return_string = "\n\treturn " + self.return_statement.get_string_interpretation()

        return def_name + '\n\t'.join(code_block.split('\n')) + return_string

    def run(self, function_dict):
        variables_dict = {}
        self.code_block.run(variables_dict, function_dict)
        return self.return_statement.run(variables_dict, function_dict)


class CallFunction():
    def __init__(self, name):
        self.name = name

    def get_string_interpretation(self):
        def_name = self.name + "()\n"
        return def_name

    def run(self, variables_dict, function_dict):
        if not self.name in function_dict.keys():
            sys.tracebacklimit = 0
            raise exceptions.FunctionNotFoundError(self.name)

        return function_dict[self.name].run(function_dict)


class Program():
    def __init__(self, functions: dict[str, Function]) -> None:
        self.functions: dict[str, Function] = functions

    def add_function(self, function: Function):
        self.functions[function.name] = function

    def get_string_interpretation(self):
        res = []

        for function in self.functions.values():
            res.append(function.get_string_interpretation())

        return '\n\n'.join(res) + "\n\nглавная()"

    def run(self):
        # print(f"\n -- - Run program. Functions: {self.functions}")
        main_function = self.functions['главная']
        # print(f"\n -- - Run program. Main_function: {main_function}")
        return main_function.run(self.functions)


class InitializingIdentifier():
    def __init__(self, type, name, value) -> None:
        self.type = type
        self.name = name
        self.value = value

    def get_string_interpretation(self) -> str:
        return f"{self.name} = {self.value.get_string_interpretation()}"

    def run(self, variables_dict, function_dict):
        value = self.value.run(variables_dict, function_dict)
        if self.type == "целое" and value < 0:
            sys.tracebacklimit = -1
            raise exceptions.Not(self.name)
        elif self.type == "целое" and isinstance(value, float):
            sys.tracebacklimit = -1
            raise exceptions.VariableNotFloatError(self.name)

        if isinstance(value, int):
            variables_dict[self.name] = IntNumber(value)
        elif isinstance(value, float):
            variables_dict[self.name] = FloatNumber(value)


class ReinitializingIdentifier():
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value
        # print(f" -- -- Reinitialize variable {self.name} with value {self.value}")

    def get_string_interpretation(self) -> str:
        return f"{self.name} = {self.value.get_string_interpretation()}"

    def run(self, variables_dict, function_dict):
        if not self.name in variables_dict.keys():
            sys.tracebacklimit = -1
            raise exceptions.VariableNotFoundError(self.name)

        old_value = variables_dict[self.name].run(variables_dict, function_dict)
        new_value = self.value.run(variables_dict, function_dict)

        if type(old_value) == int and type(new_value) == float:
            raise exceptions.VariableNotFloatError(self.name)
        
        if isinstance(new_value, int):
            variables_dict[self.name] = IntNumber(new_value)
        elif isinstance(new_value, float):
            variables_dict[self.name] = FloatNumber(new_value)


class UsingIdentifier():
    def __init__(self, name) -> None:
        self.name = name

    def get_string_interpretation(self) -> str:
        return self.name

    def run(self, variables_dict, function_dict):
        if not self.name in variables_dict.keys():
            sys.tracebacklimit = -1
            raise exceptions.VariableNotFoundError(self.name)

        return variables_dict[self.name].run(variables_dict, function_dict)


class WhileStatement():
    def __init__(self, condition, statement) -> None:
        self.condition = condition
        self.statement = statement

    def get_string_interpretation(self) -> str:
        condition = f"while ({self.condition.get_string_interpretation()}):\n\t"
        while_true = '\n\t'.join(
            self.statement.get_string_interpretation().split('\n'))
        return condition + while_true

    def run(self, variables_dict, function_dict):
        while self.condition.run(variables_dict):
            self.statement.run(variables_dict, function_dict)


class Round():
    def __init__(self, value):
        self.value = value

    def get_string_interpretation(self) -> str:
        return 'round(' + self.value + ')'

    def run(self, variables_dict, function_dict):
        round_value = round(float(self.value))
        return round_value
