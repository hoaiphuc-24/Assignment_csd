from datetime import date
def addition(firstNumber, secondNumber):
    return firstNumber + secondNumber
#end addition

def printDate():
     today = date.today()
     print("Today date is: ", today)
#end printDate
def getDate():
    today = date.today()
    return today
#end getDate
def hello(name):
    print("Hello: "+ name)
#end hello


sum = addition(1,2)
print(sum)
#invoke printDate
printDate()
#invoke getDate funtion
d= getDate()
print(d)
#invoke hello funtion
hello("David")