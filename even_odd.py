def evenOdd(n):
    if n%2==0:
        print("Number is Even")
    else:
        print("Number is Odd")

def greater(x,y,z):
    if x>y and y>z:
        print(f"{x} is the Greatest")
    elif y>x and x>z:
        print(f"{y} is the Greatest")
    else:
        print(f"{z} is the Greatest")

def multiplicationtable(n):
    for i in range(1,11): 
        mult = n*i


        print(mult)
arr = [1,2,3,4,5]

def arrevenOdd(arr):
    for i in range(len(arr)):
        if arr[i]%2==0:
            print(f"{arr[i]} is Even")
        else:
            print(f"{arr[i]} is Odd")

stringex = "Kavy changela"
def stringexample(stringex):
    print(stringex.upper())
    print(stringex.capitalize())
    print(stringex.count("a"))
    print(stringex.split("a"))
    print(stringex[1:])
    print(stringex[::-1])
    print(stringex.lower())

evenOdd(5)
greater(1,2,3)
multiplicationtable(3)
arrevenOdd(arr)
stringexample(stringex)

