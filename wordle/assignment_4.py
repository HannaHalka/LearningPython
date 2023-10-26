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


while True:
    user_input = input('Please enter a number: ')
    if user_input[:2:] == '0b':
        print(binary_to_decimal(user_input))
    else:
        print(decimal_to_binary(int(user_input)))

    if not prompt_for_bool('Continue? '):
        break
