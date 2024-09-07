def add_everything_up(a, b):
    try:
        _sum = a + b
    except TypeError:
        _sum = (str(a) + str(b))
        return _sum
    else:
        return round(_sum, 3)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
