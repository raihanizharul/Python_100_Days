import random
from hangman_words import word_list

random_words=random.choice(word_list)
print(random_words)

random_words_blank= ["_"] * len(random_words)

print("".join(random_words_blank))
user_guess=input("Guess the words:\n").lower()

for guess in user_guess:
    for i in range(len(random_words)):
        if random_words[i]==guess:
            random_words_blank[i]=guess

print("".join(random_words_blank))
