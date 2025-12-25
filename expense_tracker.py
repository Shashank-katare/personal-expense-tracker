expenses = []
def add_expense():
    name = input("Enter expense name: ")
    amount = int(input("Enter expense amount: "))
    expense = {
        "name" : name,
        "amount" : amount
    }
    expenses.append(expense)
    print("Expenses added successfully")
def view_expense():
    if not expenses:
        print("No record found")
    else:
        for i , expense in enumerate(expenses, start = 1):
            print(f"\nexpense{i}")
            print("name:", expense["name"])
            print("amount:", expense["amount"])
def view_total_expense():
    if not expenses:
        print("No expenses found")
    else:
        total = 0
        for expense in expenses:
            total = total + expense["amount"]
        print("Total expenses: ", total)  
def save_expense():
     with open("expenses.txt", "w") as f:
         for expense in expenses:
             line = f"{expense["name"]},{expense["amount"]}\n"
             f.write(line)
         print("File saved successfully")    
             
    
def show_menu():
    print("\n---Personal Expense Tracker---")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. View Total Expense")
    print("4. Exit")
while True:
    try:
        show_menu()
        choice = int(input("Enter you input: "))
        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expense()
        elif choice == 3:
            view_total_expense()
        elif choice == 4:
            save_expense()
            print("Existing program")
            break
        else:
            print("Invalid choice")
    except ValueError:
        print("print enter a number only")