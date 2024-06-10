class Std:
    def __init__(self, name, ID, GPA):
        self.name = name
        self.ID = ID
        self.GPA = GPA
    def show_std(self):
        print(self.name, ", ", self.ID, ", ", self.GPA)

class Node:
    def __init__(self, value):
        self.data = value # value o day la student
        self.next = None
        self.prev = None

class Doubly_LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_last(self, name, ID, GPA):
        newStd= Std(name, ID, GPA)
        newNode= Node(newStd)
        if (self.size == 0):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next= newNode
            newNode.prev= self.tail
            self.tail= newNode
        self.size +=1

    def show_fw(self):
        # show info from head to tail
        t=self.head
        while t != None:
            t.data.show_std()
            t=t.next
        
    def show_bw(self):
        # show info from tail to head
        t = self.tail
        while t != None:
            t.data.show_std()
            t = t.prev
        #
    def f1(self):
        print("From head to tail:\n")
        self.show_fw()
        print("From tail to head:\n")
        self.show_bw()

    # 
    def add_first(self,name, ID, GPA):
        newStd = Std(name, ID, GPA)
        newNode = Node(newStd)
        if(self.size == 0):
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev= newNode
            self.head= newNode

    def f2(self):
        print("(Before from head to tail:\n")
        self.show_fw()
        self.show_bw()
        self.add_first("New student", "SE1878", "3")
        print("After rom head to tail:\n")
        self.show_fw()
        self.show_bw()
    #
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def deleteFirst(self):
        if self.size > 1:
            self.head= self.head.next
            self.head.prev=None
            self.size-= 1
        if self.size <2:
            self.clear()

    def f3(self):
        print("(Before from head to tail:\n")
        self.show_fw()
        self.show_bw()
        self.deleteFirst()
        print("After rom head to tail:\n")
        self.show_fw()
        self.show_bw()


    def deleteLast(self):
        if self.head > 1:
            self.tail= self.tail.prev
            self.tail.next=None
            self.size-= 1
        if self.head <2:
            self.clear()

    def f4(self):
        print("(Before from head to tail:\n")
        self.show_fw()
        self.show_bw()
        self.deleteLast()
        print("After rom head to tail:\n")
        self.show_fw()
        self.show_bw()

    # 
    def f5(self):
        t = self.head
        count = 0
        while t != None:
            count += 1
            t = t.next
        print(count)

        
    # 
    def f6(self):
        t= self.head
        count=0
        while t!= None:
            if t.data.GPA > 8:
                count+=1
            t=t.next
        print(count)


    # 
    def f7(self):
        t = self.head
        average_point = 0
        while t != None:
            average_point+= t.data.GPA
            t=t.next
        print(average_point/self.size)

    #
    def f8(self):
        max_std=0
        std=""
        t=self.head
        while t != None:
            if t.data.GPA > max_std:
                max_std= t.data.GPA
                std=t
            t=t.next
        print(std.data.show_std())

    # 
    def f9(self):
        t= self.head
        while t!=None:
            if t.data.GPA <8:
                t.data.GPA+=0.5
            t=t.next
        self.show_fw()

    
if __name__ == '__main__':
    lst = Doubly_LinkedList()
    lst.add_last("Nguyen Van A", "SE1701", 8)
    lst.add_last("Le Van B", "SE1701", 7)
    lst.add_last("Tran Van C", "SE1701", 9)
    lst.add_last("Nguyen Thi D", "SE1701", 10)
    lst.add_last("Vo Van E", "SE1701", 5)
    
    print("List da khoi tao xong\n")
    print("Ban muon lam gi?\n")
    print("1. show list\n")
    print("2. them phan tu dau tien\n")
    print("3. xoa phan tu dau tien\n")
    print("4. xoa phan tu cuoi cung\n")
    print("5. dem so luong SV\n")
    print("6. dem so luong sinh vien co diem GPA lon hon 8\n")
    print("7. tinh diem trung binh cac sinh vien trong list\n")
    print("8. tim sinh vien co diem cao nhat\n")
    print("9. cong 0.5 diem cho cac sinh vien có GPA duoi 8 \n")

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
    if (choice == 8):
        lst.f8()
    if (choice == 9):
        lst.f9()