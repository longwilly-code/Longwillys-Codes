import random
import tkinter as tk
import json
import os
from cryptography.fernet import Fernet
import bcrypt


user_dir = "users"
os.makedirs(user_dir, exist_ok=True)

#--- JSON key ---
key_file = "mykey.key"

if not os.path.exists(key_file):
    # Generate a new key only if it doesn't exist
    key = Fernet.generate_key()
    with open(key_file, "wb") as f:
        f.write(key)
else:
    with open(key_file, "rb") as f:
        key = f.read()



#--- global ---
chips = 50



red = (1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)


# --- GUI ---
root = tk.Tk()
root.geometry("800x800")
#root.resizable(False, False)
root.title("Roulette")
root.config(background="brown")



# --- Frames ---
play_frame = tk.Frame(root)


# --- label ---
chips_label = tk.Label(root, text=f"CHIPS: {chips}", font=("Americana Extra Bold", 18, "bold"), bg="darkgreen", fg="white")
chips_label.pack(pady=20)

result_label = tk.Label(root, font=("Americana Extra Bold", 16))
result_label.pack(pady=20)

# --- Hide Frames ---
def hide_frames():
    play_frame.pack_forget()




# --- spin ---
def spin_wheel():
    return random.randint(0, 36)


def bet():
    
    bet_entry = tk.Entry(play_frame)
    bet_entry.grid(row=1, column=1, padx=5, pady=5)

    
    if bet_entry <= 0 or bet_entry > chips:
        result_label.config(text="Invalid bet")
        return

def bet_row(row_number):
    global chips
    
    bet()
    spin_result = spin_wheel()

    # the rows
    row_1 = (1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34)
    row_2 = (2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35)
    row_3 = (3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36)

    # Show the spin result
    result_label.config(text=f"Spin result: {spin_result}")

    # Check if the spin result is in the selected row
    if row_number == 1 and spin_result in row_1:
        result_label.config(text=f"Ball landed on {spin_result} You won on row 1!")
    elif row_number == 2 and spin_result in row_2:
        result_label.config(text=f"Ball landed on {spin_result} You won on row 2!")
    elif row_number == 3 and spin_result in row_3:
        result_label.config(text=f"Ball landed on {spin_result} You won on row 3!")
    else:
        result_label.config(text=f"Ball landed on {spin_result} You lost.")


# --- bet frame ---

bet_frame = tk.Frame(root, bg="brown")
bet_frame.pack(side="right", fill="y", padx=20, pady=20)


def color_bet(u_color):
    global chips

    spin_result = spin_wheel()

    r = (1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)
    b = (2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35)
    

    c = ""
    if spin_result in r:
        c = "red"
    elif spin_result in b:
        c = "black"
    

    if u_color == c:
        result_label.config(text=f"Ball landed on {spin_result} {c}, you won")
    else:
        result_label.config(text=f"You lost, ball landed on {spin_result} {c}")

def odds_evens_bet(u_oe):
    global chips

    spin_result = spin_wheel()

    evens = (2, 4, 6, 8, 10,
    12, 14, 16, 18,
    20, 22, 24, 26,
    28, 30, 32, 34, 36)

    odds = (1, 3, 5, 7, 9,
    11, 13, 15, 17,
    19, 21, 23, 25,
    27, 29, 31, 33, 35)

    winnig = ""
    if spin_result in evens:
        winnig = "evens"
    elif spin_result in odds:
        winnig = "odds"

    if u_oe == winnig:
        result_label.config(text=f"You won! Ball landed on {spin_result} {winnig}")
    else:
        result_label.config(text=f"You lost. Ball landed on {spin_result} {winnig}")

    
def number_bet(n,):
    global chips

    spin_result = spin_wheel()

    if spin_result == n:
        result_label.config(text=f"Jackpot! You won. Ball landed on {spin_result}")
    else:
        result_label.config(text=f"You lost. Ball landed on {spin_result}")


def x_to_y_bet(x_y):
    global chips

    spin_result = spin_wheel()

    x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18) # 1 to 18 (shortend as x)
    y = (19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36) # 19 to 36 (shortend as y)

    if spin_result in x and x_y == "1 to 18":
        result_label.config(text=f"You won! Ball landed on {spin_result} (1 to 18)")
    elif spin_result in y and x_y == "19 to 36":
        result_label.config(text=f"You won! Ball landed on {spin_result} (19 to 36) ")
    else:
        result_label.config(text=f"You lose")


def twelfths_bet(user_twelfth):
    global chips

    spin_result = spin_wheel()

    first_twelfth = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    second_twelfth = (13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)
    third_twelfth = (25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36)

    winning = ""
    if spin_result in first_twelfth:
        winning = "1st twelfth"
    elif spin_result in second_twelfth:
        winning = "2nd twelfth"
    elif spin_result in third_twelfth:
        winning = "3rd twelfth"

    if spin_result in first_twelfth and user_twelfth == "1st twelfth":
        result_label.config(text=f"You won! Ball landed {spin_result} ({winning})")

    elif spin_result in second_twelfth and user_twelfth == "2nd twelfth":
        result_label.config(text=f"You won! Ball landed on {spin_result} ({winning})")
    elif spin_result in third_twelfth and user_twelfth == "3rd twelfth":
        result_label.config(text=f"You won! Ball landed on {spin_result} ({winning})")
    else:
        result_label.config(text=f"You lost. Ball landed on {spin_result} ({winning})")






