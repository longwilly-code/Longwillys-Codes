import random
import tkinter as tk
import math



#--Global--

ball_rotation = 0



# --- Game Logic ---
class RouletteGame:
    
    def __init__(self):
        self.chips = 50

        self.red = {
            1,3,5,7,9,12,14,16,18,19,
            21,23,25,27,30,32,34,36
        }

        self.black = {
            2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35
        }

        self.row1 = {
            1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34
        }

        self.row2 = {
            2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35
        }

        self.row3 = {
            3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36
        }

        self.odds = {
            1, 3, 5, 7, 9,
            11, 13, 15, 17,
            19, 21, 23, 25,
            27, 29, 31, 33, 35
        }

        self.evens = {
            2, 4, 6, 8, 10,
            12, 14, 16, 18,
            20, 22, 24, 26,
            28, 30, 32, 34, 36
        }


        self.first_twelfth = {
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
        }

        self.second_twelfth = {
            13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24
        }

        self.third_twelfth = {
            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36
        }
    

    def spin(self):
        return random.randint(0, 36)


    def place_bet(self, amount):
        if amount > self.chips:
            return False
        
        self.chips -= amount
        
        if self.chips == 0:
            self.chips = 10

        return True
    
        
    

    def win(self, multiplier, bet):
        self.chips += bet * multiplier


    # Red/Black logic
    def bet_color(self, bet, color):
        if not self.place_bet(bet):
            return None, False
        
        spin = self.spin()

        if (color == "red" and spin in self.red) or (color == "black" and spin in self.black):
            self.win(2, bet)
            return spin, True
        return spin, False
    

    def row_bet(self, bet, row):
        if not self.place_bet(bet):
            return None, False
        
        spin = self.spin()

        if (row == "1st" and spin in self.row1) or (row == "2nd" and spin in self.row2) or (row == "3rd" and spin in self.row3):
            self.win(2, bet)
            return spin, True
        return spin, False
    
    def odds_and_even_bet(self, bet, odds_or_evens):
        if not self.place_bet(bet):
            return None, False
        
        spin = self.spin()

        if (odds_or_evens == "odds" and spin in self.odds) or (odds_or_evens == "evens" and spin in self.evens):
            self.win(2, bet)
            return spin, True
        return spin, False
    

    def twelfths_bet(self, bet, twelfth):
        if not self.place_bet(bet):
            return None, False
        
        spin = self.spin()

        if (twelfth == "1st" and spin in self.first_twelfth) or (twelfth == "2nd" and spin in self.second_twelfth) or (twelfth == "3rd" and spin in self.third_twelfth):
            self.win(2, bet)
            return spin, True
        return spin, False





game = RouletteGame()



# wheel order
wheel_order = [
0, 32, 15, 19, 4, 21, 2, 25, 17,
34, 6, 27, 13, 36, 11, 30, 8, 23,
10, 5, 24, 16, 33, 1, 20, 14, 31,
9, 22, 18, 29, 7, 28, 12, 35, 3, 26
]

wheel_colors = []
for n in wheel_order:
    if n == 0:
        wheel_colors.append("green")
    elif n in game.red:
        wheel_colors.append("red")
    else:
        wheel_colors.append("black")



num_pockets = 37


rotation = 0
speed = 0
target_angle = 0
spinning = False



root = tk.Tk()
root.title("Roulette")
root.geometry("1200x800")
root.config(background="brown")

# -- top frame --
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

result_label = tk.Label(top_frame, text="Hello!")
result_label.pack()

chip_label = tk.Label(top_frame, text=f"Chips: {game.chips}")
chip_label.pack()




# --- bet ---
bet_frame = tk.Frame(root)
bet_frame.pack(pady=10)
bet_frame.config(background="brown")

bet_lable = tk.Label(bet_frame, text="Bet:", font=("American Extra Bold", 15))
bet_lable.pack()

bet_entry = tk.Entry(bet_frame)
bet_entry.pack(pady=5)



# --- left frame ---
left_frame = tk.Frame(root)
left_frame.pack(side="left")

# --- color buttons ---
red_button = tk.Button(left_frame, text="Red", bg="red", fg="white",
                       width=8, height=3, font=("Arial", 16, "bold"),
                       command=lambda: place_color("red"))
