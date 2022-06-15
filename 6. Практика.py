
class IntFloatError(Exception):
    pass


def validate(func):
    def wrapper(*args, **kwargs):
        values = args + tuple(kwargs.values())
        for value in values:
            if type(value) not in (int, float):
                raise IntFloatError('Input should be int or float type.')

        return func(*args, **kwargs)
    return wrapper


@validate
def multiply(a, b):
    return a * b


# try:
#     abcd = 5.5
#     if abcd not in int:
#         raise IntFloatError
# except IntFloatError:
#     pass
#
