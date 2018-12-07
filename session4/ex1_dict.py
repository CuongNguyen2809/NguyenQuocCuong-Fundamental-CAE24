# 1. read file => str
# f = open("data.json")
# text = f.read()
# 2.Loads, parse , str => dict
import json


word = {
    "hi" : "Xin chào",
    "star" : "Ngôi sao" ,
    "eye" : "Mắt" ,
    "word" : "Từ" ,
    "cat" : "Con mèo",
    "dog" : "Con chó",
    "chicken" : "Con gà",
    "tiger" : "Hổ"
}
while True:
    print(*word)
    n = input ("What word you want translate : ")
    print(word[n])

    # update = input("Do you want to update (Y?N) : ").upper()
    
    # if update =="Y":
    #     new_translation = input("Your translation : ")
    #     word[n] = new_translation
    #     print("Done")
    # else:
    #     print("Not found")
        
    create = input("Do you want to contribute (Y/N) :").upper()
    if create == "Y":
        new_word = input("New Word :")
        new_tranlation = input("Your translation : ")
        word[new_word] = new_tranlation
        print("Done")


