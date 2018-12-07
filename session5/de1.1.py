p1 = {
    "Số Phòng" : 1,
    "Số hiệu tòa nhà" : "A1" ,
    "Tên chủ hộ" : "Nguyễn Văn A",
    "Số KW dùng trong tháng" : 110,
    }

p2 = {
    "Số Phòng" : 2,
    "Số hiệu tòa nhà" : "A2" ,
    "Tên chủ hộ" : "Nguyễn Văn B",
    "Số KW dùng trong tháng" : 115,
    }


p3 = {
    "Số Phòng" : 3,
    "Số hiệu tòa nhà" : "A3" ,
    "Tên chủ hộ" : "Nguyễn Văn C",
    "Số KW dùng trong tháng" : 120,
    }

 
p = [p1 ,p2,p3]
print(p)


while True:
    a = int(input("Nhập số phòng : "))
    b = input(" Nhập số hiệu tòa nhà : ")
    c = input("Tên chủ hộ  : ")
    d = int(input("Só KW dùng trong tháng : "))
    if d > 0:
        print("Error")

        new = {
            "Số Phòng" : a,
            "Số hiệu tòa nhà" : b ,
            "Tên chủ hộ" : c,
            "Số KW dùng trong tháng" : d,
            }
        p.append(new)
        print(p)
        break
    else :
        print("Error")
        

