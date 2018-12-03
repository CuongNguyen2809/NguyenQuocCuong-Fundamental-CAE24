size = [44,56,89,110,45,77,95,115,74,66,69]
print("Hello, my name is Cuong and there are my ship sizes : " )
print(size)
x = 1
for i in range(3):
    print("MONTH ",x)
    x +=1
    a = max(size)
    print("Now my biggest sheep has size",a,"let 's shear it")
    size.remove(max(size))
    size.append(8)
    print("After shearing, here is my flock" )
    print(size)
    b = 0 
    for i in range(len(size)):
        size[b] +=50
        b += 1
    print("One month has passed , now here is my flock")
    print (size)

total = sum(size)
print("My flock has size in total :",total)
t= total * 2
print("I would get",total,"* 2$ =",t,"$")
