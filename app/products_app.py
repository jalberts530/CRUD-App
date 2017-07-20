import csv
csv_file_path = "data/products.csv"
csv_file_path_2 = "data/other_products.csv"

products = []

#List File
def read_file():
    with open(csv_file_path,"r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(" + ", dict(row))

#Read & Append
with open(csv_file_path,"r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

#Write File
def write_file():
    with open(csv_file_path_2, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
        writer.writeheader() # uses fieldnames set above
        for product in products:
            writer.writerow(product)

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



#Menu Definitions
def list_products(): #List Definition #TODO Troubleshoot
        print("\n")
        print("List")
        print("THERE ARE 20 PRODUCTS:")
        read_file()

def show_product(): #Show Definition
    #print("SHOWING A PRODUCT")
    print("There are " + str(len(products)) + " Products")

def create_product(): #Create Definition
    write_file()

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
