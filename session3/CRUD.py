# C : Create R : Read U : Update D : Delete

items = ["ga" , "cho" , " meo" , " ho"]
a = input("Ban muon gi (C , R , U , D) ?  : ").upper()
if a == "C":
    b = input("Ban muon them gi ? : ")
    items.append(b)
    print(items)
elif a == "R":
    print(items)
elif a == "U" :
    c = int(input("Vi tri ban muon sua  ? : "))
    c1 = input("Ban muon sua gi ? :")
    items[c-1] = c1
    print(items)

elif a == "D":
    d = int(input("Vi tri ban muon xoa ? : "))
    items.pop(d-1)
    print(items)


   

