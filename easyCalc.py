""" Basic calculator + - * / %"""

import operator

def pyCalc():
    try:
        num1 = int(input("First number: "))
        op = input("What is the operator (=, -, *, /, %): ")
        num2 = int(input("Second Number: "))

        opList = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '%': operator.mod
        }

        if op in opList.keys():
            try:
                print(opList[op](num1, num2))
            except ZeroDivisionError:
                print("\nYou cant divide by zero.")
        else:
            print("\nYou entered the wrong operator( {} ).".format(op))
            print("Try one of these:")
            print("+ - * / %")
    except ValueError:
        print("\nYou can only use numbers.")

pyCalc()