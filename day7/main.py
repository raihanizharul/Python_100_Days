import random
from hangman_words import word_list

random_words=random.choice(word_list)
print(random_words)

random_words_blank= ["_"] * len(random_words)

lives=6
while lives!=0:
    print(lives)
    print("".join(random_words_blank))
    
    while True:
        user_guess=input("Guess the words:\n").lower()
        if len(user_guess)>len(random_words):
            print("Your input is longer than the words")
        else:
            break
        
    found=False
    for guess in user_guess:
        for i in range(len(random_words)):
            if random_words[i]==guess:
                random_words_blank[i]=guess
                found=True
    if not found:
        lives-=1
        if lives==0:
            print(f"{lives}\nGame Over")
