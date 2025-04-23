from decorator import decorator, uppercase_decorator, split_string_decorator
# from decorator import decorator, uppercase_decorator, split_string_decorator


@decorator
def my_function():
    print("Dentro da função!")

my_function()


@uppercase_decorator
def text():
    return "Texto de exemplo"

print(text())

@split_string_decorator
def text2():
    return "Texto de exemplo"

print(text2())