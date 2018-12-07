person = {
    "name" : "H.Duc",
    "age"   : 25,
    "city" : "Ha Noi",
    "book" :["Sapiens","Tam Quoc","Tieu ngao giang ho"]
}


print(person["name"])
print(person["book"])
# books = person["book"]
# print(books)
for b in person["book"]:
    print(b)

print(person["book"][1])

# print(books[-1])


# for x in person:
#     print(x, person[x])

# for v in person.values():
#     print(v)

# for k,v in person.items():
#     print(k,v)