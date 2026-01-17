while True:

   u = input('Type "go" to start: ').lower()

   if not 'go' in u:
      print('Error. Try again.')
      break

   else: 
         
       print('Hello! I will be your virtual assistant. Below are your options. How can I help you?')
       print()
       print('1 - Account balance')
       print('2 - Make a deposit')
       print('3 - Make a payment')
       print('4 - Take out a loan')
       print('5 - End service')
       print()   

   while True:
       user = input('Choice: ')
 
       if user.isdigit():
        
        if int(user) == 5: 
            print('Service ended. Thank you for choosing us!')
            break
        elif int(user) == 1: 
             print('Your current balance is: $ 1049.00')

        elif int(user) == 2:             
             num = input('Enter the bank account number: ')
             value = input('Enter the desired amount: ')

             if not num.isdigit() or not value.isdigit():
                print('Something went wrong. Try again.')
             else:
                print(f'Deposit of {value} successfully made to account {num}')

        elif int(user) == 3:
            
             print('Pic Pay')
             print('Credit Card')
             print('Invoice/Boleto')
             pay = input('Enter the payment method: ')

        elif int(user) == 4:
            insert = input('Enter the loan amount: ')
            if not insert.isdigit():
                print('Something went wrong. Try again.')
            else:
                print(f'Loan of ${insert}.00 successfully completed.')
