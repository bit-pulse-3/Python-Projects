def get_number():
    try:
        a=int(input("Enter a number: "))
        return a
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_number()

# pyrefly: ignore [parse-error]
def get_number_as_multiple_2():
    a=get_number()
    if a%2==0:
        return a
    else:
        return get_number_as_multiple_2()
    

if __name__ == "__main__":
    print(get_number_as_multiple_2())
    print(get_number_as_multiple_2())
    print(get_number_as_multiple_2())