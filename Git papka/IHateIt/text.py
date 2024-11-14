
"""
def generator():
    for i in range(1, 7):
        yield i


gen = generator()


print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


print("hello world ")
"""


def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

class MyIterator:
    def __init__(self, n=6):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

    def count_down(self):
        for i in range(self.n, -1, -1):
            yield i

    def multiplier(self, m):
        def multiply(x):
            return x * m
        return multiply


@print_result
def generate_numbers(n):
    my_iter = MyIterator(n)
    return list(my_iter)

@print_result
def generate_countdown(n):
    my_iter = MyIterator(n)
    return list(my_iter.count_down())

@print_result
def use_multiplier(n, m):
    my_iter = MyIterator(n)
    multiply_by_m = my_iter.multiplier(m)
    return [multiply_by_m(i) for i in range(n+1)]


print("Итератор (от 0 до n):")
generate_numbers(6)


print("\nГенератор (от n до 0):")
generate_countdown(6)

print("\nЗамыкание (умножение на m):")
use_multiplier(6, 2)




