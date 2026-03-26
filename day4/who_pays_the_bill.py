import random

people=["Asep","Budi","Wawan","Cecep","Kusnadi"]

#random pick using choice
who_pays=random.choice(people)
print(who_pays)

#random pick using index lists
rand_index=random.randint(0,4)
print(people[rand_index])