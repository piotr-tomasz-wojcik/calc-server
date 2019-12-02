class InvalidEquation(Exception):
    pass


def calculate(equation):
    if not isinstance(equation, list):
        try:
            return float(equation)
        except (ValueError, TypeError):
            raise InvalidEquation
    try:
        if len(equation[1]) > 2:
            raise InvalidEquation

        operator = equation[0]
        a = equation[1][0]
        b = equation[1][1]

        if operator == '+':
            return calculate(a) + calculate(b)
        elif operator == '*':
            return calculate(a) * calculate(b)
        elif operator == '/':
            return calculate(a) / calculate(b)
        elif operator == '-':
            return calculate(a) - calculate(b)
        else:
            raise InvalidEquation
    except (IndexError, TypeError, ZeroDivisionError):
        raise InvalidEquation
