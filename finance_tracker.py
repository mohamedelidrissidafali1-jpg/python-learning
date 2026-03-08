import csv
import os
from datetime import datetime

# Constants
DATA_FILE = "transactions.csv"
CATEGORIES = ["Food", "Transport", "Entertainment", "Bills", "Salary", "Other"]

# Global data structure
transactions = []

# ============================================
# PART 1: FILE OPERATIONS
# ============================================

def initialize_file():
    """Create CSV file with headers if it doesn't exist"""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Amount", "Description"])
        print("✓ Data file created")


def load_transactions():
    """Load all transactions from file into memory"""
    global transactions
    transactions = []

    if not os.path.exists(DATA_FILE):
        return

    try:
        with open(DATA_FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                transaction = {
                    "date": row["Date"],
                    "type": row["Type"],
                    "category": row["Category"],
                    "amount": float(row["Amount"]),
                    "description": row["Description"]
                }
                transactions.append(transaction)
        print(f"✓ Loaded {len(transactions)} transactions")
    except Exception as e:
        print(f"Error loading transactions: {e}")


def save_transactions():
    """Save all transactions from memory to file"""
    try:
        with open(DATA_FILE, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Amount", "Description"])

            for t in transactions:
                writer.writerow([
                    t["date"],
                    t["type"],
                    t["category"],
                    t["amount"],
                    t["description"]
                ])
        print("✓ Transactions saved")
    except Exception as e:
        print(f"Error saving transactions: {e}")

# ============================================
# PART 2: TRANSACTION MANAGEMENT
# ============================================

def add_transaction(trans_type):
    """Add a new income or expense transaction"""
    print(f"\n=== Add {trans_type} ===")

    print("\nCategories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}. {cat}")

    try:
        cat_choice = int(input("\nChoose category (number): "))
        if cat_choice < 1 or cat_choice > len(CATEGORIES):
            print("Invalid category!")
            return

        category = CATEGORIES[cat_choice - 1]

        amount = float(input("Amount: $"))
        if amount <= 0:
            print("Amount must be positive!")
            return

        description = input("Description: ")

        transaction = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": trans_type,
            "category": category,
            "amount": amount,
            "description": description
        }

        transactions.append(transaction)
        save_transactions()

        print(f"✓ {trans_type} added successfully!")

    except ValueError:
        print("Error: Invalid input!")
    except Exception as e:
        print(f"Error: {e}")


def view_all_transactions():
    """Display all transactions"""
    if len(transactions) == 0:
        print("\nNo transactions yet!")
        return

    print("\n" + "=" * 80)
    print(f"{'Date':<20} {'Type':<10} {'Category':<15} {'Amount':<10} {'Description'}")
    print("=" * 80)

    for t in transactions:
        amount_str = f"${t['amount']:.2f}"
        print(f"{t['date']:<20} {t['type']:<10} {t['category']:<15} {amount_str:<10} {t['description']}")

    print("=" * 80)


def calculate_balance():
    """Calculate and display current balance"""
    total_income = sum(t["amount"] for t in transactions if t["type"] == "Income")
    total_expenses = sum(t["amount"] for t in transactions if t["type"] == "Expense")
    balance = total_income - total_expenses

    print("\n=== Financial Summary ===")
    print(f"Total Income:   ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance:        ${balance:.2f}")

    if balance < 0:
        print("⚠️ Warning: You're spending more than you earn!")
    elif balance > 0:
        print("✓ Good! You're saving money.")

# ============================================
# FEATURE 5: VIEW BY CATEGORY
# ============================================

def view_by_category():
    """Show transactions grouped by category"""

    if len(transactions) == 0:
        print("\nNo transactions yet!")
        return

    print("\n=== Transactions by Category ===")

    for category in CATEGORIES:

        category_transactions = [t for t in transactions if t["category"] == category]

        if len(category_transactions) > 0:

            total = sum(t["amount"] for t in category_transactions)

            print(f"\n{category}: ${total:.2f}")

            for t in category_transactions:
                print(f"  - {t['date']}: ${t['amount']:.2f} ({t['description']})")

# ============================================
# FEATURE 6: MONTHLY SUMMARY
# ============================================

def monthly_summary():
    """Show summary for current month"""

    current_month = datetime.now().strftime("%m")

    monthly_transactions = [
        t for t in transactions if t["date"][5:7] == current_month
    ]

    total_income = sum(
        t["amount"] for t in monthly_transactions if t["type"] == "Income"
    )

    total_expenses = sum(
        t["amount"] for t in monthly_transactions if t["type"] == "Expense"
    )

    balance = total_income - total_expenses

    print("\n=== Monthly Summary ===")

    print(f"Total Income:   ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance:        ${balance:.2f}")

# ============================================
# FEATURE 7: SEARCH TRANSACTIONS
# ============================================

def search_transactions():
    """Search transactions by keyword"""

    print("=== Search Results ===")

    keyword = input("Search transactions: ")

    if keyword == "":
        print("Please enter a search keyword.")
        return

    found = False

    for t in transactions:
        # Check if the search keyword appears in the transaction description (case-insensitive)
        if keyword.lower() in t["description"].lower():

            print(f"{t['date']:<20} {t['type']:<10} {t['category']:<15} ${t['amount']:.2f} {t['description']}")

            found = True

    if not found:
        print("No matching transactions found.")

# ============================================
# MAIN MENU
# ============================================

def display_menu():
    print("\n" + "=" * 50)
    print("       PERSONAL FINANCE TRACKER")
    print("=" * 50)
    print("1.  Add Income")
    print("2.  Add Expense")
    print("3.  View All Transactions")
    print("4.  View Balance")
    print("5.  View by Category")
    print("6.  Monthly Summary")
    print("7.  Search Transactions")
    print("10. Exit")
    print("=" * 50)


def main():

    print("Welcome to Personal Finance Tracker!")

    initialize_file()
    load_transactions()

    while True:

        display_menu()

        choice = input("\nChoice: ")

        if choice == "1":
            add_transaction("Income")

        elif choice == "2":
            add_transaction("Expense")

        elif choice == "3":
            view_all_transactions()

        elif choice == "4":
            calculate_balance()

        elif choice == "5":
            view_by_category()

        elif choice == "6":
            monthly_summary()

        elif choice == "7":
            search_transactions()

        elif choice == "10":
            print("\nSaving data...")
            save_transactions()
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()