red_button.pack()

#spacer = tk.Frame(left_frame, height=10, width=111, bg="brown")
#spacer.pack()

black_button = tk.Button(left_frame, text="Black", bg="black", fg="white",
                         width=8, height=3, font=("Arial", 16, "bold"),
                         command=lambda: place_color("black"))
black_button.pack()


# --- odds & evens buttons ---

odds_button = tk.Button(left_frame, text="Odds", bg="green", fg="gold",
                        width=8, height=3, font=("Areal", 16),
                        command=lambda: chose_odds_evens("odds"))
odds_button.pack()

even_button = tk.Button(left_frame, text="Evens", bg= "green", fg="gold",
                        width=8, height=3, font=("Arial", 16),
                        command=lambda: chose_odds_evens("evens"))
even_button.pack()



# --- board gui ---
board_frame = tk.Frame(root, bg="brown")
board_frame.pack(side="right", padx=10, pady=10)









# --- center frame ---

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

def draw_wheel(angle, ball_rotation):
    canvas.delete("wheel")
    
    for i in range(num_pockets):
        start = (360/num_pockets) * i + angle
        extent = 360/num_pockets

        canvas.create_arc(
            50, 50, 350, 350,
            start=start,
            extent=extent,
            fill=wheel_colors[i],
            outline="white",
            tags="wheel"
        )

        mid_angle = start + extent / 2
        rad = math.radians(mid_angle)

        x = 200 + 120 * math.cos(rad)
        y = 200 - 120 * math.sin(rad)

        canvas.create_text(
            x, y,
            text=str(wheel_order[i]),
            fill="white",
            font=("Arial", 10, "bold"),
            tags="wheel"
        )

    # draw ball at its rotation
    ball_angle = math.radians(ball_rotation)
    bx = 200 + 140 * math.cos(ball_angle)
    by = 200 - 140 * math.sin(ball_angle)

    canvas.create_oval(
        bx-5, by-5, bx+5, by+5,
        fill="white",
        tags="wheel"
    )


def animate_spin(spin_result, callback):
    global rotation, speed, spinning, ball_rotation

    spinning = True
    speed = 30

    # Compute target angle
    pocket_angle = 360 / num_pockets
    index = wheel_order.index(spin_result)
    target_angle = 360 - (index * pocket_angle)  # ball lands on correct number
    start_ball = ball_rotation  # start from current position

    def spin():
        global rotation, speed, spinning, ball_rotation

        rotation += speed
        rotation %= 360
        speed *= 0.95  

        # Smoothly move ball toward target
        ball_rotation += (target_angle - ball_rotation) * 0.1  # interpolation

        draw_wheel(rotation, ball_rotation)

        # Stop condition
        if abs(ball_rotation - target_angle) > 0.5 or speed > 0.5:
            root.after(30, spin)
        else:
            ball_rotation = target_angle
            draw_wheel(rotation, ball_rotation)
            spinning = False
            callback(spin_result)

    spin()







# --- bottom frame ---

bottom_frame = tk.Frame(root)
bottom_frame.pack(side="bottom", fill="x")
bottom_frame.config(bg="brown")


row3_button = tk.Button(bottom_frame,
                        text="3rd Row",
                        bg="green", fg="gold", 
                        width=10, height=5,
                        font=(12),
                        command=lambda: chose_row("3rd"))
row3_button.grid(row=0, column=2, padx=5, pady=5)

row2_button = tk.Button(bottom_frame,
                        text="2nd Row",
                        bg="green", fg="gold", 
                        width=10, height=5,
                        font=(12),
                        command=lambda: chose_row("2nd"))
row2_button.grid(row=0, column=1, padx=5, pady=5)

row1_button = tk.Button(bottom_frame,
                        text="1st Row",
                        bg="green", fg="gold", 
                        width=10, height=5,
                        font=(12),
                        command=lambda: chose_row("1st"))
row1_button.grid(row=0, column=0, padx=5, pady=5)



first_twelfth_button = tk.Button(bottom_frame,
                                 text="1st twelfth",
                                 bg="black", fg="gold",
                                 width=10, height=5,
                                 font=(10),
                                 command=lambda: choose_twelths("1st"))
first_twelfth_button.grid(row=1, column=1, padx=5, pady=5)



