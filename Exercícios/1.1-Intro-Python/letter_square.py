import random

random_number = random.uniform(3, 20)

def letter_square(measure):
    if measure < 1:
        return print("'Test number < 0', Invalid measurement!")
    elif measure == 1:
        return print("'Test number ==1' Enter a larger measurement.")
    else:
        for _ in range(int(measure)):
            print("*" * int(measure))

letter_square(0)
letter_square(1)
letter_square(random_number)
