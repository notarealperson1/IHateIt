


class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Person:
    def set_age(self):
        try:
            a = int(input("Write your real age: "))

            if a < 0:
                print("Error: Age cannot be negative.")
            elif a > 120:
                print("Error: Age is too high.")
            else:
                print("You have been successfully added to our database.")

        except ValueError:
            print("Error: Please enter a valid number for age.")
        except InvalidAgeError as e:

            print(e)

person = Person()
person.set_age()






