from random import randint

word = "hexagon"
characters = list(word)
print(word)
print(characters)
for _ in range(len(characters)):
    i = randint(0,len(characters)-1)
    ch = characters[i]
    print(ch , end="")
    characters.pop(i)

print()

user_guess = input("Your guess : ")
if user_guess == word :
    print("Hura")
else:
    print(" :(( ")