import csv
csv_file_path = "data/products.csv"

#Menu Greeting & Inputs
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
chosen_operation = chosen_operation.title()
print(chosen_operation)

# Product List
products = []

#Menu Definitions
def list_products(): #List Definition
        print("\n")
        print("List")
        print("THERE ARE 20 PRODUCTS:")
        with open(csv_file_path,"r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                print(" + ", dict(row))
def show_product(): #Show Definition
    with open(csv_file_path,"r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            products.append(row)
    print("There are " + str(len(products)) + " Products")
def create_product(): #Create Definition
    print("CREATING A PRODUCT")
def update_product(): #Update Definition
    print("UPDATING A PRODUCT")
def destroy_product(): #Destroy Definition
    print("DESTROYING A PRODUCT")

#Menu If statements
if chosen_operation == "List": list_products()
elif chosen_operation == "Show": show_product()
elif chosen_operation == "Create": create_product()
elif chosen_operation == "Update": update_product()
elif chosen_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")
