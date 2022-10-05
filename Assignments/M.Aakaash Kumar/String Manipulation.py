i=1
while(i>0):
    print("\n1.Concatenation\n2.Reversal\n3.Slicing with custom positions\n0.Exit\n\n")
    choice = int(input("Enter a choice:"))
    if (choice == 0):
        print("Exit")
        break
    elif (choice > 3):
        print("Invalid choice")
    elif(choice==1):
        a = input("Enter the first string: ")
        b = input("Enter the second string: ")
        print("Contatenation: ")
        print(a + b)
    elif(choice==2):
        a = input("Enter the string for reverse: ")[::-1]
        print(a)
    elif(choice==3):
        string=input("Enter the string for slicing: ")
        start=int(input("Enter the starting character: "))
        end=int(input("Enter the ending character: "))
        print("After slicing: ")
        print(string[start-1:end])