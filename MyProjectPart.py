#number of hours worked regular + overtime
def caculate_gross_pay(hours_worked):
    MONEY_PER_HOUR = 10
    HOURS_WORKED_BEFOR_OVERTIME = 40
    OVERTIME = 1.5
    print("hours_worked", hours_worked)

    #only regular amount worked
    regular_hours_worked = hours_worked
    if hours_worked > HOURS_WORKED_BEFOR_OVERTIME:
        regular_hours_worked = HOURS_WORKED_BEFOR_OVERTIME
    print("regular_hours_worked", regular_hours_worked)

    #overtime worked
    over_time_hours_worked  = 0
    if hours_worked > HOURS_WORKED_BEFOR_OVERTIME :
        over_time_hours_worked = hours_worked - HOURS_WORKED_BEFOR_OVERTIME
    print("over_time_hours_worked", over_time_hours_worked)


    gross_pay_amount = regular_hours_worked * MONEY_PER_HOUR
    overtime_payment =  over_time_hours_worked * MONEY_PER_HOUR * OVERTIME
    return gross_pay_amount + overtime_payment

def caculate_pre_tax_amount(amount):
    return amount


def caculate_post_tax_amount(amount):
    STATE_TAXES = 5.6
    FEDERAL_TAXES = 7.9
    state_deductions = amount * (STATE_TAXES / 100)
    federal_deductions = amount * (FEDERAL_TAXES / 100)


    return amount - state_deductions - federal_deductions





employ_first_name = input("What is your first name ? ")
employ_last_name =  input("what is yout last name ? ")
employ_id = input("What is your ID ? ")
employ_number_of_dependent = int(input("What is your number of dependent "))
employ_hours_worked = int(input("How many hours have your worked "))

gross_pay = caculate_gross_pay(employ_hours_worked)

pre_tax_amount = caculate_pre_tax_amount(gross_pay)

post_tax_amount = caculate_post_tax_amount(gross_pay)



# Use nested dictionary variable to store employees' information
employees = {}
employees[employ_id] = {
    "first name": employ_first_name,
    "last anme": employ_last_name,
    "number of dependents": employ_number_of_dependent,
    "hours worked": employ_hours_worked,
    "gross pay": gross_pay,
    "pre-tax amount": pre_tax_amount,
    "post-tax amount": post_tax_amount
}

# Output each employee's information
print("\nEmployee List:")
for eid, info in employees.items():
    print(f"ID: {eid}\n"
          f"first name: {info['first name']}\n"
          f"last name: {info['last anme']}\n"
          f"number of dependents: {info['number of dependents']}\n"
          f"hours worked: {info['hours worked']}\n"
          f"gross pay: ${info['gross pay']:,.2f}\n"
          f"pre-tax amount: ${info['pre-tax amount']:,.2f}\n"
          f"post-tax amount: ${info['post-tax amount']:,.2f}\n\n"
          )







