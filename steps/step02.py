import numpy as np


class Variable:
    def __init__(self, data):
        self.data = data


class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output

    def forward(self, in_data):
        raise NotImplementedError()  # 継承して使う前提なので、普通に呼び出された場合はエラーを出す


class Square(Function):
    def forward(self, x):
        return x**2


x = Variable(np.array(10))
f = Square()
y = f(x)
print(type(y))
print(y.data)
