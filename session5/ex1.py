p1 = {
    "name" : "Huy",
    "VND per hour" : 20,
    "Hour" : 25
}

p2 = {
    "name" : "Quan",
    "VND per hour" : 30,
    "Hour" : 30
}

p3 = {
    "name" : "Duc",
    "VND per hour" : 25,
    "Hour" : 15
}

p_list = [p1,p2,p3]


wage_list = [p["VND per hour"]*p["Hour"] for p in p_list]
total =sum(wage_list)
print(total)
# print(p_list)
# total = 0
# for p in p_list:
#     s = p["VND per hour"]*p["Hour"]
#     total += s
#     print(p["name"],": ",s)
# print(total)


# for s in p_list:
#     total += s
#     print(total)

# print(p)

# s1 = p1["VND per hour"]*p1["Hour"]
# s2 = p2["VND per hour"]*p2["Hour"]
# s3 = p3["VND per hour"]*p3["Hour"]


# print(p1["name"] , ":" ,s1)
# print(p2["name"] , ":" ,s2)
# print(p3["name"] , ":" ,s3)


# s = s1 +s2 + s3
# print("Tong luong : " , s)
