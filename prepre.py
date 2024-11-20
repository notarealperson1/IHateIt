def ver():
    a = int(input("Write your name: "))
    b = int(input("How old are you? "))

    if b < 18:
        print("LOCKED")
    else:
        print("opened")
ver()









import random

def number():
    number_guess = random.randint(1,10)

    print("try to guessing the number!")

    attempt = 3
    for attempt in range(1, attempt + 1):
        user_guess = int(input(f"atemmpt {attempt}, enter the guessed number:"))

        if user_guess < number_guess:
            print(f"lower and {attempt} attempts left")
        elif user_guess > number_guess:
            print(f"bigger and {attempt} attempts left")
        else:
            print(f"congrats. you guessed the number by {attempt} attempts! the guessed number is:{number_guess}")
    else:
            print("you lose")
number()







def print_numbers():
    first = int(input("from first number: "))
    second = int(input("to second: "))

    for number in range(first, second + 1):
        print(number)

print_numbers()









def invert():
    first = int(input("from first number: "))
    second = int(input("to second: "))

    for number in range(second,first, - 1):
        print(number)

invert()






def factorial():
    n = int(input("factorial from number...: "))
    result = 1

    for i in range(1, n + 1):
        result *= i
    print(f"factorial number {n} = {result}")

factorial()