
def task1(x,y):
    add = x + y
    diff = x - y
    if y != 0 :
        div = x / y
    else:
        div = "Enter a non zero number!"
    mult = x * y

    print("Addition: ", add, "\nSubtraction: ", diff, "\nMultiplication: ", mult, "\nDivision: ", div)

a,b = int(input("Enter two numbers to perform operations on-\n First number: ")), int(input("Second number: "))

task1(a,b)