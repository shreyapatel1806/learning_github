
### pytest example

def add(a,b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -5) == -10

test_add()


###email validation

email = input("Enter email: ")

if "@" in email and ".com" in email:
    print("Valid email")
else:
    print("Invalid email")





### password validation
password = input("Enter password: ")

if len(password) < 8:
    print("Password must be at least 8 characters")
elif not any(char.isupper() for char in password):
    print("Password must contain an uppercase letter")
elif not any(char.islower() for char in password):
    print("Password must contain a lowercase letter")
elif not any(char.isdigit() for char in password):
    print("Password must contain a number")
else:
    print("Valid password")



### validation and exapction handlingtry:

try:
    age = int(input("Enter age: "))
    print("Age:", age)

except ValueError:
    print("Please enter a valid number")


    
if age < 0:
        print("Age cannot be negative")
elif age < 120:
        print("Valid age")
else:
        print("Age cannot be greater than 120")