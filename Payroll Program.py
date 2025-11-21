# Constants
MAX_HOURS = 60
HOURLY_RATE = 20

# A list to store all employees records
employees = []

def housekeeping():
    """Collects data for one employee and returns it as a dictionary."""
    employee_name = input("Enter employee first and last name or enter DONE to print results")

    if employee_name.upper() == "DONE":
        return None
    
    employee_id = input ("Enter employee ID")
    dependents = int(input("Number of dependents: "))

    hours_worked = float(input("Enter hours worked"))
    if hours_worked > MAX_HOURS:
        print("Invalid input: hours worked cannot exceed 60.")
        return home
    
    #Return collected employee data
    return {
        "name": employee_name,
        "id": employee_id,
        "dependents": dependents,
        "hours": hours_worked

    }

def print_results():
    print("----RESULTS----")
    for emp in employees:
        print(f"Name: {emp['name']}")
        print(f"ID: {emp['id']}")
        print(f"Dependents: {emp['dependents']}")
        print(f"Hours Worked: {emp['hours']}")
        print(f"Gross Pay: {emp.get('gross_pay', 'N/A')}")
        print("------------")


#-------------MAIN PROGRAM LOOP--------------

while True:
    record = housekeeping():

    # User types DONE -> break out and print results
    if record is None:
        break
    # Add employee record to the list
    employees.append(record)

    # CHeck if we have 5 employees (or decided amount of employees)
    if len(employees) >= 5:  # <-- change number if needed



# After collecting employees, run calculations
    calculations():
   

# Print final results
    print_results()
