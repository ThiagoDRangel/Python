from random import choice

number_choise = [5, 10, 15, 20]
initial_list = []

def calculator():
    number = choice(number_choise)
    for contador in range(number):
       initial_list.append(contador)
    soma = sum(initial_list)
    media = soma / number
    print(initial_list, 'Média', media)
calculator()