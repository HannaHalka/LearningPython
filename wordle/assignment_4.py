def decimal_to_binary(input_value: int) -> str:
    if input_value < 0:
        assert False, "Only positive decimals supported"

    if input_value == 0:
        return '0b0'

    result = ''
    while input_value >= 1:
        if input_value % 2 == 1:
            result = '1' + result
        else:
            result = '0' + result

        input_value = input_value // 2
    return '0b' + result


assert decimal_to_binary(0) == '0b0'
assert decimal_to_binary(1) == '0b1'
assert decimal_to_binary(16) == '0b10000'
assert decimal_to_binary(17) == '0b10001'


def binary_to_decimal(input_value: str) -> int:
    assert input_value[:2:] == '0b'
    input_value = input_value[2::]
    result = 0
    rank = 0
    for digit in input_value[::-1]:
        if digit == '1':
            result += 2 ** rank
        elif digit == '0':
            pass
        else:
            assert False, f'Unexpected digit, 0 or 1 are allowed, got {digit}'
        rank += 1
    return result


assert binary_to_decimal('0b0') == 0
assert binary_to_decimal('0b1') == 1
assert binary_to_decimal('0b10000') == 16
assert binary_to_decimal('0b10001') == 17


def prompt_for_bool(prompt: str) -> bool:
    while True:
        str_value = input(prompt)
        if str_value not in ['yes', 'no']:
            print('please enter yes or no')
            continue
        if str_value == 'yes':
            return True
        else:
            return False


def hex_to_decimal(input_value: str) -> int:
    assert input_value[:2:] == '0x'
    input_value = input_value[2::]
    result = 0
    rank = 0
    for digit in input_value[::-1]:
        result += (16 ** rank) * int(digit, 16)
        rank += 1
    return result


assert hex_to_decimal('0x0') == 0
assert hex_to_decimal('0x1') == 1
assert hex_to_decimal('0xAA') == 170
assert hex_to_decimal('0xFF') == 255
assert hex_to_decimal('0xff') == 255


def decimal_to_hex_digit(input_value: int) -> str:
    if input_value == 10: return 'A'
    if input_value == 11: return 'B'
    if input_value == 12: return 'C'
    if input_value == 13: return 'D'
    if input_value == 14: return 'E'
    if input_value == 15: return 'F'
    return str(input_value)


def decimal_to_hex(input_value: int) -> str:
    assert input_value >= 0
    if input_value == 0:
        return '0x0'
    result = ''
    while input_value > 0:
        remainder = input_value % 16
        hex_digit = decimal_to_hex_digit(remainder)
        result = hex_digit + result
        input_value = input_value // 16
    return '0x' + result


assert decimal_to_hex(0) == '0x0'
assert decimal_to_hex(1) == '0x1'
assert decimal_to_hex(16) == '0x10'
assert decimal_to_hex(170) == '0xAA'


def get_number_system():
    while True:
        inp = input("To which number system to convert? \n1 - binary \n2 - decimal \n3 - hex\n  ->  ")
        if inp == '1': return 2
        if inp == '2': return 10
        if inp == '3': return 16


while True:
    user_input = input('Please enter a number: ')

    base = get_number_system()

    if user_input[:2:] == '0b':
        if base == 2:
            print(user_input)
        elif base == 10:
            print(binary_to_decimal(user_input))
        else:
            dec = binary_to_decimal(user_input)
            print(decimal_to_hex(dec))

    elif user_input[:2:] == '0x':
        if base == 2:
            dec = hex_to_decimal(user_input)
            print(decimal_to_binary(dec))
        elif base == 10:
            print(hex_to_decimal(user_input))
        else:
            print(user_input)

    else:
        if base == 2:
            print(decimal_to_binary(int(user_input)))
        elif base == 10:
            print(user_input)
        else:
            print(decimal_to_hex(int(user_input)))

    if not prompt_for_bool('Continue? '):
        break
