class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
products=[]

def add_product():
    name=input("Enter name: ")
    price=input("Enter price: ")
    quantity=input("Enter quantity: ")
    product=Product(name,price,quantity)
    products.append(product)
    print(f"Product {name} added")

def update_price():
    name=input("Enter the product name: ")
    new_price=float(input("Enter new price: "))
    for product in products :
        if name == product.name:
            product.price=new_price
            break
        else:
            print(f"Product {name} not found")

def available_products():
    for product in products:
        if int(product.quantity) >0 :
            print(f"Name: {product.name}, Price: {product.price}, Available Quantity: {product.quantity}")
        else:
            print("Sold out")
def all_products():
    print("Product in store: ")
    for product in products:
        print(f"Name: {product.name}, Price: {product.price}, Available Quantity: {product.quantity}")

def get_choice():
    print("1. Add product")
    print("2. Update the price of the product")
    print("3. A list of all available products in the Store")
    print("4. Print all product")
    print("5.Exit")
    choice=int(input("Enter your choice: "))
    return choice

def main():
    while True:
        choice = get_choice()
        if   choice == 1: add_product()
        elif choice == 2: update_price()
        elif choice == 3: available_products()
        elif choice == 4: all_products()
        elif choice == 5 :
            break

        else:
            print("Invalue choice")

if __name__=="__main__":
    main()


