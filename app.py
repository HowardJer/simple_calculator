import addition
import subtraction
import multiplication
import division

print("Please make a choice.  Select from:")
print("1 for add")
print("2 for subtract")
print("3 for multiply")
print("4 for divide")
if True:   
    choice = input("Enter selection(1, 2, 3, 4):")     
    if choice in ('1', '2', '3','4'):           
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))
        if choice == '1':
            print(num1, "+", num2, "=", addition.add(num1,num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtraction.subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplication.multiply(num1, num2))

        elif choice == '4':
            try:
                print(num1, "/", num2, "=", division.divide(num1,num2))
            except ZeroDivisionError:
                print("You cannot divide by zero")  
        else:
            print("Invalid Input")

