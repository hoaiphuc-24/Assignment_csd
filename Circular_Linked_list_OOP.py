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

class Circular_LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_last(self, name, ID, GPA):
        newStd = Std(name, ID, GPA)
        newNode = Node(newStd)
        if self.size==0:
            self.head= newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        self.tail.next= self.head

    def show(self):
        t=self.head
        i=0
        while (i< self.size):
            t.data.show_std()
            t=t.next
            i+=1


    def deleteFirst(self):
        if self.size > 1:
            self.head= self.head.next
            self.tail.next=self.head
        else:
            self.head = None
            self.tail = None
            self.size = 0
        self.size-=1

    # 
    def f1(self):
        pass


    # 
    def f2(self):
        self.deleteFirst()


    def f3(self):
        s=self.size
        print(f"Số lượng sinh viên là {s}")



    # 
    def f4(self):
        t=self.head
        count=0
        i = 0
        while (i < self.size):
            if t.data.GPA >= 5:
                count+=1
            t = t.next
            i += 1
        print(count)


    # 
    def f5(self):
        pass
        
    # 
    def f6(self):
        pass

    # 
    def f7(self):
        t=self.head
        for i in range(self.size):
            if t.data.name =="Vo Van E":
                t.data.GPA+=1
            t=t.next
        self.show()

    def f8(self):
        TMP=Circular_LinkedList()
        t = self.head
        for i in range(self.size):
            if t.data.GPA <8:
                TMP.add_last(t.data.name, t.data.ID, t.data.GPA)
            t=t.next
        self.head = TMP.head
        self.size = TMP.size
        self.show()

    
if __name__ == '__main__':
    lst = Circular_LinkedList()
    lst.add_last("Nguyen Van A", "SE1701", 8)
    lst.add_last("Le Van B", "SE1701", 7)
    lst.add_last("Tran Van C", "SE1701", 9)
    lst.add_last("Nguyen Thi D", "SE1701", 10)
    lst.add_last("Vo Van E", "SE1701", 5)
    
    print("List da khoi tao xong\n")
    print("Ban muon lam gi?\n")
    print("1. show list\n")
    print("2. xoa SV dau tien\n")
    print("3. dem so luong SV trong list\n")
    print("4. dem so luong SV gioi (GPA>=5)\n")
    print("5. tinh tong cac phan tu\n")
    print("6. tim SV co GPA cao nhat trong lop\n")
    print("7. bonus cho SV Vo Van E them 1 diem\n")
    print("8. xóa sinh viên điểm trên 8\n")
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