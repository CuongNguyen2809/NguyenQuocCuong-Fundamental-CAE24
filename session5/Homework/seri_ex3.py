p = ["35","36","40" ,"44"]

print("Answer the following algebra question : ")
print("If x = 8 , then what is the value of 4(x+3) ?  ")
for i in range(4):
    print((i+1),".",p[i] )

n = int(input("Your choice : "))
if n<0:
        print("Error")
elif n>4:
        print("Error")
else:
    if n == 1:
            print("Try again :(")
    elif n == 2:
            print("Try again :(")
    elif n == 3:
            print("Try again :(")
    elif n == 4 :
            print("Bingo")
           



