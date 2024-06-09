class Product:
    def __init__(self, id, name):
        self.id= id
        self.name= name
    def id(self):
        return self.id

    def name(self):
        return self.name

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"
#endclassProduct

class Coffee(Product):
    def __init__(self, id, name, quantity, unitPrice):
        super().__init__(id, name)
        self.quantity= quantity
        self.unitPrice= unitPrice


    def getTotal(self):
        total= self.quantity* self.unitPrice
        return total

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Quantity: {self.quantity}, unitPrice: {self.unitPrice}"
#endclassCoffee

class Program:
    def __init__(self):
        self.coffee_list=[]

    def menu(self):
        print("1.Add new Coffee")
        print("2.Find Coffee by ID")
        print("3.Print Coffee list")
        print("4.Exit")

    def add(self):
        id=int(input("Enter ID: "))
        name=input("Enter name: ")
        quantity=int(input("Enter Quantity: "))
        unitPrice=float(input("Enter unitPrice: "))
        product=Coffee(id, name, quantity, unitPrice)
        print("Coffee added successfully")
        self.coffee_list.append(product)
#end add
    def find(self):
        id = int(input("Enter ID: "))
        for i in self.coffee_list:
            if id == i.id:
                print(i)
            else:
                print("Coffe not found")

    def print_coffee(self):
        for i in self.coffee_list:
            print(i)
#end find
def main():
    program=Program()
    while True:
        program.menu()
        choice=int(input("Enter your choice: "))
        if choice == 1:
            program.add()
        if choice == 2:
            program.find()
        if choice == 3:
            program.print_coffee()
        if choice==4:
            print("Exiting...")
            break
#enddefmain

if __name__=="__main__":
    main()