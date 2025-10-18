def calculate_gross_pay(hours_worked):
    MONEY_PER_HOUR = 10
    HOURS_WORKED_BEFORE_OVERTIME = 40
    OVERTIME_RATE = 1.5

    # Regular and overtime hours
    regular_hours = min(hours_worked, HOURS_WORKED_BEFORE_OVERTIME)
    overtime_hours = max(0, hours_worked - HOURS_WORKED_BEFORE_OVERTIME)

    # Pay calculations
    gross_pay = (regular_hours * MONEY_PER_HOUR) + (overtime_hours * MONEY_PER_HOUR * OVERTIME_RATE)
    return gross_pay


def calculate_pre_tax_amount(amount):
    RETIREMENT_DEDUCTION = 3.0  # percent
    deduction = amount * (RETIREMENT_DEDUCTION / 100)
    return amount - deduction


def calculate_post_tax_amount(amount):
    STATE_TAX = 5.6
    FEDERAL_TAX = 7.9
    state_deduction = amount * (STATE_TAX / 100)
    federal_deduction = amount * (FEDERAL_TAX / 100)
    return amount - state_deduction - federal_deduction


# Create dictionary to store multiple employees
employees = {}

# Start loop to enter employee data
while True:
    print("\nEnter Employee Information:")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    emp_id = input("Employee ID: ")
    dependents = int(input("Number of dependents: "))
    hours_worked = int(input("Hours worked: "))

    # Calculations
    gross_pay = calculate_gross_pay(hours_worked)
    pre_tax_amount = calculate_pre_tax_amount(gross_pay)
    post_tax_amount = calculate_post_tax_amount(pre_tax_amount)

    # Store employee info
    employees[emp_id] = {
        "first name": first_name,
        "last name": last_name,
        "dependents": dependents,
        "hours worked": hours_worked,
        "gross pay": gross_pay,
        "pre-tax amount": pre_tax_amount,
        "post-tax amount": post_tax_amount
    }

    # Ask user if they want to continue
    another = input("\nWould you like to enter another employee? (yes/no): ").strip().lower()
    if another != "yes":
        break


# Display all employee information
print("\n=== Employee List ===")
for eid, info in employees.items():
    print(f"""
ID: {eid}
First Name: {info['first name']}
Last Name: {info['last name']}
Dependents: {info['dependents']}
Hours Worked: {info['hours worked']}
Gross Pay: ${info['gross pay']:,.2f}
Pre-Tax Amount: ${info['pre-tax amount']:,.2f}
Post-Tax Amount: ${info['post-tax amount']:,.2f}
""")