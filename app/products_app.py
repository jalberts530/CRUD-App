import csv

products = []

csv_file_path = "data/products.csv"
csv_file_path_2 = "data/other_products.csv"

# READ PRODUCTS CSV
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

#Menu Greeting & Inputs
print("----------------------------------")
print("PRODUCTS APPLICATION")
print("----------------------------------")
print("Welcome User!")
print("\n")
print("There are " + str(len(products)) + " Products in the database. Please choose an operation:" )
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

#Menu Definitions
def list_products():
    for product in products:
        print(" + ", dict(product))

def show_product():
    print("SHOWING A PRODUCT")

def create_product():
    print("CREATING A PRODUCT")
    product_name = input("name is:")
    product_aisle = input("aisle is:")
    product_department = input("department is:")
    product_price = input("price is:")
    new_product = {
        "id": len(products) + 1,
        "name": product_name,
        "aisle": product_aisle,
        "department": product_department,
        "price": product_price
    }
    print("NEW PRODUCT IS", new_product)
    products.append(new_product)

def update_product():
    print("UPDATING A PRODUCT")

def destroy_product():
    print("DESTROYING A PRODUCT")

#Menu If Statements
if chosen_operation == "List": list_products()
elif chosen_operation == "Show": show_product()
elif chosen_operation == "Create": create_product()
elif chosen_operation == "Update": update_product()
elif chosen_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")

# OVERWRITING INVENTORY CSV FILE
with open(csv_file_path_2, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)
