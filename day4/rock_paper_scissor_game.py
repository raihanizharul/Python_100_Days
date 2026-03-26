import random

def rock():
    return """
        _______
    ---'     ____)
            (_____)
            (_____)
            (____)
    ---.__ (___)
    """
def paper():
    return """
        _______
    ---'    ____)____
                ______)
               _______)
             _______)
    ---.__________)
    """
def scissor():
    return """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
rand_index=[0,1,2]
user_input=int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissor.\n"))
print("Yours:")
if user_input==0:
    print(rock())
    print("Rock")
    
elif user_input==1:
    print(paper())
    print("Paper")
    
elif user_input==2:
    print(scissor())
    print("Scissor")

print("")    
comp_input=random.choice(rand_index)
print("Computer:")
if comp_input==0:
    print(rock())
    print("Rock")
    
elif comp_input==1:
    print(paper())
    print("Paper")
    
elif comp_input==2:
    print(scissor())
    print("Scissor")

print("")    
if user_input==comp_input:
    print("Tied")
elif user_input==0 and comp_input==1:
    print("You Lose...")
elif user_input==0 and comp_input==2:
    print("You Win!")
elif user_input==1 and comp_input==0:
    print("You Win!")
elif user_input==1 and comp_input==2:
    print("You Lose...")
elif user_input==2 and comp_input==0:
    print("You Lose...")
elif user_input==2 and comp_input==1:
    print("You Win!")
else:
    print("Wrong number, you're disqualified")