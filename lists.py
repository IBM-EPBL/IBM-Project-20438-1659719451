a = []
n = int(input("\nEnter the number of values in the list: \n"))
print("\nEnter the values of the list: \n")
for i in range(n):
    a.append(int(input()))
i=1
while(i>0):

    print("\n1.Insert an integer at a position\n2.Print the list\n3.Delete the first element\n4.Append any element"
          "\n5.Sort and display the list\n6.Pop the last element\n7.Reverse and print the list\n0.Exit\n\n")
    choice = int(input("Enter a choice:"))

    if(choice==0):
        print("Exit")
        break
    elif(choice>7):
        print("Invalid choice")
    elif(choice==1):
        position=int(input("\nEnter the position to inserted: "))
        value=int(input("\nEnter the value to be inserted: "))
        a.insert(position-1,value)
        print(a)
    elif(choice==2):
        print(a)
    elif(choice==3):
        a.remove(a[0])
        print(a)
    elif(choice==4):
        a.append(int(input()))
        print(a)
    elif(choice==5):
        a.sort()
        print(a)
    elif(choice==6):
        a.pop()
        print(a)
    elif(choice==7):
        a.reverse()
        print(a)

