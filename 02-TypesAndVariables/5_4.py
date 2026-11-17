amount = input('Enter the amount of money: ')
int_amount = float(amount)
vat = 0.23
sum_vat = int_amount * vat

print(f'Amount : {int_amount:.2f}')
print(f'VAT 23% : {sum_vat:.2f}')