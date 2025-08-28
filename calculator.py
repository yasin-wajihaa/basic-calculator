"""
calculator.py
-------------
A simple command-line calculator with history support.

Features:
- Addition, subtraction, multiplication, division
- Power, n-th root, percentage
- Keeps the last 10 operations in history
"""

from collections import deque

# Store history of last 10 calculations
history = deque(maxlen=10)


# ---------- BASIC OPERATIONS ----------
def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference (a - b)."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float | None:
    """Return the division (a / b). Handle division by zero safely."""
    try:
        return a / b
    except ZeroDivisionError:
        print("ERROR! You can't divide a number by zero.")
        return None


def power(a: float, b: float) -> float:
    """Return a raised to the power of b."""
    return a ** b


def percentage(a: float, b: float) -> float:
    """Return 'a percent of b' => (a/100) * b."""
    return (a / 100) * b


def nth_root(a: float, b: float) -> float | None:
    """
    Return the b-th root of a.
    Handles invalid cases:
    - Zeroth root
    - Even root of a negative number
    """
    try:
        if a < 0 and float(b).is_integer() and int(b) % 2 == 0:
            print("ERROR: Even root of a negative number is not real.")
            return None
        return a ** (1 / b)
    except ZeroDivisionError:
        print("ERROR: Cannot take zeroth root.")
        return None


# ---------- USER INTERFACE ----------
def show_menu() -> None:
    """Display the menu of operations."""
    print("\nWELCOME TO BASIC CALCULATOR!")
    print("SELECT THE NUMBER FOR THE OPERATION YOU WANT TO PERFORM.\n")
    print("""
0. HISTORY          
1. ADDITION
2. SUBTRACTION
3. MULTIPLICATION
4. DIVISION
5. POWER
6. n-th ROOT
7. PERCENTAGE
""")


def get_input() -> int:
    """Get and validate user's choice of operation."""
    while True:
        user_input = input("> ").strip()
        try:
            choice = int(user_input)
            if 0 <= choice <= 7:
                return choice
            print("Enter a valid number between 0 and 7!")
        except ValueError:
            print("Please enter a valid integer!")


def get_numbers() -> tuple[float, float]:
    """Get two numbers from the user and return them as floats."""
    while True:
        num1 = input("Enter First Number: ").strip()
        num2 = input("Enter Second Number: ").strip()
        try:
            return float(num1), float(num2)
        except ValueError:
            print("Please enter valid numbers!")


# ---------- CALCULATION LOGIC ----------
operations = {
    1: (add, "+"),
    2: (subtract, "-"),
    3: (multiply, "*"),
    4: (divide, "/"),
    5: (power, "^"),
    6: (nth_root, "√"),
    7: (percentage, "%")
}


def show_history() -> None:
    """Display the last 10 calculations."""
    if not history:
        print("NO HISTORY YET.")
    else:
        print("\n--- CALCULATION HISTORY ---")
        for i, h in enumerate(history, start=1):
            print(f"{i}. {h}")


def calculate(choice: int):
    """Perform the chosen operation and record it in history."""
    a, b = get_numbers()
    func, symbol = operations[choice]
    result = func(a, b)
    history.append(f"{a} {symbol} {b} = {result}")
    return a, b, symbol, result


def main():
    """Main control function for calculator workflow."""
    show_menu()
    choice = get_input()

    if choice == 0:
        show_history()
        return

    a, b, symbol, result = calculate(choice)
    if result is not None:
        print(f"{a} {symbol} {b} = {result}")


# ---------- PROGRAM ENTRY ----------
if __name__ == "__main__":
    while True:
        main()
        try_again = input("Do you want to use again? (Y/N) ").strip().upper()
        if try_again != "Y":
            print("THANK YOU for using.")
            break
