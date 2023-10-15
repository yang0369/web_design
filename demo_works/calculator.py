# two types of programming

# 1. functional programming
# def calculate(x, y, ops):
#     if ops == "sum":
#         print(x + y)
#
#
# calculate(1, 2, "sum")


# 2. object-oriented programming -> OOP
class Calculator(object):
    def __init__(self, ops):
        print(" below are the available operations: 1. sum, 2. minus ")
        self.ops = ops

    def calculate(self, x, y):
        if self.ops == "sum":
            print(x + y)

    # minus
    # prompt the user how to use the calculator

# Example usage:
# instantiate
calc = Calculator("sum")

# call class method
calc.calculate(1, 2)