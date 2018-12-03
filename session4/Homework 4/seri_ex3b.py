from random import randint

word = ['champion' , 'meticulous' ,'hexagon']

i = randint(0 ,len(word)-1)
a = word[i]
characters = list(a)

for _ in range(len(characters)):
    j = randint (0, len(characters)-1)
    ch = characters[j]
    print(ch, end =" ")
    characters.pop(j)

print()

user_guess = input("Your answer: ")
if user_guess == word:
    print("Hura")
else:
    print(":(")

