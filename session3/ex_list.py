items = ["ga" , "cho" , "meo"]
print(*items)
n = input("Name one thing you want to add")
items.append(n)
print(*items, sep=",")