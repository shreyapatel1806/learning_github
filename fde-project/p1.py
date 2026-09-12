import csv

with open(r"d:\my_projects\fde-project\customers.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for customer in reader:
        print(customer["id"],"\t",customer["name"],"\t",customer["city"])
        # print(customer["name"],"\t",customer["city"])