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


class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())
