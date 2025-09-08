'''import mathematics function'''
import Mathematics
from Mathematics import *

''' App logic '''
while True:
    # Options
    print('------------------')
    print('1.Add Number')
    print('2.Subtract Number')
    print('3.Multiply Number')
    print('4.Divide Number')
    print('5.Quit')
    print('------------------')


    ''' User input '''
    user_input = int(input("Enter Option:"))
    if user_input == 5:
        print('YOU PRESS QUIT')
        break
    first_user_input = int(input('Enter First Number: '))
    second_user_input = int(input('Enter Second Number: '))

    # logic
    if user_input == 1:
        add =Mathematics.Add_Func(first_user_input, second_user_input)
        print(f'Result:{first_user_input} + {second_user_input} = {add}')
    elif user_input == 2:
        sub =Mathematics.Subtract_Func(first_user_input, second_user_input)
        print(f'Result:{first_user_input} - {second_user_input} = {sub}')
    elif user_input == 3:
        multi =Mathematics.Multiplication_Func(first_user_input, second_user_input)
        print(f'Result:{first_user_input} * {second_user_input} = {multi}')
    elif user_input == 4:
        divide =Mathematics.Devide_Function(first_user_input, second_user_input)
        print(f'Result:{first_user_input} / {second_user_input} = {divide}')

