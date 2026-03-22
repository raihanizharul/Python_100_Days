print("Welcome to the tip calculator")
bill=float(input("What was the total bill? $"))
tip=float(input("How much the tip would you like to give? $10, 13$, 15$ or others? $"))
num_people=int(input("How many people to split the bill? "))

def tip_calculator(bill: float, tip: float, num_people: int) -> float:
    total_amount=(bill+tip)/num_people
    return total_amount

print(f"Total amount to pay is ${tip_calculator(bill,tip,num_people)}")