def prompt_for_int(prompt, min=None, max=None):
    while True:
        str_value = input(prompt)
        if not str_value.isdigit():
            print('please enter numerical value')
            continue
        int_value = int(str_value)
        if min and int_value < min:
            print('please enter value greater or equal than', min)
            continue
        if max and int_value > max:
            print('please enter value less or equal than', max)
            continue
        return int_value

# calculations in dollars
salary_total = prompt_for_int("please enter your total salary ")
expected_salary_growth = prompt_for_int("please enter expected salary raise (in percents) each 6 month  ", 0, 100)
saving_percent = prompt_for_int("please enter how much you can save each month (in percents) ", 0, 100)
real_estate_cost = prompt_for_int("please enter the real estate cost ")
initial_contribution_percent = prompt_for_int("please enter initial contribution (in percents) ", 0, 100)
annual_interest_rate_percent = prompt_for_int("please enter the investment annual interest rate (in percents) ", 0, 100)

# what we need, example $100000 * 25% = $25000
target_amount = real_estate_cost * initial_contribution_percent / 100

# what we can invest per month, example $1000 * 50% = $500
can_save_monthly = salary_total * saving_percent / 100

# at the beginning of 1st month we make initial $500 investment
current_amount = can_save_monthly

month_count = 1

# one iteration - one month
while current_amount < target_amount:
    if month_count % 6 == 0:
        salary_with_bonus = salary_total + (salary_total * (expected_salary_growth / 100))
        salary_total = salary_with_bonus
        can_save_monthly = salary_with_bonus * (saving_percent / 100)
    interest = current_amount * annual_interest_rate_percent / 12 / 100
    current_amount = current_amount + interest
    current_amount = current_amount + can_save_monthly
    month_count = month_count + 1


print(month_count // 12, 'years', month_count % 12, 'months')



def prompt_for_bool(prompt):
    while True:
        str_value = input(prompt)
        if str_value not in ['yes', 'no']:
            print('please enter yes or no')
            continue
        if str_value == 'yes':
            return True
        else:
            return False


cont = prompt_for_bool("please enter do you want to calculate the body of the loan ")
if not cont:
    exit(1)

years_of_loan = prompt_for_int("please enter how many years of lending ")
annual_percent = prompt_for_int("please enter your annual percent  ", 0, 100)

# this is amount that has to be paid on top of lending body
surplus = real_estate_cost * (annual_percent / 100) * years_of_loan
loan_body = (real_estate_cost + surplus) - target_amount
has_to_pay_monthly = loan_body / years_of_loan / 12

if has_to_pay_monthly > can_save_monthly:
    print('loan is impossible :(')
else:
    print('loan is possible! :)')


print(has_to_pay_monthly)
