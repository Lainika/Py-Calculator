print (

'''
╔═══╗──╔╗──────╔╗───╔╗
║╔═╗║──║║──────║║──╔╝╚╗
║║─╚╬══╣║╔══╦╗╔╣║╔═╩╗╔╬══╦═╗
║║─╔╣╔╗║║║╔═╣║║║║║╔╗║║║╔╗║╔╝
║╚═╝║╔╗║╚╣╚═╣╚╝║╚╣╔╗║╚╣╚╝║║
╚═══╩╝╚╩═╩══╩══╩═╩╝╚╩═╩══╩╝
''') 

#first read this------------\
#                           |
#                           |
#                           /          
#                          √
'''
   print("Your_Calculation")
   print("for_addition : type 'add'")
   print("for_multiplication : 'multiply'")
   print("for_division : 'divide'")
   print("for_subtration :subtract")
   print("for_square_root: root")
   print("for_cancle_processing :'clear'")
'''
print('''
 Type         for action
__________________________________
|'add'       | addition          |
|'multiply'  | multiplication    |
|'divide'    | integer division  |
|'subtract'  | subtract          |
|'root'      | square root       |
|'percentage'| Percentage of 100 |
|'clear'     | cancel            |
----------------------------------
''')

while True:
    user_input = input("What would you like to do? ")

    if user_input == "clear":
        break

    elif user_input == 'add':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = (num1 + num2)
        print(result)

    elif user_input == 'multiply':
        num1 = float(input("Enter the first factor: "))
        num2 = float(input("Enter the second factor: "))
        result = (num1 * num2)
        print(result)

    elif user_input == 'divide':
        num1 = float(input("Enter dividend: "))
        num2 = float(input("Enter divisor: "))
        result = (num1 // num2)
        print(result)

    elif user_input == 'subtract':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = (num1 - num2)
        print(result)

    elif user_input == 'root':
        num1 = float(input("Enter radicand: "))
        result1 = (num1 ** 1 / 2)
        print(result1)

    elif user_input == 'percentage':
        num1 = float(input("Enter number:"))
        result1 = (num1 / 100)
        print(result1)

    else:
        print("Incorrect input please choose one of the above actions.")