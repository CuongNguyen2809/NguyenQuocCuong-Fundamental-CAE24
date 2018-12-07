items = ["death note" , "netflix" , "teaching"]
print(items)
n = int(input("Position you want to update ? : "))
if n < -3 or n >2 :
    print ("Nhap sai. Vui long nhap lai ")
print (n)
m = input("Your replacing favorite ? : ")
print (m)
items[n-1] = m
print(items)