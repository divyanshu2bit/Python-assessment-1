# Program to read employee name and salary until "stop"
# Then calculate total salary (Basic + HRA 20% + DA 10%)

employees = []   # list to store tuples (name, salary)

while True:
    name = input("Enter employee name (type 'stop' to end): ")

    if name.lower() == "stop":
        break

    salary = int(input("Enter basic salary: "))
    
    employees.append((name, salary))


# Display total salary
print("\n--- Employee Salary Details ---")

for name, basic_salary in employees:
