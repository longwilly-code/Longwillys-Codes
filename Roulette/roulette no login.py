import random
import tkinter as tk

#--Global--
chips = 50

red = (1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)
black = (2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35)
green = (0,)

#--GUI--
root = tk.Tk()
root.geometry("800x400")
root.resizable(False, False)
root.title("Roulette")
root.config(background="dark red")

#--Frames--
choice_frame = tk.Frame(root)
number_frame = tk.Frame(root)
color_frame = tk.Frame(root)

# --- Chips and result display ---
chips_label = tk.Label(root, text=f"CHIPS: {chips}", font=("Americana Extra Bold", 18, "bold"), bg="darkgreen", fg="white")
chips_label.pack(pady=10)

result_label = tk.Label(root, text="Result:", font=("Americana Extra Bold", 16))
result_label.pack(pady=20)

#--hides frames--
def hide_frames():
    choice_frame.pack_forget()
    number_frame.pack_forget()
    color_frame.pack_forget()

#---choice frame---
def show_choice_frame():
    hide_frames()
    choice_frame.pack(pady=20)

def numbers():
    hide_frames()
    number_frame.pack(pady=20)

def colors():
    hide_frames()
    color_frame.pack(pady=20)

#--buttons for bet type--
tk.Label(choice_frame, text="Choose your bet type:", font=("Americana Extra Bold", 14)).pack(pady=10)
tk.Button(choice_frame, text="Number", width=10, command=numbers).pack(pady=5)
tk.Button(choice_frame, text="Color", width=10, command=colors).pack(pady=5)

# --- Color Frame Widgets ---
tk.Label(color_frame, text="Place Your Color Bet", font=("Americana Extra Bold", 14)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(color_frame, text="Enter your bet:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
bet_entry_c = tk.Entry(color_frame)
bet_entry_c.grid(row=1, column=1, padx=5, pady=5)

tk.Button(color_frame, text="Red", width=10, command=lambda: bet_color("red")).grid(row=2, column=0, padx=5, pady=5)
tk.Button(color_frame, text="Black", width=10, command=lambda: bet_color("black")).grid(row=2, column=1, padx=5, pady=5)
tk.Button(color_frame, text="Green", width=10, command=lambda: bet_color("green")).grid(row=3, column=0, columnspan=2, pady=5)
tk.Button(color_frame, text="Back", width=20, command=show_choice_frame).grid(row=4, column=0, columnspan=2, pady=10)

# --- Number Frame Widgets ---
tk.Label(number_frame, text="Place Your Number Bet", font=("Americana Extra Bold", 14)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(number_frame, text="Choose a number (0-36):").grid(row=1, column=0, sticky="e", padx=5, pady=5)
number_entry = tk.Entry(number_frame)
number_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(number_frame, text="Enter your bet:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
bet_entry_n = tk.Entry(number_frame)
bet_entry_n.grid(row=2, column=1, padx=5, pady=5)

tk.Button(number_frame, text="Place Number Bet", width=20, command=lambda: bet_number()).grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(number_frame, text="Back", width=20, command=show_choice_frame).grid(row=4, column=0, columnspan=2, pady=5)

# --- Betting Functions ---
def bet_color(user_color):
    global chips
    try:
        bet = int(bet_entry_c.get())
    except ValueError:
        result_label.config(text="Invalid bet")
        return

    if bet <= 0 or bet > chips:
        result_label.config(text="Invalid bet")
        return

    r = random.randint(0, 36)
    if r in red:
        winning_color = "red"
    elif r in black:
        winning_color = "black"
    else:
        winning_color = "green"

    if user_color == winning_color:
        if winning_color == "green":
            chips += bet * 35
        else:
            chips += bet
        result_label.config(text=f"Ball landed on {r} ({winning_color})")
    else:
        chips -= bet
        result_label.config(text=f"Ball landed on {r} ({winning_color})")

    chips_label.config(text=f"{chips} chips.")
    
    
    if chips <= 0:
        chips + 10
        chips_label.config(text=f"{chips} chips.")

    bet_entry_n.delete(0, tk.END)

def bet_number():
    global chips
    try:
        user_number = int(number_entry.get())
        bet = int(bet_entry_n.get())
    except ValueError:
        result_label.config(text="Invalid bet")
        return

    if bet <= 0 or bet > chips:
        result_label.config(text="Invalid bet")
        return

    r = random.randint(0, 36)
    if user_number == r:
        chips += bet * 35
        result_label.config(text=f"JACKPOT!!! Ball landed on {r}")
    else:
        chips -= bet
        result_label.config(text=f"Ball landed on {r}")

    chips_label.config(text=f"{chips} chips.")
    

    if chips <= 0:
        chips + 10
        chips_label.config(text=f"{chips} chips.")
    
    bet_entry_n.delete(0, tk.END)

# --- Start App ---
show_choice_frame()
root.mainloop()
