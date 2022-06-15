class ArgumentsError(Exception):
    pass


def add_values(a, b):
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise ArgumentsError("Provide correct values")
    return a + b


try:
    add_values(5, '6')

except Exception as f:
    print('Unsupported args.', str(f))
