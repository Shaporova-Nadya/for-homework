def curry(func, arity):
    if arity < 0:
        raise ValueError('Арность не может быть меньше нуля')
    def func1(*args):
        if len(args)  == arity:
            return func(*args)
        def func2(*args2):
            return func1 (*(args + args2))
        return func2
    return func1


def uncurry(func, arity):
    if arity < 0:
        raise ValueError('Арность не может быть меньше нуля')

    def uncurried_func(*args):
        if len(args) != arity:
            raise TypeError(f"Ожидается {arity} аргументов, получено {len(args)}.")
        result = func
        for arg in args:
            result = result(arg)
        return result
    return uncurried_func

def sum(a, b, c):
    return a + b + c

sum_curry = curry(sum, 3)
print(sum_curry(1)(2)(3))
sum_uncurry = uncurry(sum_curry, 3)
print(sum_uncurry(1, 2, 3))

try:
    curry(sum, -2)
except ValueError as e:
    print(f"\Ошибка при каррировании: {e}")

try:
    sum_uncurry(1, 2)
except TypeError as e:
    print(f"\Ошибка при раскаррировании: {e}")

def sum_three(a, b, c):
    return a + b + c

def multiply_four(a, b, c, d):
    return a * b * c * d
