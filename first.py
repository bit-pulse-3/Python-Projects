choice = 0
while choice != 5:
    choice = int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\nChoose Option:"))
    match (choice):
        case 1:
            val_count = int(input("Enter number of values to add:"))
            value = 0
            for i in range(val_count):
                input_value = int(input(f"Enter {i} value:"))
                value += input_value
            print(f"The addition of the numbers = {value}")
        case 2:
            val_count = int(input("Enter number of values to subtract:"))
            value = 0
            for i in range(val_count):
                input_value = int(input(f"Enter {i} value:"))
                value -= input_value
            print(f"The subtraction of the numbers = {value}")
        case 3:
            val_count = int(input("Enter number of values to multiply:"))
            value = 1
            for i in range(val_count):
                input_value = int(input(f"Enter {i} value:"))
                value *= input_value
            print(f"The multiplication of the numbers = {value}")
        case 4:
            input_value = int(input("Enter nomenator value:"))
            input_value2 = int(input("Enter denomenator value:"))
            value = input_value / input_value2
            print(f"The divison of the numbers = {value}")
        case 5:
            print("Exit Succesfull.......\n")
