# 2.1
size = [44,56,89,110,45,77,95,115,74,66,69]
print("Hello, my name is Cuong and there are my ship sizes : " )
print(size)

#2.2
a = max(size)
print("Now my biggest sheep has size",a,"let 's shear it")

#2.3
size.pop(7)
size.append(8)
print("After shearing, here is my flock" )
print(size)

#2.4
b = 0 
for i in range(len(size)):
    size[b] +=50
    b += 1
print("One month has passed , now here is my flock")
print (size)
