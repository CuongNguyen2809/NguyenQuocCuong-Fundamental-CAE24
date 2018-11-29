print("Type exit to escape ")
while True:
    a = input("Enter your number : ")
    
    if a.isalpha()  :
        print("error")
    elif a.isdigit() :
        print("Digit count : " , len(str(a)))
    if a == "exit":

        break

    

