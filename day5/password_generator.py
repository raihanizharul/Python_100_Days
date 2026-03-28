import random

letters=[
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

symbols=[
    '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '=', '+'
]



print("Welcome to the password generator!")
len_letter=int(input("How many letters would you like in your password?\n"))
total_symbols=int(input("How many symbols would you like?\n"))
total_numbers=int(input("How many numbers would you like?\n"))

random_letters=[random.choice(letters) for x in range(len_letter)]
random_symbols=[random.choice(symbols) for x in range(total_symbols)]
random_numbers=[str(random.randint(0,9)) for x in range(total_numbers)]

password=random_letters+random_symbols+random_numbers
random.shuffle(password)
final_password=""

print(random_letters)
print(random_symbols)
print(random_numbers)

for x in password:
    final_password+=x
    
print(f"Your password:\n{final_password}")
