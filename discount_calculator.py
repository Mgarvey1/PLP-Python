def calculate_discount(price, discount_percent):
#Check if discount is 20% or higher 
 if discount_percent >= 20:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price
 else:
    #If discount < 20%, return original price
    return price
 

# Prompt user for input 
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print result
if discount_percent >=20:
  print("Final price after discount:", final_price)
else:
  print("No discount applied. Final price:", final_price)  