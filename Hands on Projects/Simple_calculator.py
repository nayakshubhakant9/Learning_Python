try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("What kind of operation do you want to perform.\nPress + for addition\npress - for substraction\npress / division\npress * for multiplication ")

    o = input("Enter operation: ")
    match o:
        case "+":
            print(f"The result is: {a + b}")
        case "-":
            print(f"The result is: {a - b}")
        case "*":
            print(f"The result is: {a * b}")
        case "/":
            print(f"The result is: {a / b}")
        case default:
            print(f"There was an error")    

except Exception as e:
    print("Enter a valid value of a and b")
