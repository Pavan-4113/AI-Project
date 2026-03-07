from datetime import date
from tabulate import tabulate

def add_expense(expenses):
    """Ask user details and add a new expense dictionary into the list."""
    print("Add a new expense.......", expenses)

    amount = input("Enter amount: ").strip()
    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    if not amount:
        print("Amount is required. Expense not added.")
        return
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Expense not added.")
        return
    if amount <= 0:
        print("Amount must be positive. Expense not added.")
        return
    if not category:
        print("Category is required. Expense not added.")
        return
    
    expense = {
        "date": str(date.today()),
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)
    print("Expense Added Successfully!")


def list_expenses(expenses):
    """Display all expenses in a tabular format."""
    print("/n All Expenses.......", expenses)
    if not expenses:
        print("No expenses to display.")
        return
    rows = []
    for e in expenses:
        rows.append([e["date"], e["amount"], e["category"], e["description"]])
    print(tabulate(rows,headers=["Date", "Amount", "Category", "Description"], tablefmt="grid"))


def show_total(expenses):
    """Display the total amount of all expenses."""
    total = 0
    for e in expenses:
        total += float(e["amount"])
    print(f"Total Amount: {total:.2f}")

def show_category(expenses):
    print("/n summary......")
    if not expenses:
        print("no expenses to display")
        return
    category_summary = {}
    for e in expenses:
        cat = e["category"]
        sum = float(e["amount"])
        category_summary[cat] = category_summary.get(cat, 0.0) + sum

    rows = []
    for cat, sum in category_summary.items():
            rows.append([cat, f"{sum:.2f}"])
    print(tabulate(rows, headers=["Category", "Total Amount"], tablefmt="grid"))