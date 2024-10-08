print("Welcome to Bill Split Calculator")
bill=float(input("What is the Bill amount?\n"))
tip=int(input("How much would you like to tip?\n"))
person=int(input("How many person does acomapny including you?\n"))
final_bill=float(bill + tip)
split=final_bill/person
final_split=round(split,2)
print(f"Total bill for Each Person is : {final_split}")