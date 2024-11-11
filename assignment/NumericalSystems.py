def valid_int(prompt: str, min_value=2, max_value=16):
    while True:
        str_value = input(prompt)
        if not str_value.isdigit():
            print('please enter a numeral value! ')
            continue
        int_value = int(str_value)
        if max_value <= int_value <= min_value:
            print('your base must be in diapason 2-16!')
            continue
        return int_value


def to_decimal(input_value, base):
    result = 0
    rank = 0
    for digit in input_value[::-1]:
        result += '0123456789ABCDEF'.index(digit) * (base ** rank)
        rank += 1
    return result


def decimal_to_any_base(input_value, base):
    if input_value == 0:
        return f'0x{base}'
    result = ''
    while input_value > 0:
        remainder = input_value % base
        result = helper_for_any(remainder) + result
        input_value = input_value // base
    return result + f'x{base}'


def get_base(input_value):
    while True:
        if 'x' not in input_value:
            print('not valid input')
            continue
        else:
            num, base_str = input_value.split('x', 1)
            base = int(base_str)
            return num, base


def helper_for_any(input_value):
    return '0123456789ABCDEF'[input_value]


def prompt_for_bool(prompt):
    while True:
        str_value = input(prompt)
        if str_value.lower() not in ['yes', 'no']:
            print('Please enter yes or no')
            continue
        return str_value.lower() == 'yes'


while True:
    user_input = input('Please enter your number with xN (where N is the base): ')
    num_str, input_base = get_base(user_input)

    target_base = valid_int('Please enter the target base (2-16): ')

    if int(input_base) == int(target_base):
        print(f'Your input is already in same base: {user_input}')
    else:
        if input_base != 10:
            decimal_value = to_decimal(num_str, input_base)
        else:
            decimal_value = int(num_str)

        if target_base == 10:
            print(f'Converted to decimal: {decimal_value}')
        else:
            converted_value = decimal_to_any_base(decimal_value, target_base)
            print(f'Converted to base {target_base}: {converted_value}')

    if not prompt_for_bool('Continue? '):
        break
