import csv
csv_file_path = "data/products.csv"

print("----------------------------------")
print("PRODUCTS APPLICATION")
print("----------------------------------")
print("Welcome User!")
print("\n")
print("There are 20 Products in the database. Please choose an operation:" )
print("\n")
print("    operation | description" )
print("    --------- | -----------")
print("    'List'    | Display a list of product identifiers and names.")
print("    'Show'    | Show information abouta product.")
print("    'Create'  | Add a new produt.")
print("    'Update'  | Edit an exisiting product.")
print("    'Destroy' | Delete an exisiting product")

print("\n")
chosen_operation = input("Input Operation: ")
print(chosen_operation)

if chosen_operation.title() == "List":
    print("\n")
    print("List")
    print("THERE ARE 20 PRODUCTS:")
    with open(csv_file_path,"r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(" + " + str(row))
elif chosen_operation.title() == "Show":
    print("SHOWING A PRODUCT")
elif chosen_operation.title() == "Create":
    print("CREATING A PRODUCT")
elif chosen_operation.title() == "Update":
    print("UPDATING A PRODUCT")
elif chosen_operation.title() == "Destroy":
    print("DESTROYING A PRODUCT")
else:
    print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")
