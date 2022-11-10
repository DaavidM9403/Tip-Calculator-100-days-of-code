print("TIP CALCULATOR")
print()
myBill = float(input("Total of the bill?:"))
groupOfPeople = int(input("How many people where there?:"))
tip = float(input("How much would you like to tip?:"))
answer = myBill / groupOfPeople
tip_total =  myBill * tip
final_answer_2 = myBill + tip_total

print("We are all paying",round(answer, 2), "each")
print("The total of everthing will be", round(final_answer_2, 2))