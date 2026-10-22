import random

# plans. 1. add chips into the spin. playet starts with 50 chips, player can chose how much to gamble. 2. make it into tkinter.

#YELLOW = "\033[33m"
#BLUE = "\033[34m"
#RED = "\033[31m"
#GREEN = "\033[32m"
#RESET = "\033[0m" 

red = (1, 3, 5, 7, 9,
12, 14, 16, 18,
19, 21, 23, 25, 27,
30, 32, 34, 36,)


black = (2, 4, 6, 8, 10,
11, 13, 15, 17,
20, 22, 24, 26, 28,
29, 31, 33, 35)

green = (0,)


def spin():
        
    # chips for gambling
    chips = 50

    while chips > 0:
        print(f"\nyou have {chips} chips to use\n")
        bet = int(input("amount here: "))
            
        if bet <= 0 or bet > chips:
            print(f"broke boi, you have {chips} chips")
            continue

        r = random.randint(0, 36) #roulette

        if r in red:
            c = "red"
        elif r in black:
            c = "black"
        else:
            c = "green"

        # chose a color or a number
        choice = int(input("\n\npress 1 to chose a number, press 2 to chose a color: "))

        if choice == 1:
            un = int(input("chose a number between 0 to 36: ")) #user number
            if un == r:
                winnings = bet * 35
                chips += winnings
                print(f"\n\nJackpot! {r} was the winning number! \n\nyou won {winnings}")
            else:
                chips -= bet
                print(f"\n\nsorry the winning number was {r}.\n\nyou lost {bet} chips.")

        #color roulette
        
        elif choice == 2:
            uc = input("\nchoose a color (red/black/green): ").lower()
            if uc == c:
               if c == "green":
                winnings = bet * 2
                chips += winnings
                print(f"\n\nyou won on {c}, you won {winnings} chips.")
               else:
                winnings = bet
                chips += winnings
                print(f"\n\nyou won on {c}, you won {winnings} chips")
            else:
                chips -= bet
                print(f"\n\nyou lost {bet} chips, the winning color was {c}")

spin()