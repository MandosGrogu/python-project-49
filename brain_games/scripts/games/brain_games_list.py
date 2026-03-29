import math
import random

import prompt

times = 2


def brain_even(name: str):

    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < times + 1:
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
        if i == times:
            print(f'Congratulations, {name}!')
        i += 1


def brain_calc(name: str):
    print('What is the result of the expression?')
    operations = ['+', '-', '*']
    i = 0
    while i < times + 1:
        operation_choice = random.randint(0, 2)
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        print(f'Question: {number1} {operations[operation_choice]} {number2}')
        answer = prompt.string('Your answer: ')
        if operations[operation_choice] == '+':
            ground_truth = number1 + number2
        elif operations[operation_choice] == '-':
            ground_truth = number1 - number2
        else:
            ground_truth = number1 * number2

        if ground_truth == int(answer):
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{ground_truth}\'.')
            print(f'Let\'s try again, {name}!')
            break

        if i == times:
            print(f'Congratulations, {name}!')
        i += 1


def brain_gcd(name: str):

    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < times + 1:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        answer = prompt.string(f'Question: {number1} {number2}\nYour answer: ')
        ground_truth = math.gcd(number1, number2)
        if ground_truth == int(answer):
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{ground_truth}\'.')
            print(f'Let\'s try again, {name}!')
            break

        if i == times:
            print(f'Congratulations, {name}!')
        i += 1


def brain_progression(name: str):
    
    print('What number is missing in the progression?')
    i = 0
    while i < times + 1:
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
            ground_truth = progression[changed_index]
            if ground_truth == int(answer):
                print('Correct!')
            else:
                print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{ground_truth}\'.')
                print(f'Let\'s try again, {name}!')
                break

            if i == times:
                print(f'Congratulations, {name}!')
            i += 1