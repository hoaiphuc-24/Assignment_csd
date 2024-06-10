class Phone:
    def __init__(self,n,b,p):
        self.name = n
        self.brand = b
        self.price = p
    def show_Phone(self):
        print(self.name, ", ", self.brand,", ", self.price)


class Node:
    def __init__(self, elem, next_node):
        self.elem = elem # elem la mot bien co kieu la Phone
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def addFirst(self, n,b,r):
        newPhone= Phone(n,b,r)
        newNode= Node(newPhone, None) #self.head = Node(Phone(n,b,p), self.head)
        newNode.next= self.head
        self.head= newNode
    def deleteFirst(self):
        if self.head != None:
            self.head= self.head.next


    def show(self):
        t=self.head
        while t != None:
            t.elem.show_Phone()
            t=t.next

    def f1(self):
        self.show()

    def f2(self):
        self.deleteFirst()

    def f3(self):
        t = self.head
        count=0
        while t != None:
            count+=1
            t= t.next
        print(count)

    def f4(self):
        count = 0
        t = self.head
        while t != None:
            if t.elem.price  > 5:
                count+=1
            t = t.next
        print(count)

    def f5(self):
        sum_price=0
        t = self.head
        while t != None:
            sum_price+= t.elem.price
            t = t.next
        print(sum_price)

    def f6(self):
        max_price= 0
        t=self.head
        while t != None:
            if t.elem.price > max_price:
                max_price= t.elem.price
            t = t.next
        print(max_price)


    def f7(self):
        t = self.head
        while t != None:
            if t.elem.brand== "Samsung":
                t.elem.price*=0.9
            t = t.next
    def deletelast(self):
        t = self.head
        if t < 2:
            self.head=None
            return
        while t.next.next != None:
            t= t.next
            return

    def delete_k(self,k):



if __name__ == '__main__':
    lst = LinkedList()

    lst.addFirst("Galaxy J10", "Samsung", 7)
    lst.addFirst("Galaxy s23", "Samsung", 20)
    lst.addFirst("13 Pro Max", "IPhone", 27)
    lst.addFirst("A32", "Oppo", 10)
    lst.addFirst("Bphone", "Bom_Phone", 5)
    print("List da khoi tao xong\n")
    print("Ban muon lam gi?\n")
    print("1. show list\n")
    print("2. xoa phan tu dau tien\n")
    print("3. dem so luong Phone\n")
    print("4. dem so luong Phone co price lon hon 5\n")
    print("5. tinh tong gia tien Phone trong List\n")
    print("6. Tim Phone co price cao nhat\n")
    print("7. giam gia tat ca dien thoai Samsung 10% \n")

    print("Default: thoat chuong trinh\n")
    choice = input()
    choice = int(choice)
    r = "khong lam gi ca"
    if (choice == 1):
        lst.f1()
    if (choice == 2):
        lst.f2()
    if (choice == 3):
        lst.f3()
    if (choice == 4):
        lst.f4()
    if (choice == 5):
        lst.f5()
    if (choice == 6):
        lst.f6()
    if (choice == 7):
        lst.f7()