def select_number(n):
    result_label.config(text=f"number selected {n}")

# --- roulette board ---
def create_board(frame):
    zero_button = tk.Button(frame,
                            text="0",
                            bg="green",
                            fg="white",
                            font=("American Extra Bold", 18, "bold"),
                            width=6,
                            height=3,
                            command=lambda:number_bet(0))
    zero_button.grid(row=0, column=0, columnspan=3, sticky="nsew")

    for i in range(1, 37):
        row = ((i - 1) % 12) + 1
        col = (i - 1) // 12

        color = "red" if i in red else "black"

        button = tk.Button(frame,
                           text=str(i),
                           bg=color,
                           fg="white",
                           font=("American Extra Bold", 18, "bold"),
                           width=6,
                           height=3,
                           command=lambda n=i:number_bet(n))
        button.grid(row=row, column=col, sticky="nsew")

    for c in range(3):
        frame.columnconfigure(c, weight=1)

    for r in range(12):
        frame.rowconfigure(r, weight=1)


    # --- Row betting ---
    row1_button = tk.Button(frame,
                text="2 to 1",
                bg="gold",
                fg="white",
                font=("Ameerican Extra Bold", 18, "bold"),
                command=lambda: bet_row(1))
    row1_button.grid(row=13, column=0, sticky="nsew")

    row2_button = tk.Button(frame,
                text="2 to 1",
                bg="gold",
                fg="white",
                font=("Ameerican Extra Bold", 18, "bold"),
                command=lambda: bet_row(2))
    row2_button.grid(row=13, column=1, sticky="nsew")

    row3_button = tk.Button(frame,
                text="2 to 1",
                bg="gold",
                fg="white",
                font=("Ameerican Extra Bold", 18, "bold"),
                command=lambda: bet_row(3))
    row3_button.grid(row=13, column=2, sticky="nsew")

    


# --- color betting ---
color_frame = tk.Frame(root, bg="brown")
color_frame.pack(side="left", fill="y", padx=20, pady=20)

red_button = tk.Button(color_frame,
                       text="Red",
                       bg="red",
                       fg="white",
                       font=("American Extra Bold", 18, "bold"),
                       width=6,
                       height=2,
                       command=lambda: color_bet("red"))
red_button.pack(pady=10)

black_button = tk.Button(color_frame,
                         text="Black",
                         bg="black",
                         fg="white",
                         font=("American Extra Bold", 18, "bold"),
                         width=6,
                         height=2,
                         command=lambda: color_bet("black"))
black_button.pack(pady=10)


# --- odds & evens buttons --- 
odds_evens_frame = tk.Frame(root, bg="brown")
odds_evens_frame.pack(side="right", fill="y", padx=20, pady=20)

odds_button = tk.Button(odds_evens_frame,
                        text="odds",
                        bg="gold",
                        fg="white",
                        font=("American Extra Bold", 18, "bold"),
                        width=6,
                        height=3,
                        command=lambda: odds_evens_bet("odds"))
odds_button.pack(pady=10)

evens_button = tk.Button(odds_evens_frame,
                        text="evens",
                        bg="gold",
                        fg="white",
                        font=("American Extra Bold", 18, "bold"),
                        width=6,
                        height=3,
                        command=lambda: odds_evens_bet("evens"))
evens_button.pack(pady=10)


# --- 1 to 18 & 19 to 36 ---
x_to_y_frame = tk.Frame(root, bg="brown")
x_to_y_frame.pack(side="left", fill="x", padx=10, pady=10)

x_button = tk.Button(x_to_y_frame,
                     text="1 to 18",
                     bg="green",
                     fg="gold",
                     font=("American Extra Bold", 18, "bold"),
                     width=6,
                     height=3,
                     command=lambda: x_to_y_bet("1 to 18"))
x_button.pack(pady=10)

y_button = tk.Button(x_to_y_frame,
                     text="19 to 36",
                     bg="green",
                     fg="gold",
                     font=("American Extra Bold", 18, "bold"),
                     width=6,
                     height=3,
                     command=lambda: x_to_y_bet("19 to 36"))
y_button.pack(pady=10)
                     
# --- twelfths ---
twelfths_frame = tk.Frame(root, bg="brown")
twelfths_frame.pack(side="right", fill="x", padx=10, pady=10)

first_twelfths_button = tk.Button(twelfths_frame,
                             text="1st twelfth",
                             bg="red",
                             fg="gold",
                             font=("American Extra Bold", 15, "bold"),
                             width=8,
                             height=3,
                             command=lambda: twelfths_bet("1st twelfth"))
first_twelfths_button.pack(pady=10)

second_twelfths_button = tk.Button(twelfths_frame,
                             text="2nd twelfth",
                             bg="black",
                             fg="gold",
                             font=("American Extra Bold", 15, "bold"),
                             width=8,
                             height=3,
                             command=lambda: twelfths_bet("2nd twelfth"))
second_twelfths_button.pack(pady=10)

third_twelfths_button = tk.Button(twelfths_frame,
                             text="3rd twelfth",
                             bg="green",
                             fg="gold",
                             font=("American Extra Bold", 15, "bold"),
                             width=8,
                             height=3,
                             command=lambda: twelfths_bet("3rd twelfth"))
third_twelfths_button.pack(pady=10)






# --- Start ---
play_frame.pack(expand=True)
create_board(play_frame)
root.mainloop()


