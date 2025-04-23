def decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorator: Before function call")
        result = func(*args, **kwargs)
        print("Decorator: After function call")
        return result
    return wrapper

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


def split_string_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.split()
    return wrapper