import random
import operator

"""
A classic game of Freaking Math. 

Input of the game is a lower bound and an upper bound for the random generator, for which it will generate math 
equations within those bounds. 

Enter either 1 (True) or 0 (False) for each displayed equation. A correct answer earns 1 point, while an incorrect 
one stops the game immediately.
"""

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def math_game(start, stop):
    print('== FREAKING MATH CONSOLE == \n Give correct answers to get scores.\n')
    score, correct = 0, True
    while correct:
        # Declare random operator and operands
        op = random.choice(list(ops.keys()))
        operand_1 = random.randint(start, stop)
        operand_2 = random.randint(start, stop)
        # Declare true result of operation, as well as a random result and the display result
        true_res = ops[op](operand_1, operand_2)
        random_res = random.randint(start, stop)
        display_res = random.choice([true_res, random_res])
        # user input and game conditions
        user_ans = int(input(f'{operand_1} {op} {operand_2} = {display_res} \n'
                             f'1 for True, 0 for False: '))
        if (true_res == display_res and user_ans == 1) or (true_res != display_res and user_ans == 0):
            score += 1
            print(f'Score: {score} \n')
        else:
            correct = False
            print(f'Incorrect.\n\n == GAME OVER ==\n Your total score is {score}')


if __name__ == '__main__':
    math_game(-20, 20)

# ----------------------------------------------
# Sample result:

# == FREAKING MATH CONSOLE ==
#  Give correct answers to get scores.
#
# -13 + 5 = -8
# 1 for True, 0 for False: 1
# Score: 1
#
# -5 + -9 = 15 
# 1 for True, 0 for False: 0
# Score: 2
#
# 16 - 18 = -2
# 1 for True, 0 for False: 1
# Score: 3
#
# -1 - 16 = -8
# 1 for True, 0 for False: 1
# Incorrect.
#
#  == GAME OVER ==
#  Your total score is 3
