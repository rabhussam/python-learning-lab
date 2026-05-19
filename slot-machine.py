import random

def spin_row():
    symbols = ['🪙', '💎', '💵', '💰']
    return[random.choice(symbols)for _ in range(3)]
def print_row(row):
    print(" | ".join(row))
def get_payout(row , bet):          # THIS IS JUST SO THE FUNCTION RECOGNIZES THESE VARIABLES
    if row[0] == row[1] == row[2]:
        if row[0] == '🪙':
            return bet * 7
        elif row[0] == '💎':
            return bet * 100
        elif row[0] == '💰':
            return bet * 5
        elif row[0] == '💵':
            return bet * 3  # WHEN PYTHON READS A RETURN IT EXITS THE FUNCTION!!
    return 0
def main():
    balance = 100

    print("*********************")
    print("WELCOME TO THE CASINO")
    print("SYMBOLS: 🪙 💎 💵 💰")
    print("*********************")

    while balance > 0:
        bet = input("How much would you like to bet: ")

        if not bet.isdigit():
            print("Please enter a number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("INSUFFICIENT FUNDS")
            continue

        if bet <= 0:
            print("Error")
            continue

        balance -= bet

        row = spin_row()
        print_row(row)
        payout = get_payout(row, bet)
        if payout > 0:
            print("YOU WON!")
        else:
            print("YOU LOST!")
        balance+= payout
        print(f"YOUR BALANCE IS {balance}")

        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again == 'y':
            continue
        else:
            break

main()
