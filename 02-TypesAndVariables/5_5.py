original_price = input("Enter the original price of the item: ")
discount_percentage = input("Enter the discount percentage: ")
original_price_float = float(original_price)
discount_percentage_float = float(discount_percentage)
discount_amount = original_price_float * (discount_percentage_float / 100)
final_price = original_price_float - discount_amount
print(f'Discount amount: {discount_amount:.2f}')
print(f'Final price: {final_price:.2f}')