import csv
from datetime import datetime
FILENAME="expenses.csv"
FIELDNAMES=["date","category","description","amount"]
CATEGORIES=["Food","Transport","Study","Entertainment","Health","Other"]

def load_expenses():
    try:
        with open(FILENAME,"r") as f:
            reader=csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(FILENAME,"w",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(expenses)

expenses=load_expenses()

def add_expenses(expenses):
    print("\nSelect category:")
    for i,cat in enumerate(CATEGORIES,1):
        print(f"{i}.{cat}")
    try:
        cat_choice=int(input("Enter number:"))
        if cat_choice<1 or cat_choice>len(CATEGORIES):
            print("❌Invalid choice!")
            return
        category=CATEGORIES[cat_choice-1]
    except ValueError:
        print("❌Enter a number!")
        return
    description=input("Enter description:").strip()
    if not description:
        print("Description can't be empty!")
        return
    try:
        amount=float(input("Enter amount: ₹"))
        if amount<=0:
            print("❌Amount must be positive and greater than zero!")
            return
    except ValueError:
        print("❌ Enter a valid number.")
        return
    date=datetime.today().strftime("%Y-%m-%d")
    expenses.append({"date":date,"category":category,"description":description,"amount":amount})
    save_expenses(expenses)
    print(f"✅ Expenses added! ({date} | {category} | {description} | ₹{amount:.2f})")

def view_expenses(expenses):
    if not expenses:
        print("❌No expenses found!")
        return
    print(f"\n{'#':<4} {'Date':<12} {'Category':<15} {'Description':<20} {'Amount':>8}")
    print("-" * 62)
    for i,exp in enumerate(expenses,1):
        print(f"{i:<4} {exp['date']:<12} {exp['category']:<15} {exp['description']:<20} ₹{float(exp['amount']):>7.2f}")

def view_total(expenses):
    if not expenses:
        print("❌No expenses found!")
        return
    total=sum(float(exp['amount']) for exp in expenses)
    print(f"\n💰 Total spent: ₹{total:.2f}")
 
def view_by_category(expenses):
    if not expenses:
        print("❌No expenses found!")
        return
    category_totals={}
    for exp in expenses:
        cat=exp['category']
        amount=float(exp['amount'])
        if cat in category_totals:
            category_totals[cat]+=amount
        else:
            category_totals[cat]=amount
    print(f"\n{'📊 Category':<20} {'Total':>10}")
    print("-" * 32)
    for cat,total in category_totals.items():
        print(f"{cat:<20} ₹{total:>9.2f}")
    print("-" * 32)
    print(f"{'Total':<20} ₹{sum(category_totals.values()):>9.2f}")   

def delete_expense(expenses):
    if not expenses:
        print("❌No expenses found!")
        return
    view_expenses(expenses)
    try:
        choice=int(input("\nEnter expense number to delete: "))
        if choice<1 or choice>len(expenses):
            print("❌ Invalid number.")
            return
    except ValueError:
        print("❌ Enter a number.")
        return  
    removed=expenses.pop(choice-1)
    save_expenses(expenses)
    print(f"✅ Deleted: {removed['description']} | ₹{float(removed['amount']):.2f}")

while True:
    print("\n====== EXPENSE TRACKER ======")
    print("1. Add expense\n2. View all expenses\n3. View total spent\n4. View spending by category\n5. Delete an expense\n6. Exit")
    print("=============================")
    try:
        choice=int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice! Enter number between 1-6.")
        continue
    if choice == 1:
        add_expenses(expenses)
    elif choice == 2:
        view_expenses(expenses)
    elif choice == 3:
        view_total(expenses)
    elif choice == 4:
        view_by_category(expenses)
    elif choice == 5:
        delete_expense(expenses)
    elif choice == 6:
        print("Goodbye! 👋")
        break
    else:
        print("❌ Invalid choice. Enter number between 1 to 6.")