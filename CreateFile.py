#Create a text file
def CreateFile():
    try:
        print("Enter file's content:")
        fhand = open("data.txt", "w")
        s = input(">")
        while (s.lower() != "done"):
            fhand.write(s+"\n")
            s = input(">")
        print("Winite successfully")
        fhand.close()
    except:
        print('Error:')
#end function
def ReadFile():
    try:
        fhand = open("data.txt", "r")
        for str in fhand:
            print(str.rstrip())
        fhand.close()
    except:
        print("Error:")
        quit()
#end function
def main():
    CreateFile()
    print("Read data from file:")
    print('*'*25)
    ReadFile()
#end main
#------------------------------***********************-------------------
if __name__ == "__main__":
    main()