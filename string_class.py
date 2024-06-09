def isreverse(string):
    reversed_string=string[::-1]
    print(reversed_string)
#string=input("Nhap string:")
#isreverse(string)
#endreverse

def count(string_char):
    specialcharacters=0
    for char in string_char:
        if not char.isalnum():
            specialcharacters += 1
    return specialcharacters

#string_char=input("Enter string: ")
#count(string_char)
#print(count(string_char))
#end

def sort_list():
    items=input("Enter list name: ")
    ascend=items.split()
    ascend.sort()
    print("The list of items name is:", ascend)
sort_list()
#endsort
