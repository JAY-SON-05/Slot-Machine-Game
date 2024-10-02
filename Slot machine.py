import random  # for random values

MAX_LINES = 3 #use this as constant for betting
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#it for a slot that will be random
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

#it will be like a person bet on 1 line then it will be 1st line and accordingly 2 means next 2 lines and all

def check_winnings(columns, lines , bet , values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line] #chcek what is in the 1st row
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check: #checking the symbols are not the same
                break
        else:
            winnings += values[symbol]  * bet  #if all are the same then user won
                    #bet is on each line not on total
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol ,symbol_count in symbols.items():  #items function used to call all the key and the value from dict.
        for  _ in  range (symbol_count):
            all_symbols.append(symbol)

#this is how items we generate in slot machine
    columns = []  #"_" it is an anonymous variable
    for _ in range(cols): #it will generate  3 cols in it
        column = [] #it will pick value randomly for each row
        current_symbols = all_symbols[:] # ":" is a slice opertaor to copy the list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns): #we will transpose here the matrix type
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):  #using enumerate to get index while iterating
            if i != len(columns) - 1:
                print(column[row], end = "  |  ")
            else:
                print(column[row] , end = "")

        print()


#Making a  def function to use it continously
def deposit():
    while True:#using while coz we don't know how many time a user will make mistake while entering the value
        #amount = int(input("What Would you like to deposit? $"))  OR
            amount = input("What Would you like to deposit? $")
            if amount.isdigit():
                amount = int(amount)
                if amount > 0 :
                    break
                else :
                    print("Amount must be greater than 0")
            else:
                print("please Enter a valid number.")

    return amount

def get_number_of_lines():
    while True: #we converted str max lines coz it can be changed so it will updated auto...ly
        lines = input("Enter the no. of lines bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid no. of lines ")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("What Would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:  #using "f" for making use of {} for any value that is stored in it
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("please Enter a valid number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough amount , your current balance is : ${balance}")
        else:
            break

    print(f"You are betting ${bet} on ${lines} lines. Total bet is equal to : ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines :", *winning_lines)
    return winnings - total_bet   #it will deduct the balance


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)   #it will update the balance

    print(f"You left with  ${balance}")
main()


