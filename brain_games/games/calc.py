from operator import add, mul, sub
from random import randint


def get_expression() -> str:
    operators = ['+', '-', '*']
    random_i = randint(0, len(operators) - 1)
    operator_sign = operators[random_i]
    match operator_sign:
        case '*':
            operand_1 = randint(0, 25)
            operand_2 = randint(0, 10)
        case _:
            operand_1 = randint(0, 50)
            operand_2 = randint(0, 50)
    return f'{operand_1} {operator_sign} {operand_2}'


def solve_expression(question) -> int:
    [operand_1, operator_sign, operand_2] = question.split(' ')
    operators_dict = {'+': add, '-': sub, '*': mul}
    answer = operators_dict[operator_sign](int(operand_1), int(operand_2))
    return answer
