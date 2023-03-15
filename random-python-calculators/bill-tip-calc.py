# Receiving input for bill amount as a floating point number
bill_amount = float(input("Bill amount: ")) 

# Receiving input for the tip percentage as a floating point number
tip_percentage = float(input("Tip percentage: "))

# Receiving the input for the number of people as an integer
number_of_people = int(input("Number of people: "))

tip_amount = bill_amount * tip_percentage / 100

# Calculating each person's bill contribution
bill_contribution = bill_amount / number_of_people

# Calculating each person's tip contribution
tip_contribution = tip_amount / number_of_people

total_contribution = bill_contribution + tip_contribution

# Displaying the results
print("Bill contribution per person: ", bill_contribution)
print("Tip contribution per person: ", tip_contribution)
print("Total contribution per person: ", total_contribution)