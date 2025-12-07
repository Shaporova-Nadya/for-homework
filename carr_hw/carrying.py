def curry(func, arity):
    if arity < 0:
        raise ValueError("Арность не может быть меньше нуля")

    def build_curried_func(collected_args): 
        if len(collected_args) == arity:
            return func(*collected_args)
        else:
            def next_arg_func(arg):
                if len(collected_args) + 1 > arity:  
                    raise TypeError(f"Лишний аргумент: {arg}")
                return build_curried_func(collected_args + (arg,))
            return next_arg_func
    return build_curried_func(tuple())



def uncurry(func, arity):
    if arity < 0:
        raise ValueError("Арность не может быть меньше нуля")

    def uncurried_func(*args):
        if len(args) != arity:
            raise TypeError(f"Ожидается {arity} аргументов, получено {len(args)}.")
        result = func
        for arg in args:
            result = result(arg)
        return result
    return uncurried_func

def sum_three_args(a, b, c): 
    return a + b + c

def multiply_four(a, b, c, d):
    return a * b * c * d
