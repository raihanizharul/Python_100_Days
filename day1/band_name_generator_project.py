'''
 This is a simple band name generator project. 
 It takes the city you grew up in and your pet's name to create a unique band name. 
'''
print("Welcome to the Band Name Generator.")
print("What's the name of the city you grew up in?")
city = str(input())
print("What's your pet's name?")
pet = str(input())
print(f"Your band name could be {city+" "+pet}")