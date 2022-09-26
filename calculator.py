import numpy
i=1
while(i>0):
    print("\nWelcome to the calculator: ")
    print("\nSelect an operation: \n\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Square\n6.Cube\n7.Square root\n8.Cube root\n\n")
    choice = int(input("Enter a choice:"))
    if (choice == 0):
        print("Exit")
        break
    elif (choice > 8):
        print("Invalid choice\n\n")
    elif(1<=choice<=4):
        a=int(input("Enter the First number: "))
        b=int(input("Enter the Second number: "))
        print("Result:\n")
        if(choice==1):
            print(a+b)
        elif(choice==2):
            print(a-b)
        elif(choice==3):
            print(a*b)
        elif(choice==4):
            print(a/b)
    elif(5<=choice<=8):
        a=float(input("Enter the number:"))
        print("Result:\n")
        if(choice==5):
            print(a*a)
        if(choice==6):
            print(a*a*a)
        if(choice==7):
            print(numpy.sqrt(a))
        if(choice==8):
            print(numpy.cbrt(a))


