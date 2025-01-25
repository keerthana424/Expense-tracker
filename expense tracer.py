import json

# Define a function to add an expense
def add_expense(expenses):
    description = input("Enter the description of the expense: ")
    amount = float(input("Enter the amount: "))
    
    expense = {
        'description': description,
        'amount': amount
    }
    
    expenses.append(expense)
    print(f"Expense '{description}' of amount {amount} added successfully!")

# Define a function to view all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    else:
        print("\nYour recorded expenses:")
        for expense in expenses:
            print(f"Description: {expense['description']}, Amount: {expense['amount']}")
        
        total = sum(expense['amount'] for expense in expenses)
        print(f"\nTotal Expenses: {total}")

# Define a function to save the expenses to a file
def save_expenses(expenses, filename):
    with open(filename, 'w') as file:
        json.dump(expenses, file)
    print("Expenses saved successfully!")

# Define a function to load the expenses from a file
def load_expenses(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("No saved expenses found, starting with an empty list.")
        return []

# Main function
def expense_tracker():
    expenses = load_expenses('expenses.json')  # Load expenses from a file
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            save_expenses(expenses, 'expenses.json')  # Save expenses before exiting
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the app
if _name_ == "_main_":
    expense_tracker()