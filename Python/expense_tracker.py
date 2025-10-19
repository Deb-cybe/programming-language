# File: python/expense_tracker.py
import datetime

def add_expense(expenses):
    item = input("Enter expense name: ")
    amount = float(input("Enter amount spent: "))
    date = datetime.date.today()
    expenses.append({"item": item, "amount": amount, "date": date})
    print(f"Added {item} - ₹{amount} on {date}")

def show_summary(expenses):
    print("\n------ Expense Summary ------")
    total = sum(e["amount"] for e in expenses)
    for e in expenses:
        print(f"{e['date']} | {e['item']} - ₹{e['amount']}")
    print(f"Total Spent: ₹{total}")
    print("------------------------------")

def main():
    expenses = []
    while True:
        print("\n1. Add Expense  2. Show Summary  3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_summary(expenses)
        elif choice == "3":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
