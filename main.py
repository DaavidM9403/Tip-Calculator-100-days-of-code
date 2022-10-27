print("TIP CALCULATOR")
print()
myBill = float(input("Total of the bill?:"))
groupOfPeople = int(input("How many people where there?:"))
tip = float(input("How much would you like to tip?:"))
answer = myBill / groupOfPeople
final_answer =  myBill * tip

print("We are all paying",round(answer), "each")
print("we are splitting a tip of", final_answer)