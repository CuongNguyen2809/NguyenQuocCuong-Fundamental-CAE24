items = ["T-Shirt" , "Sweater" ]
a = input("Welcome to our shop, what do you want  (C , R , U , D) ?  : ").upper()
if a == "C":
    b = input("Enter new item ? : ")
    items.append(b)
    print("Our item: ",items)
elif a == "R":
    print(items)
elif a == "U" :
    c = int(input("Update position : "))
    c1 = input("New item ? : ")
    items[c-1] = c1
    print("Our item : ",items)

elif a == "D":
    d = int(input("Delete position : "))
    items.pop(d-1)
    print("Our item : ",items)