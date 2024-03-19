print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

bill_per_person = (bill + (tip / 100 * bill) ) / people
final_amount = "{:.2f}".format(bill_per_person)

# print(f"Each person should pay: ${round(final_amount, 2)}")

print(f"Each person should pay: ${final_amount}")