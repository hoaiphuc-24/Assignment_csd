class Phone:
    def __init__(self, n, b, p):
        self.name = n
        self.brand = b
        self.price = p

    def show_Phone(self):
        print(self.name, ", ", self.brand, ", ", self.price)


class Node:
    def __init__(self, elem, next_node):
        self.elem = elem  # elem la mot bien co kieu la Phone
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def addFirst(self, n, b, p):
        self.head = Node(Phone(n, b, p), self.head)

    def showFW(self,node):
        if node==None:
            print("End of list")
            return
        node.elem.show_Phone()
        self.showFW(node.next)
    def f1(self):
        self.showFW(self.head)

    def showBW(self,node):
        if node==None:
            print("Begin of list")
            return
        self.showBW(node.next)
        node.elem.show_Phone()
    def f2(self):
        self.showBW(self.head)

    def count(self,node):
        if node == None:
            return 0
        return (1 + self.count(node.next))
    def f3(self):
        return self.count(self.head)


    def countf4(self,node):
        if node == None:
            return 0
        if node.elem.price>5:
            return (1+self.count(node.next))
        else:
            return (self.count(node.next))

    def f4(self):
        print( self.countf4(self.head))


    def sumPrice(self,node):
        if node == None:
            return 0
        return (node.elem.price + self.sumPrice(node.next))
    def f5(self):
        print(self.sumPrice(self.head))


    def priceMax(self,node):
        if node== None:
            return 0
        elif (node.elem.price> self.priceMax(node.next)):
            return node.elem.price
        else:
            print(self.priceMax(node.next))

    def f6(self):
        pass
        
    def f7(self):
        pass
    
    def f8(self):
        pass


if __name__ == '__main__':
    lst = LinkedList()

    lst.addFirst("Galaxy J10", "Samsung", 7)
    lst.addFirst("Galaxy s23", "Samsung", 20)
    lst.addFirst("13 Pro Max", "IPhone", 27)
    lst.addFirst("A32", "Oppo", 10)
    lst.addFirst("Bphone", "Bom_Phone", 5)
    lst.addFirst("Prime J7", "Samsung", 4)
    lst.addFirst("13 Pro", "IPhone", 7)
    lst.addFirst("A2", "Oppo", 7)
    lst.addFirst("A20", "Oppo", 15)
    print("List da khoi tao xong\n")
    print("Ban muon lam gi?\n")
    print("1. show list tu dau toi cuoi\n")
    print("2. show list tu cuoi ve dau\n")
    print("3. dem so luong Phone trong list\n")
    print("4. dem so luong Phone co price > 5\n")
    print("5. tinh tong cua Price trong list\n")
    print("6. tim Phone co price cao nhat\n")
    print("7. giam gia tat ca dien thoai Samsung 10% \n")
    print("8. xoa tat ca dien thoai co price > 10 \n")

    print("Default: thoat chuong trinh\n")
    choice = input()
    choice = int(choice)
    r = "khong lam gi ca"
    if (choice == 1):
        lst.f1()
    if (choice == 2):
        lst.f2()
    if (choice == 3):
        r=lst.f3()
        print(r)
    if (choice == 4):
        lst.f4()
    if (choice == 5):
        lst.f5()
    if (choice == 6):
        lst.f6()
    if (choice == 7):
        lst.f7()
    if (choice == 8):
        lst.f8()



