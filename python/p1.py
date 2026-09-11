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