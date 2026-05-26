# ============================================================
#  CodSoft Internship - Task 2: CALCULATOR
#  Author  : Srushti Patil
#  Language: Python 3
#  Run     : python calculator.py
# ============================================================

# ---------- Individual operation functions ----------

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the division of a by b. Handles division by zero."""
    if b == 0:
        return None   # Signal error to caller
    return a / b

def modulus(a, b):
    """Return the remainder of a divided by b."""
    if b == 0:
        return None
    return a % b

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

def square_root(a):
    """Return the square root of a. Handles negative input."""
    if a < 0:
        return None   # Cannot take sqrt of negative number
    return a ** 0.5

# ---------- Get a valid number from user ----------
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠️  Invalid input. Please enter a number.")

# ---------- Format result (remove .0 for whole numbers) ----------
def format_result(value):
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, float):
        return round(value, 6)
    return value

# ---------- Display the menu ----------
def show_menu():
    print("\n" + "=" * 45)
    print(f"{'🧮  CALCULATOR':^45}")
    print("=" * 45)
    print("  1.  Addition          ( + )")
    print("  2.  Subtraction       ( - )")
    print("  3.  Multiplication    ( × )")
    print("  4.  Division          ( ÷ )")
    print("  5.  Modulus           ( % )")
    print("  6.  Power / Exponent  ( ^ )")
    print("  7.  Square Root       ( √ )")
    print("  8.  View History")
    print("  9.  Clear History")
    print("  0.  Exit")
    print("=" * 45)

# ---------- Perform calculation ----------
def perform_calculation(choice, history):
    if choice in ["1", "2", "3", "4", "5", "6"]:
        a = get_number("  Enter first number  : ")
        b = get_number("  Enter second number : ")

        if choice == "1":
            result = add(a, b)
            expr   = f"{format_result(a)} + {format_result(b)}"
        elif choice == "2":
            result = subtract(a, b)
            expr   = f"{format_result(a)} - {format_result(b)}"
        elif choice == "3":
            result = multiply(a, b)
            expr   = f"{format_result(a)} × {format_result(b)}"
        elif choice == "4":
            result = divide(a, b)
            expr   = f"{format_result(a)} ÷ {format_result(b)}"
        elif choice == "5":
            result = modulus(a, b)
            expr   = f"{format_result(a)} % {format_result(b)}"
        elif choice == "6":
            result = power(a, b)
            expr   = f"{format_result(a)} ^ {format_result(b)}"

        if result is None:
            print("  ❌ Error: Cannot divide by zero!")
            return
        formatted = format_result(result)
        print(f"\n  📊 Result: {expr} = {formatted}")
        history.append(f"{expr} = {formatted}")

    elif choice == "7":
        a = get_number("  Enter number: ")
        result = square_root(a)
        if result is None:
            print("  ❌ Error: Cannot calculate square root of a negative number!")
            return
        formatted = format_result(result)
        print(f"\n  📊 Result: √{format_result(a)} = {formatted}")
        history.append(f"√{format_result(a)} = {formatted}")

# ---------- Show calculation history ----------
def show_history(history):
    print("\n" + "-" * 45)
    print(f"{'📜  CALCULATION HISTORY':^45}")
    print("-" * 45)
    if not history:
        print("  No calculations yet.")
    else:
        for i, entry in enumerate(history, 1):
            print(f"  {i:2}. {entry}")
    print("-" * 45)

# ---------- Main ----------
def main():
    history = []
    print("\n  Welcome to the Calculator App")
    print("  CodSoft Python Internship - Task 2")

    while True:
        show_menu()
        choice = input("  Choose an option (0-9): ").strip()

        if choice == "0":
            print("\n  👋 Thanks for using the Calculator!\n")
            break
        elif choice in ["1", "2", "3", "4", "5", "6", "7"]:
            perform_calculation(choice, history)
            # Ask if user wants to continue or go back to menu
            again = input("\n  Perform another calculation? (y/n): ").strip().lower()
            if again != "y":
                print("\n  👋 Thanks for using the Calculator!\n")
                break
        elif choice == "8":
            show_history(history)
        elif choice == "9":
            history.clear()
            print("  🧹 History cleared.")
        else:
            print("  ⚠️  Invalid choice. Please enter 0-9.")

# ---------- Entry Point ----------
if __name__ == "__main__":
    main()
