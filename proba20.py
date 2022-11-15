def my_decorator(func):
    def wrapper():
        print("Начало выполнения функции.")
        func()
        print("Конец выполнения функции.")

    return wrapper


@my_decorator
def my_first_decorator():
    print("Это мой первый декоратор!")

from decorators import do_twice

@do_twice
def test_twice():
    print("Это вызов функции test_twice!")