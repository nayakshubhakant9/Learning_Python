try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("What kind of operation do you want to perform. Press + for addition\npress - for substraction\npress division\n press * for multiplication ")

    o = input("Enter operation: ")
    match 0:
        case "+":
            print(f("The result is: (a + b)"))
        case "-":
            print(f("The result is: (a - b)"))
        case "*":
            print(f("The result is: (a * b)"))
        case "/":
            print(f("The result is: (a / b)"))
        case default:
            print(f("There was an error"))    

except Exception as e:
    print("Enter a valid value of a and b")
