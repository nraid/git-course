def validate(func):
    def wrapper(*args, **kwargs):
        values = args + tuple(kwargs.values())
        for value in values:
            if type(value) not in (int, float):
                raise ValueError('Values should be int or float type.')

        return func(*args, **kwargs)
    return wrapper


@validate
def add_values(*args, **kwargs):
    return sum(args + tuple(kwargs.values()))


def sub_values(*args):
    return sum(args)


print(add_values(5, 6, c='dg'))

