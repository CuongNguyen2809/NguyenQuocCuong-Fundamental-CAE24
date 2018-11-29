while True: 
    a = input("Guess your number (1 - 100) : ")
    if a.isalpha() or int(a) <1 or int(a) > 100:
        print ("Error")
      
    elif int(a) <= 50:
                    print("Too small :( ")
    elif int(a) >= 52:
                    print("A little too large :( ")
    else  :
        print(" ___Bin go___ ")
        break