p1 = ["35","36","40" ,"44"]
p2 = ["About 55","About 65","About 75","About 85"]

print("Answer the following algebra question : ")

print("If x = 8 , then what is the value of 4(x+3) ?  ")
for i in range(4):
    print((i+1),".",p1[i] )

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
           
print("Estimate this answer (exact calculation not needed) :")
print("Jack scored these marks in 5 math tests : 49,81,72,66 and 52 .What is the mean?")
for j in range(4):
    print((j+1),".",p2[j])

m = int(input("Your choice :"))
if m == 2 :
    print("Bingo")
else:
    print("Try again :(")

print("Your correctly answer 1 out of 2 questiona")



