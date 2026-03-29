import math
import random

import prompt

from brain_games.cli import is_prime

TIMES = 2


def brain_even(name: str):

    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < TIMES + 1:
        number = random.randint(1, 100)
        answer = prompt.string(f'Question: {number}\nYour answer: ')
        if number % 2 == 0:
            if answer == 'yes':
                print('Correct!')
            else:
                print('\'no\' is wrong answer ;(. Correct answer was \'yes\'.')
                print(f'Let\'s try again, {name}!')
                break
        else:
            if answer == 'no':
                print('Correct!')
            else:
                print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
                print(f'Let\'s try again, {name}!')
                break
        if i == TIMES:
            print(f'Congratulations, {name}!')
        i += 1


def brain_calc(name: str):
    print('What is the result of the expression?')
    operations = ['+', '-', '*']
    i = 0
    while i < TIMES + 1:
        operation_choice = random.randint(0, 2)
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        print(f'Question: {number1} {operations[operation_choice]} {number2}')
        answer = prompt.string('Your answer: ')
        if operations[operation_choice] == '+':
            truth = number1 + number2
        elif operations[operation_choice] == '-':
            truth = number1 - number2
        else:
            truth = number1 * number2

        if truth == int(answer):
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(.')
            print(f'Correct answer was \'{truth}\'.', end=' ')
            print(f'Let\'s try again, {name}!')
            break

        if i == TIMES:
            print(f'Congratulations, {name}!')
        i += 1


def brain_gcd(name: str):

    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < TIMES + 1:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        answer = prompt.string(f'Question: {number1} {number2}\nYour answer: ')
        truth = math.gcd(number1, number2)
        if truth == int(answer):
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(.')
            print(f'Correct answer was \'{truth}\'.', end=' ')
            print(f'Let\'s try again, {name}!')
            break

        if i == TIMES:
            print(f'Congratulations, {name}!')
        i += 1


def brain_progression(name: str):
    
    print('What number is missing in the progression?')
    i = 0
    while i < TIMES + 1:
        min_number = random.randint(1, 30)
        max_number = random.randint(31, 1000)
        step = random.randint(1, 10)
        progression = list(range(min_number, max_number, step))
        if len(progression) < 10:
            continue 
        else:
            progression = progression[:10]
            progression_str = [str(n) for n in progression]
            changed_index = random.randint(0, len(progression_str) - 1)
            progression_str[changed_index] = '..'
            print(f'Question: {' '.join(progression_str)}')
            answer = prompt.string('Your answer: ')
            truth = progression[changed_index]
            if truth == int(answer):
                print('Correct!')
            else:
                print(f'\'{answer}\' is wrong answer ;(.')
                print(f'Correct answer was \'{truth}\'.', end=' ')
                print(f'Let\'s try again, {name}!')
                break

            if i == TIMES:
                print(f'Congratulations, {name}!')
            i += 1


def brain_prime(name: str):
    
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < TIMES + 1:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        truth = is_prime(number)
        if truth:
            if answer == 'yes':
                print('Correct!')
            else:
                print('\'no\' is wrong answer ;(. Correct answer was \'yes\'.')
                print(f'Let\'s try again, {name}!')
                break
        else:
            if answer == 'yes':
                print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
                print(f'Let\'s try again, {name}!')
                break
            else:
                print('Correct!')

        if i == TIMES:
            print(f'Congratulations, {name}!')
        i += 1