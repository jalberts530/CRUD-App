import csv

products = []

csv_file_path = "data/products.csv"
#csv_file_path_2 = "data/other_products.csv"

# READ PRODUCTS CSV
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

#Product Lookup
def lookup_product_by_id(product_id):
    matching_products = [product for product in products if product["id"] == product_id]
    return matching_products[0] # because the line above gives us a list and we want to return a single item

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
    product_id = input("Please input a valid product identifier. ")
    for product in products:
        product_show = lookup_product_by_id(product_id)
    print("SHOW PRODUCT HERE: ", dict(product_show))

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
    update_product_id = input("Please input a valid product identifier. ")
    product = [i for i in products if i["id"]==update_product_id]
    if product:
        product = product[0]
        print(dict(product))
        update_product_name = input("What should we change the NAME to?: ")
        update_product_aisle = input ("What should we change the AISLE to?: ")
        update_product_department= input("What should we change DEPARTMENT to?: ")
        update_product_price = input("What should we change PRICE to?: ")
        updated_product = {
        "name":update_product_name,
        "aisle":update_product_aisle,
        "department":update_product_department,
        "price":update_product_price
        }
        print("We will update to ",dict(updated_product) )
        confirmation = input("Please type Y if its okay to update: ")
        confirmation = confirmation.capitalize()
        if confirmation == "Y":
            product["name"] = update_product_name
            product["aisle"]= update_product_aisle
            product["department"]=update_product_department
            product["price"]=update_product_price
            print("Updated product")
        else:
            print("Try again")
    else:
            print("Not a valid ID, please try again")


def destroy_product():
    print("DESTROYING A PRODUCT")
    destroy_product = input("Please input a valid product identifier. ")
    product = [i for i in products if i["id"] == destroy_product]
    if product:
        product = product[0]
        print("I am destroying the following product: ")
        print(dict(product))
        confirmation = input("Please type Y if its okay to destroy: ")
        confirmation = confirmation.capitalize()
        if confirmation == "Y":
            del products[products.index(product)]
            print("Updated product list")
        else:
            print("Try again")

#Menu If Statements
if chosen_operation == "List": list_products()
elif chosen_operation == "Show": show_product()
elif chosen_operation == "Create": create_product()
elif chosen_operation == "Update": update_product()
elif chosen_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")

# OVERWRITING INVENTORY CSV FILE
with open(csv_file_path, "w", newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)
