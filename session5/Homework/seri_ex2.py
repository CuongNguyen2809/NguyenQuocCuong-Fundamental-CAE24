prices = {
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}

stock = {
"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}
total = 0
for a in prices:
    print(a)
    print("  price:", prices[a])
    
    for b in stock:
        if b ==a:
            print("  stock: ", stock[b])
        

            
            gia = prices[a] * stock[b]
            total += gia
            
print("Total : " , total)



