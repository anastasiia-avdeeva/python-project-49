from operator import add, mul, sub
from random import randint


def get_expression() -> list:
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
    return [operand_1, operator_sign, operand_2]


def solve_expression(operand_1: int, operator_sign: str, operand_2: int) -> int:
    operators_dict = {'+': add, '-': sub, '*': mul}
    answer = operators_dict[operator_sign](operand_1, operand_2)
    return answer


def get_rules() -> str:
    return 'What is the result of the expression?'


def get_question_and_answer() -> tuple[str, str]:
    [operand_1, operator_sign, operand_2] = get_expression()
    question = f'{operand_1} {operator_sign} {operand_2}'
    answer = solve_expression(operand_1, operator_sign, operand_2)
    return question, str(answer)
