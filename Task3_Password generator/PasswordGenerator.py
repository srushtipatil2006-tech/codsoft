# ============================================================
#  CodSoft Internship - Task 3: PASSWORD GENERATOR
#  Author  : Srushti Patil
#  Language: Python 3
#  Run     : python password_generator.py
#  No extra libraries needed — uses built-in `random` & `string`
# ============================================================

import random
import string

# ---------- Character sets ----------
UPPERCASE = string.ascii_uppercase        # A-Z
LOWERCASE = string.ascii_lowercase        # a-z
DIGITS    = string.digits                 # 0-9
SYMBOLS   = "!@#$%^&*()_+-=[]{}|;:,.<>?" # Special characters

# ---------- Generate one password ----------
def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """
    Generate a random password based on selected character types.
    Guarantees at least one character from each selected type.
    """
    if not any([use_upper, use_lower, use_digits, use_symbols]):
        print("  ⚠️  Please select at least one character type.")
        return None

    # Build the full character pool
    pool = ""
    required_chars = []   # Ensures at least one from each type

    if use_upper:
        pool += UPPERCASE
        required_chars.append(random.choice(UPPERCASE))

    if use_lower:
        pool += LOWERCASE
        required_chars.append(random.choice(LOWERCASE))

    if use_digits:
        pool += DIGITS
        required_chars.append(random.choice(DIGITS))

    if use_symbols:
        pool += SYMBOLS
        required_chars.append(random.choice(SYMBOLS))

    # Fill remaining length from the full pool
    remaining_length = length - len(required_chars)
    if remaining_length < 0:
        # Length is less than number of required types — just use required
        password_chars = required_chars[:length]
    else:
        password_chars = required_chars + [random.choice(pool) for _ in range(remaining_length)]

    # Shuffle to avoid predictable positions (e.g., uppercase always first)
    random.shuffle(password_chars)

    return "".join(password_chars)

# ---------- Check password strength ----------
def check_strength(password):
    """Return strength label and a simple score."""
    score = 0
    has_upper   = any(c in UPPERCASE for c in password)
    has_lower   = any(c in LOWERCASE for c in password)
    has_digit   = any(c in DIGITS    for c in password)
    has_symbol  = any(c in SYMBOLS   for c in password)

    if len(password) >= 8:  score += 1
    if len(password) >= 12: score += 1
    if len(password) >= 16: score += 1
    if has_upper:           score += 1
    if has_lower:           score += 1
    if has_digit:           score += 1
    if has_symbol:          score += 1

    if score <= 2:   return "⚠️  WEAK"
    elif score <= 4: return "🟡 FAIR"
    elif score <= 5: return "🟢 STRONG"
    else:            return "🔒 VERY STRONG"

# ---------- Get a valid integer from user ----------
def get_int(prompt, min_val, max_val):
    while True:
        try:
            val = int(input(prompt))
            if min_val <= val <= max_val:
                return val
            else:
                print(f"  ⚠️  Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("  ⚠️  Invalid input. Please enter a number.")

# ---------- Yes / No input ----------
def yes_no(prompt):
    while True:
        ans = input(prompt + " (y/n): ").strip().lower()
        if ans in ["y", "yes"]:
            return True
        elif ans in ["n", "no"]:
            return False
        else:
            print("  ⚠️  Please enter y or n.")

# ---------- Main generator flow ----------
def run_generator(history):
    print("\n" + "=" * 50)
    print(f"{'🔐  PASSWORD GENERATOR':^50}")
    print("=" * 50)

    # Step 1 — Password length
    length = get_int("  Enter desired password length (6 - 64): ", 6, 64)

    # Step 2 — Character type selection
    print("\n  Select character types to include:")
    use_upper   = yes_no("  Include UPPERCASE letters (A-Z)?")
    use_lower   = yes_no("  Include lowercase letters (a-z)?")
    use_digits  = yes_no("  Include Numbers (0-9)?")
    use_symbols = yes_no("  Include Symbols (!@#$...)?")

    # Step 3 — How many passwords to generate
    count = get_int("\n  How many passwords to generate? (1-10): ", 1, 10)

    print("\n" + "-" * 50)
    print(f"  Generated Password{'s' if count > 1 else ''}:")
    print("-" * 50)

    generated = []
    for i in range(count):
        pwd = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        if pwd:
            strength = check_strength(pwd)
            print(f"  {i+1:2}. {pwd}")
            print(f"      Strength : {strength}")
            print(f"      Length   : {len(pwd)} characters")
            if count > 1 and i < count - 1:
                print()
            generated.append(pwd)
            history.append(pwd)

    print("-" * 50)

    # Step 4 — Let user pick one to "copy" (display prominently)
    if len(generated) > 1:
        pick = get_int(f"\n  Enter number to select a password (1-{len(generated)}): ", 1, len(generated))
        selected = generated[pick - 1]
    elif generated:
        selected = generated[0]
    else:
        return

    print(f"\n  ✅ Selected Password:\n")
    print(f"  >>>  {selected}  <<<\n")
    print("  (Copy the password above manually)")

# ---------- Show history ----------
def show_history(history):
    print("\n" + "-" * 50)
    print(f"{'📜  PASSWORD HISTORY':^50}")
    print("-" * 50)
    if not history:
        print("  No passwords generated yet.")
    else:
        for i, pwd in enumerate(history, 1):
            print(f"  {i:2}. {pwd}  [{check_strength(pwd)}]")
    print("-" * 50)

# ---------- Main menu ----------
def main():
    history = []
    print("\n  Welcome to the Password Generator")
    print("  CodSoft Python Internship - Task 3")

    while True:
        print("\n" + "-" * 40)
        print("  MENU")
        print("  1. Generate Password(s)")
        print("  2. View Password History")
        print("  3. Clear History")
        print("  4. Exit")
        print("-" * 40)

        choice = input("  Choose an option (1-4): ").strip()

        if choice == "1":
            run_generator(history)
        elif choice == "2":
            show_history(history)
        elif choice == "3":
            history.clear()
            print("  🧹 History cleared.")
        elif choice == "4":
            print("\n  👋 Stay secure! Goodbye!\n")
            break
        else:
            print("  ⚠️  Invalid choice. Please enter 1-4.")

# ---------- Entry Point ----------
if __name__ == "__main__":
    main()
