def get_number():
    try:
        a=int(input("Enter a number: "))
        return a
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_number()
    

if __name__ == "__main__":
    print(get_number())
    print(get_number())
    print(get_number())