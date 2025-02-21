print('Welcome to semicolon Expense Tracker App')
print('===========================================')

expense = []

print('1. Add on expense')
print('2. View all expense')
print('3. Calculate Total ExpenseExpense')
print('4. Exit')

value = int(input('Enter your choice: '))

while value not in range(1, 5):

	print('Invalid input')

	value = int(input('Enter your choice: '))

while True:

	if value == 1:

		date = input('Enter date(yyyy-mm-dd): ')

		description = input('Enter description: ')

		amount = input('Enter amount: ')

		expense.append({'date': date, 'description': description ,'amount': amount} )

		print('Expenses added')

		print('1. Add on expense')
		print('2. View all expense')
		print('3. Calculate Total ExpenseExpense')
		print('4. Exit')

		value = int(input('Enter your choice: '))

	elif value == 2:

		for expenses in expense:

			print(f"Date: {expenses['date']}, Description: {expenses['description']}, Amount: {expenses['amount']}")

		print('1. Add on expense')
		print('2. View all expense')
		print('3. Calculate Total ExpenseExpense')
		print('4. Exit')

		value = int(input('Enter your choice: '))

	elif value == 3:

		total = 0

		for amount in expense:
			
			total += int(amount['amount'])

		print(f"Total Expenses : {total}")

		print('1. Add on expense')
		print('2. View all expense')
		print('3. Calculate Total ExpenseExpense')
		print('4. Exit')

		value = int(input('Enter your choice: '))

	elif value == 4:

		print('Exiting the App,Goodbye')

		break
			
	
		
		
			
		