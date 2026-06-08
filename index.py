print("Hello World!")

a=int(input("Enter a number:"))

def check(a):
    if a%2==0:
        print("Even")
    else:
        print("Odd")
def check_number_as_multiple(a):
    for i in range(a):
        if i%a==0:
            print(i)

def printmessage():
    print("hello")
    

print(f"number {a} is {check(a)}")
print(f"{a} is a multiple of:{check_number_as_multiple(a)}") 