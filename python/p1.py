# making a function to print the devider for each chapter for better understanding of the code
def devider(name , chapter):
    length = f"{name} is reading program {chapter}"
    print("\n")
    print(length)
    print("=" * len(length))



# first chapter of python
devider("Python", 1)
def add(a, b):
    return a + b

print(add(10,20))
print(add(10,40) * 2)
print(add(10,70) + 100)



# second chapter of python
devider("Python", 2)
def sub(a, b):
    return a - b

result = sub(30, 20)
print(result)



# third chapter of python
devider("Python", 3)
j = int(input("Enter a number: "))
print("\n")
for i in range(1, 11, 1):
    k = f"{j} * {i} ="
    print(k , j * i)



# fourth chapter of python
devider("Python", 4)
i = 1
p = int(input("Enter a number: "))
print("\n")
while i < 11:
    product = p * i
    print(f"{p} * {i} = {product}")
    i += 1



#fifth chapter of python
devider("Python", 5)
def employee_name(name):
    return name

def calculate_salary(hours_worked, hourly_rate):
    return hours_worked * hourly_rate

def calculate_bonus(salary):
    return salary * 0.10

def calculate_final_salary(salary, bonus):
    return salary + bonus

def display_report(name, salary, bonus, final_salary):
    print("Employee:", name)
    print("Salary:", salary)
    print("Bonus:", bonus)
    print("Final Salary:", final_salary)

hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))
nam = employee_name(input("Enter employee name: "))       
salary = calculate_salary(hours_worked, hourly_rate)
bonus = calculate_bonus(salary)
final_salary = calculate_final_salary(salary, bonus)
display_report(nam, salary, bonus, final_salary)