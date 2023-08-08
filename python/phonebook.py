import csv
with open("phonebook.csv", "a") as file:
    name = input("Name: ")
    number = input("Number: ")

    writer = csv.DictWriter(file, fieldnames=["Name", "Number"])
    writer.writerow({"Name": name, "Number": number})