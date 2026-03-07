from storage import load_expenses, save_expenses
from tracker import add_expense, list_expenses, show_total, show_category


def show_menu():
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Show Total")
    print("4. Show Category Summary")
    print("5. Exit")
    print(".............................................")

def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice= input("Enter your choice (1-5): ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            show_category(expenses)
        elif choice == "5":
            save_expenses(expenses)
            print("Goodbye!")
            break
        else:
            print("No one to execute")
if __name__ == "__main__":
    main()