loop = True
while loop:
    pas = input("Enter your password : ")
    if (not pas.islower()) and (not pas.isupper()):
        loop = False 

print("Welcome")
