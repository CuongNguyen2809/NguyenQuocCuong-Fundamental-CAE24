a = int(input(" nhap a : "))
b = int(input(" nhap b : "))
c = int(input(" nhap c : "))
#a(x**2)+b*x+c = 0

delta = (b**2) - 4*a*c
if delta < 0:
    print("PT vo nghiem")
elif delta == 0 :
    print ("PT có 1 nghiệm duy nhat :" , )
    x = (-b)/(2*a)
    print("x= " ,x)
else:
    print ("PT có 2 nghiệm : ")
    x1 = ((-b)+(delta**0.5))/(2*a)

    x2 = ((-b)-(delta**0.5))/(2*a)
    print("x1 = " , x1)
    print("x2 =" , x2)