# --- board logic ---
def create_board(frame):

    zero_button = tk.Button(
        frame,
        text="0",
        bg="green",
        fg="white",
        font=("Arial", 12, "bold"),
        width=10,
        height=1,
        command=lambda n=0: bet_number(n)
        )
    zero_button.grid(row=0, column=0, columnspan=3, sticky="nsew")



    for i in range(1, 37):
        row = (i - 1) // 3 + 1
        col = (i - 1) % 3

        color = "red" if i in game.red else "black"

        button = tk.Button(
            frame,
            text=str(i),
            bg=color,
            fg="white",
            font=("Arial", 12, "bold"),
            width=10,
            height=1,
            command=lambda n=i: bet_number(n)
        )
        button.grid(row=row, column=col, sticky="nsew")

    for c in range(3):
        frame.columnconfigure(c, weight=1)

    for r in range(13):
        frame.rowconfigure(r, weight=1)



def bet_number(number):
    try:
        bet = int(bet_entry.get())
    except ValueError:
        result_label.config(text="Enter a valid number!")
        return

    if not game.place_bet(bet):
        result_label.config(text="Not enough chips!")
        return

    spin_result = game.spin()  # single spin
    won = (spin_result == number)
    if won:
        game.win(36, bet)  # 35:1 payout

    def show_result(result):
        msg = f"Ball landed on {result}. You {'won' if won else 'lost'}."
        result_label.config(text=msg)
        chip_label.config(text=f"Chips: {game.chips}")

    animate_spin(spin_result, show_result)



def place_color(color):
    try:
        bet = int(bet_entry.get())
    except ValueError:
        result_label.config(text="Enter a valid number!")
        return

    if not game.place_bet(bet):
        result_label.config(text="Not enough chips!")
        return

    # SINGLE spin
    spin_result = game.spin()

    # calculate win based on that spin
    won = (color == "red" and spin_result in game.red) or \
          (color == "black" and spin_result in game.black)
    if won:
        game.win(2, bet)

    # animate using the same spin_result
    def show_result(result):
        msg = f"Ball landed on {spin_result}. You {'won' if won else 'lost'} the {color} bet!"
        result_label.config(text=msg)
        chip_label.config(text=f"Chips: {game.chips}")

    animate_spin(spin_result, show_result)


def chose_row(row):
    try:
        bet = int(bet_entry.get())
    except ValueError:
        result_label.config(text="Enter a valid number!")
        return
    
    if not game.row_bet(bet):
        result_label.config(text="Not enough chips!")
        return

    spin, won = game.bet_color(bet, row)
    if spin is None:
        result_label.config(text="Not enough chips!")
        return
    
    msg = f"Ball landed on {spin}. You {'won' if won else 'lost'} the {row} bet!"
    result_label.config(text=msg)
    chip_label.config(text=f"Chips: {game.chips}")
    



def chose_odds_evens(odds_or_evens):
    try:
        bet = int(bet_entry.get())
    except ValueError:
        result_label.config(text="Enter a valid number!")
        return


    spin, won = game.odds_and_even_bet(bet, odds_or_evens)
    if spin is None:
        result_label.config(text="Not enough chips!")
        return 
    
    msg = f"Ball landed on {spin}. You {'won' if won else 'lost'} the {odds_or_evens}"
    result_label.config(text=msg)
    chip_label.config(text=f"Chips: {game.chips}")



def choose_twelths(twelfth):
    try:
        bet = int(bet_entry.get())
    except ValueError:
        result_label.config(text="Enter a valid bet")
        return
    

    spin_result = game.spin()


    # calculate win based on that spin
    won = (twelfth == "1st" and spin_result in game.first_twelfth) or \
          (twelfth == "2nd" and spin_result in game.second_twelfth) or \
          (twelfth == "3rd" and spin_result in game.third_twelfth)
    if won:
        game.win(2, bet)

    # animate using the same spin_result
    def show_result(result):
        msg = f"Ball landed on {spin_result}. You {'won' if won else 'lost'} the {twelfth} bet!"
        result_label.config(text=msg)
        chip_label.config(text=f"Chips: {game.chips}")

    animate_spin(spin_result, show_result)









draw_wheel(0, 0)
create_board(board_frame)
root.mainloop()