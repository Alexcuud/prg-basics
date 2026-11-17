###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')
first= phone[0:3]
sekond= phone[4:7]
third= phone[6:9]
print(f'Your phone number is: {first}-{sekond}-{third}')
...