class student():
    name = ""
    GPA = -1

    def addInfo(self, n, gpa):
        self.name = n
        self.GPA = gpa

    def showInfo_std(self):
        print("Thong tin SV:  ")
        print(self.name)
        print(self.GPA)

    def is_Good_Student(self):
        if (self.GPA >=8.0):
            print("Day la SV gioi")
        else:
            print("Ban can co gang them")

    def is_Bad_Student(self):
        if (self.GPA <=5.0):
            return 1
        else:
            return 0
class classRoom():
    std_list = []

    def nhapInfo_std(self, aname, agpa):
        studentA = student()
        studentA.addInfo(aname, agpa)
        self.std_list.append(studentA)

    def nhapInfo(self, classSize):
        for i in range(classSize):
            print("Nhap thong tin cho SV thu "+ str(i+1))
            print("Nhap ten:")
            name = input()
            print("Nhap diem:")
            gpa = input()
            self.nhapInfo_std(name, gpa)

    def ShowInfo(self):
        for i in range(len(self.std_list)):
            print("Thong tin cho SV thu " + str(i+1))
            self.std_list[i].showInfo_std()

    def find_the_best(self):
        best = self.std_list[0]
        for i in range(len(self.std_list)):
            if (self.std_list[i].GPA > best.GPA):
                best = self.std_list[i]
        return best
    def countStudent(self):
        return len(self.std_list)

    def countGoodStudent(self):
        count = 0
        for i in range(len(self.std_list)):
            if (self.std_list[i].is_Good_Student()):
                count += 1
        return count

    def countBadStudent(self):
        count = 0
        for i in range(len(self.std_list)):
            if (self.std_list[i].is_Good_Student()==1):
                self.std_list[i].showInfo_std




if __name__ == '__main__':
    csd203 = classRoom()
    csd203.nhapInfo(4)
    print("--------------------------------------")
    csd203.ShowInfo()
    print("--------------------------------------")
    A = csd203.find_the_best()
    A.showInfo_std()



