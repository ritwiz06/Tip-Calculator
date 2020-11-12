#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))
tip_math=1 + (percent_tip)/100
final_amt=(bill/no_of_people) * tip_math
tip=round(final_amt, 2)
tip="%.2f" % tip
#or
tip = "{:.2f}".format(float(tip))
print(f"Each person should pay: ${tip}")