
def add(a :float, b :float)->float:
    return a+b


def subtract(a :float, b :float)->float:
    return a-b


def multiply(a :float, b :float)->float:
    return a*b


def divide(a :float, b :float)->float:
    try:
        return a/b
    except ZeroDivisionError:
        print("ERROR! " \
        "you can't divide a number by zero")    
    return None


def power(a :float, b :float)->float:
    return a**b


def percentage(a :float, b :float)->float:
    return (a/100)*b


def nth_root(a :float, b :float)->float:
    try:
        if a < 0 and float(b).is_integer() and int(b) % 2 == 0:
            print("Error: Even root of a -ve number is not a real number")
            return None
        else:
            return a**(1/b)
    except ZeroDivisionError:
        print("ERROR: Cannot take zeroth root")   


def show_menu():
    print("""WELCOME TO BASIC CALCULATOR!
SELECT THE NUMBER FOR THE OPERATION YOU WANT TO PERFORM.""")
    print("""
1. ADDITION
2. SUBTRACTION
3. MULTIPLICATION
4. DIVISION
5. POWER
6. n-th ROOT
7. PERCENTAGE """)
    

def get_input():
    while True:
        user_input=input("> ").strip()
        try:
            check=int(user_input)
            if (1<=check<=7):
               return check
            else:
                print("Enter a valid number to perform desired operation!")
                 
        except ValueError: 
            print("Please enter a valid Integer!")   
            continue 

def get_numbers():
    while True:
        num1=input("Enter First Number: ").strip()
        num2=input("Enter Second Number: ").strip()
        try:
            a=float(num1)
            b=float(num2)
            return a, b
        except ValueError:
            print("Please enter valid numbers!")
            continue

operations={
    1: (add, "+"),
    2: (subtract, "-"),
    3: (multiply, "*"),
    4: (divide, "/"),
    5: (power, "^"),
    6: (nth_root, "√"),
    7: (percentage, "%")

}


def calculate():
    choice=get_input()
    a,b =get_numbers()
    func, symbol =operations[choice]

    result=func(a,b)
    
    return a, b, symbol, result


def main():
    show_menu()
    a, b, symbol, result=calculate()
    if result is not None:
        print (f"{a} {symbol} {b} = {result}")


while True:
    main()

    try_again=input("Do you want to use again? (Y/N) ").strip().upper()
    if try_again != "Y":
        print("THANKYOU for using.")
        break

            




        
        
        


    





def history():
    pass


