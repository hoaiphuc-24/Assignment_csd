expression = input("Enter a simple expression: ")
try:
    result=eval(expression)
except:
    print("A simple expression containing one of four operators +, -, *, / ")
else:
    print(f"The result of {expression} is {result}.")