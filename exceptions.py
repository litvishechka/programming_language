class RichException(Exception):
    pass


class SyntaxError(Exception):
    def __init__(self, lineno):
        self.lineno = lineno

    def __str__(self):
        return f"\n\tError on line: {self.lineno}"


class FunctionNotFoundError(Exception):
    def __init__(self, function_name) -> None:
        self.function_name = function_name

    def __str__(self) -> str:
        return f"\n\tFunction \"{self.function_name}\" was not declared in the program."


class VariableNotFoundError(Exception):
    def __init__(self, variable_name) -> None:
        self.variable_name = variable_name

    def __str__(self) -> str:
        return f"\n\tVariable \"{self.variable_name}\" was not declared in the program."
    

class VariableNotPositiveError(Exception):
    def __init__(self, variable_name) -> None:
        self.variable_name = variable_name

    def __str__(self) -> str:
        return f"\n\tThe variable \"{self.variable_name}\" must not be negative."
    

class VariableNotFloatError(Exception):
    def __init__(self, variable_name) -> None:
        self.variable_name = variable_name

    def __str__(self) -> str:
        return f"\n\tThe variable \"{self.variable_name}\" must not contain a point."

