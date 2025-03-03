import sys

def calculate_ratios():
    print("Financial Ratio Calculator")
    print("1. Current Ratio")
    print("2. Quick Ratio")
    print("3. Debt-to-Equity Ratio")
    print("4. Return on Assets (ROA)")
    print("5. Return on Equity (ROE)")
    choice = input("Enter the number of the ratio you want to calculate: ")

    if choice == '1':
        current_assets = float(input("Enter current assets: "))
        current_liabilities = float(input("Enter current liabilities: "))
        ratio = current_assets / current_liabilities
        print(f"Current Ratio: {ratio:.2f}")

    elif choice == '2':
        cash = float(input("Enter cash: "))
        accounts_receivable = float(input("Enter accounts receivable: "))
        current_liabilities = float(input("Enter current liabilities: "))
        ratio = (cash + accounts_receivable) / current_liabilities
        print(f"Quick Ratio: {ratio:.2f}")

    elif choice == '3':
        total_liabilities = float(input("Enter total liabilities: "))
        total_equity = float(input("Enter total equity: "))
        ratio = total_liabilities / total_equity
        print(f"Debt-to-Equity Ratio: {ratio:.2f}")

    elif choice == '4':
        net_income = float(input("Enter net income: "))
        total_assets = float(input("Enter total assets: "))
        ratio = net_income / total_assets
        print(f"Return on Assets (ROA): {ratio:.2%}")

    elif choice == '5':
        net_income = float(input("Enter net income: "))
        total_equity = float(input("Enter total equity: "))
        ratio = net_income / total_equity
        print(f"Return on Equity (ROE): {ratio:.2%}")

    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    calculate_ratios()