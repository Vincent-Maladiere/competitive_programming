"""
Given a string s representing a valid expression, implement a basic calculator
to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates
strings as mathematical expressions, such as eval().
"""
# %%

ops = ["+", "-", ")", "("]

def calculate(s, idx=0):

    stack = []
    s = s.replace(" ", "")

    while idx < len(s):

        token = s[idx]
 
        if token.isnumeric():
            if len(stack) == 0 or isinstance(stack[0], str):
                stack.insert(0, int(token))
            else:
                stack[0] = int(f"{stack[0]}{token}")

        elif token in ["+", "-", ")"]:

            if len(stack) == 3:
                y = stack.pop(0)
                op = stack.pop(0)
                op_func = {
                    "+": lambda x, y: x + y,
                    "-": lambda x, y: x - y,
                }[op]
                stack[0] = op_func(stack[0], y)

            if token in ["+", "-"]:
                if len(stack) == 0:
                    stack.insert(0, 0)
                stack.insert(0, token)

            else:
                return stack[0], idx

        elif token == "(":
            x, idx = calculate(s, idx+1)
            stack.insert(0, x)
        
        idx += 1
        
    if len(stack) == 3:
        y = stack.pop(0)
        op = stack.pop(0)
        op_func = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
        }[op]
        stack[0] = op_func(stack[0], y)        

    return int(stack[0])


s = "(1+(4+5+2)-3)+(6+8)"
s = "(11 - (10 + 20))"

calculate(s)

# %%
import pytest

@pytest.mark.parametrize("s, expected", [
    ("((0))", 0),
    ("-1", -1),
    ("(-1)", -1),
    ("(10+20-10+100)", 120),
    ("(11-(10+20))", -19),
    ("(11 - (10 + 20))", -19),
])
def test_suite(s, expected):
    assert calculate(s) == expected