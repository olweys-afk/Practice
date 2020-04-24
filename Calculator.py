def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y


print("A. Add")
print("B. Sub")
print("C. Mul")
print("D. Div")
Sel = input("Select Action:")

First = int(input("Enter A Number:"))
Second = int(input("Enter A Number:"))

if Sel == 'A':
    c = add(First,Second)
    print(c)

if Sel == 'B':
    c = sub(First,Second)
    print(c)

if Sel == 'C':
    c = mul(First,Second)
    print(c)

if Sel == 'D':
    c = div(First,Second)
    print(c)


