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

fernet = Fernet(key)

#--Global--
chips = 50
current_user = None

red = (1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)
black = (2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35)
green = (0,)

evens = (2, 4, 6, 8, 10,
12, 14, 16, 18,
20, 22, 24, 26,
28, 30, 32, 34, 36)

odds = (1, 3, 5, 7, 9,
11, 13, 15, 17,
19, 21, 23, 25,
27, 29, 31, 33, 35)

first_twelfth = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
second_twelfth = (13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)
third_twelfth = (25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36)

x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18) # 1 to 18 (shortend as x)
y = (19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36) # 19 to 36 (shortend as y)

two_to_one_1 = (1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34)
two_to_one_2 = (2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35)
two_to_one_3 = (3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36)

#--GUI--
root = tk.Tk()
root.geometry("1280x920")
root.resizable(False, False)
root.title("Roulette")
root.config(background="dark red")

#--Frames--
login_frame = tk.Frame(root)

signin_frame = tk.Frame(root)
signup_frame = tk.Frame(root)


choice_frame = tk.Frame(root)

number_frame = tk.Frame(root)
color_frame = tk.Frame(root)

odds_evens_frame = tk.Frame(root)

twelfths_frame = tk.Frame(root)

x_to_y_frame = tk.Frame(root)

row_frame = tk.Frame(root)

# --- Chips and result display ---
chips_label = tk.Label(root, text=f"CHIPS: {chips}", font=("Americana Extra Bold", 18, "bold"), bg="darkgreen", fg="white")
chips_label.pack(pady=10)

result_label = tk.Label(root, font=("Americana Extra Bold", 16))
result_label.pack(pady=20)


table_text = "Roulette Table:\n         0     \n"
for row in range(12):

    row_numbers = [str(row * 3 + col + 1).rjust(2) for col in range(3)]
    table_text += " ".join(row_numbers) + "\n"

table_text = table_text

table_label = tk.Label(root,
                        text=table_text,
                       font=("Americana Extra Bold", 16),
                       justify="left")
table_label.pack(pady=20)


#--hides frames--
def hide_frames():

    #--login frames--
    login_frame.pack_forget()
    signin_frame.pack_forget()
    signup_frame.pack_forget()

    #--choice frames--
    choice_frame.pack_forget()

    number_frame.pack_forget()
    color_frame.pack_forget()

    odds_evens_frame.pack_forget()

    twelfths_frame.pack_forget()

    x_to_y_frame.pack_forget()

    row_frame.pack_forget()





    #--labels--
    chips_label.pack_forget()
    result_label.pack_forget()
    table_label.pack_forget()

#---frames---
def show_login_frame():
    hide_frames()
    login_frame.pack(pady=20)

def signin():
    hide_frames()
    signin_frame.pack(pady=20)

def signup():
    hide_frames()
    result_label.pack(pady=20)
    signup_frame.pack(pady=20)

def show_choice_frame():
    hide_frames()
    result_label.pack(pady=20)
    choice_frame.pack(pady=20)


def numbers():

    hide_frames()

    result_label.pack(pady=20)
    chips_label.pack(pady=20)

    number_frame.pack(pady=20)

    

def colors():
    hide_frames()
    result_label.pack(pady=20)
    chips_label.pack(pady=20)

    color_frame.pack(pady=20)

def odds_evens():
    hide_frames()
    
    result_label.pack(pady=20)
    chips_label.pack(pady=20)

    odds_evens_frame.pack(pady=20)

def twelfths():
    hide_frames()

    result_label.pack(pady=20)
    chips_label.pack(pady=20)
    table_label.pack(pady=20)

    twelfths_frame.pack(pady=20)

def x_to_y():
    hide_frames()

    result_label.pack(pady=20)
    chips_label.pack(pady=20)
    table_label.pack(pady=20)

    x_to_y_frame.pack(pady=20)

def three_row():
    hide_frames()
    
    result_label.pack(pady=20)
    chips_label.pack(pady=20)
    table_label.pack(pady=20)

    row_frame.pack(pady=20)



#--login or sign in--
tk.Label(login_frame, text="login or sign up", font=("Americana Extra Bold", 14)).pack(pady=10)

tk.Button(login_frame, text="Sign Up", width=30, command=signup).pack(pady=10)

tk.Button(login_frame, text="sign in", width=30, command=signin).pack(pady=50)


#--sign up--
tk.Label(signup_frame, text="Username:").pack(pady=5)
signup_username_entry = tk.Entry(signup_frame)
signup_username_entry.pack(pady=5)

tk.Label(signup_frame, text="Password:").pack(pady=5)
signup_password_entry = tk.Entry(signup_frame, show="*")
signup_password_entry.pack(pady=5)

tk.Button(signup_frame, text="Sign Up",
           command=lambda: create_user_gui(signup_username_entry.get(),
                                            signup_password_entry.get())).pack(pady=10)

tk.Button(signup_frame, text="Back", command= show_login_frame).pack(pady=5)




#--log in--
tk.Label(signin_frame, text="Username:").pack(pady=5)
signin_username_entry = tk.Entry(signin_frame)
signin_username_entry.pack(pady=5)

tk.Label(signin_frame, text="Password:").pack(pady=5)
signin_password_entry = tk.Entry(signin_frame, show="*")
signin_password_entry.pack(pady=5)

tk.Button(signin_frame, text="Sign In",
           command=lambda: login_gui(signin_username_entry.get(), 
                                     signin_password_entry.get())).pack(pady=10)

tk.Button(signin_frame, text="Back", command= show_login_frame).pack(pady=5)




#--buttons for choice frame type--
tk.Label(choice_frame, text="Choose your bet type:", font=("Americana Extra Bold", 14)).pack(pady=10)
tk.Button(choice_frame, text="Number", width=10, command=numbers).pack(pady=5)
tk.Button(choice_frame, text="Color", width=10, command=colors).pack(pady=5)
tk.Button(choice_frame, text="Odds & Evens", width=10, command=odds_evens).pack(pady=5)
tk.Button(choice_frame, text="Twelfths", width=10, command=twelfths).pack(pady=5)
tk.Button(choice_frame, text="1 to 18 & 19 to 36", width=20, command=x_to_y).pack(pady=5)
tk.Button(choice_frame, text="Rows", width=10, command=three_row).pack(pady=5)




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


# --- Odds & Evens widgets ---

tk.Label(odds_evens_frame, text="Place Your Color Bet", font=("Americana Extra Bold", 14)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(odds_evens_frame, text="Enter your bet:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
bet_entry_oe = tk.Entry(odds_evens_frame)
bet_entry_oe.grid(row=1, column=1, padx=5, pady=5)

tk.Button(odds_evens_frame, text="Evens", width=10, command=lambda: bet_odds_evens("Evens")).grid(row=2, column=0, padx=5, pady=5)
tk.Button(odds_evens_frame, text="Odds", width=10, command=lambda: bet_odds_evens("Odds")).grid(row=2, column=1, padx=5, pady=5)

tk.Button(odds_evens_frame, text="Back", width=20, command=show_choice_frame).grid(row=4, column=0, columnspan=2, pady=10)


# --- Tweltfhs widgets ---

tk.Label(twelfths_frame, text="Place Your Bet", font=("Americana Extra Bold", 14)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(twelfths_frame, text="Enter your bet:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
bet_entry_t = tk.Entry(twelfths_frame)
bet_entry_t.grid(row=1, column=1, padx=5, pady=5)

tk.Button(twelfths_frame, text="1st 12", width=20, command=lambda: bet_tweltfhs("1st 12")).grid(row=2, column=0, padx=5, pady=5)
tk.Button(twelfths_frame, text="2nd 12", width=20, command=lambda: bet_tweltfhs("2nd 12")).grid(row=2, column=1, padx=5, pady=5)
tk.Button(twelfths_frame, text="3rd 12", width=20, command=lambda: bet_tweltfhs("3rd 12")).grid(row=2, column=2, padx=5, pady=5)

tk.Button(twelfths_frame, text="Back", width=20, command=show_choice_frame).grid(row=4, column=0, columnspan=2, pady=10)



# --- 1 to 18 & 19 to 36 Widgets ---

tk.Label(x_to_y_frame, text="Place Your Bet", font=("Americana Extra Bold", 14)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(x_to_y_frame, text="Enter your bet:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
bet_entry_x_to_y = tk.Entry(x_to_y_frame)
bet_entry_x_to_y.grid(row=1, column=1, padx=5, pady=5)

tk.Button(x_to_y_frame, text="1 to 18", width=20, command=lambda: bet_x_to_y("1 to 18")).grid(row=2, column=0, padx=5, pady=5)
tk.Button(x_to_y_frame, text="19 to 36", width=20, command=lambda: bet_x_to_y("19 to 36")).grid(row=2, column=1, padx=5, pady=5)


tk.Button(x_to_y_frame, text="Back", width=20, command=show_choice_frame).grid(row=4, column=0, columnspan=2, pady=10)



# --- row Widgets ---

tk.Label(row_frame, text="Place Your Bet", font=("Americana Extra Bold", 14)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(row_frame, text="Enter your bet:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
bet_entry_r = tk.Entry(row_frame)
bet_entry_r.grid(row=1, column=1, padx=5, pady=5)

tk.Button(row_frame, text="1st row", width=20, command=lambda: bet_row("1st row")).grid(row=2, column=0, padx=5, pady=5)
tk.Button(row_frame, text="2nd row", width=20, command=lambda: bet_row("2nd row")).grid(row=2, column=1, padx=5, pady=5)
tk.Button(row_frame, text="3rd row", width=20, command=lambda: bet_row("3rd row")).grid(row=2, column=2, padx=5, pady=5)

tk.Button(row_frame, text="Back", width=20, command=show_choice_frame).grid(row=4, column=0, columnspan=2, pady=10)



#---sign up function---
def create_user_gui(username, password):


    path = os.path.join(user_dir, f"{username}.json")
    if os.path.exists(path):
        result_label.config(text="Username already exists")
        return False

    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())


    user_data = {
        "username": username,
        "password": hashed_pw.decode(),
        "chips": 50  # start with 50 chips
    }

    json_bytes = json.dumps(user_data).encode()
    encrypted_data = fernet.encrypt(json_bytes)

    with open(path, "wb") as f:
        f.write(encrypted_data)

    result_label.config(text="Account created! You have 50 chips.")
    show_choice_frame()
    return True
    


#--existing user log in--
def login_gui(username, password):
    global current_user, chips


    path = os.path.join(user_dir, f"{username}.json")
    if not os.path.exists(path):
        result_label.config(text="User does not exist")
        return None

    with open(path, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = fernet.decrypt(encrypted_data)
    user_data = json.loads(decrypted_data.decode())


    if not bcrypt.checkpw(password.encode(), user_data["password"].encode()):
        result_label.config(text="Incorrect password")
        return None

    
    current_user = username

    chips = user_data["chips"]
    chips_label.config(text=f"Chips: {chips}")
    result_label.config(text=f"Welcome back, {username}!")

    show_choice_frame()
    return user_data

def save_user_data():
    global current_user, chips

    if current_user is None:
        return
    
    path = os.path.join(user_dir, f"{current_user}.json")

    with open(path, "rb") as f:
        encrypted_data = f.read()
        
    decrypted_data = fernet.decrypt(encrypted_data)
    user_data = json.loads(decrypted_data.decode())

    user_data["chips"] = chips

    json_bytes = json.dumps(user_data).encode()
    encrypted_data = fernet.encrypt(json_bytes)

    with open(path, "wb") as f:
        f.write(encrypted_data)


        

        


# --- Betting Functions ---

#---color betting---
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
        chips += 10
        chips_label.config(text=f"{chips} chips.")

    save_user_data()



    bet_entry_c.delete(0, tk.END)







#--number betting--
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
        chips += 10
        chips_label.config(text=f"{chips} chips.")

    save_user_data()
    
    bet_entry_n.delete(0, tk.END)






# --- Odds & Evens Betting ---
def bet_odds_evens(user_row):
    global chips

    try:
        bet = int(bet_entry_oe.get())
    except ValueError:
        result_label.config(text="Invalid bet")
        return
    
    if bet <= 0 or bet > chips:
        result_label.config(text="Invalid bet")
        return


    r = random.randint(0, 36)
    if r == 0:
        chips -= bet
        result_label.config(text="Ball landed on 0 (green)")
    else:
        if (r in evens and user_row == "Evens") or \
        (r in odds and user_row == "Odds"):
            chips += bet
            result_label.config(text=f"Ball landed on {r} ({user_row})")
        else:
            chips -= bet
            if user_row == "Odds":
                result_label.config(text=f"Ball landed on {r} (Evens)")
            elif user_row == "Evens":
                result_label.config(text=f"Ball landed on {r} (Odds)")


    chips_label.config(text=f"{chips} chips.")
    
    
    if chips <= 0:
        chips += 10
        chips_label.config(text=f"{chips} chips.")

    save_user_data()
    bet_entry_oe.delete(0, tk.END)



# --- Tweltfhs Betting ---

def bet_tweltfhs(user_tweltfh):
    global chips

    try:
        bet = int(bet_entry_t.get())
    except ValueError:
        result_label.config(text="Invalid bet")
        return
    
    if bet <= 0 or bet > chips:
        result_label.config(text="Invalid bet")
        return
    
    r = random.randint(0, 36)
    if r == 0:
        bet -= chips
    else:
        if (r in first_twelfth and user_tweltfh == "1st 12") or\
        (r in second_twelfth and user_tweltfh == "2nd 12") or\
        (r in third_twelfth and user_tweltfh == "3rd 12"):
            chips += bet
            result_label.config(text=f"Ball landed on {r} {user_tweltfh}")
        else:
            chips -= bet
            result_label.config(text="aids to code the lost message for this one")

            chips_label.config(text=f"{chips} chips.")
    
    
    if chips <= 0:
        chips += 10
        chips_label.config(text=f"{chips} chips.")

    save_user_data()
    bet_entry_t.delete(0, tk.END)




def bet_x_to_y(user_x_to_y):
    global chips

    try:
        bet = int(bet_entry_x_to_y.get())
    except ValueError:
        result_label.config(text="Invalid bet")
        return
    
    if bet <= 0 or bet > chips:
        result_label.config(text="Invalid bet")
        return
    
    r = random.randint(0, 36)
    if r == 0:
        bet -= chips
    else:
        if (r in x and user_x_to_y == "1 to 18") or\
        (r in y and user_x_to_y == "19 to 36"):
            chips += bet
            result_label.config(text=f"Ball landed on {r} {user_x_to_y}")
            chips_label.config(text=f"CHIPS: {chips}")

        else:
            if (r in x and user_x_to_y == "19 to 36"):
                chips -= bet
                result_label.config(text=f"Ball landed on {r} (1 to 18)")
                chips_label.config(text=f"CHIPS: {chips}")

            elif (r in y and user_x_to_y == "1 to 18"):
                chips -= bet
                result_label.config(text=f"Ball landed on {r} (19 to 36)")
                chips_label.config(text=f"CHIPS: {chips}")


    if chips <= 0:
        chips += 10
        chips_label.config(text=f"{chips} chips.")

    save_user_data()
    bet_entry_x_to_y.delete(0, tk.END)




def bet_row(user_row):
    global chips

    try:
        bet = int(bet_entry_r.get())
    except ValueError:
        result_label.config(text="Invalid bet")
        return
    
    if bet <= 0 or bet > chips:
        result_label.config(text="Invalid bet")
        return
    
    r = random.randint(0, 36)
    if r == 0:
        bet -= chips
    else:
        if (r in two_to_one_1 and user_row == "first row") or\
        (r in two_to_one_2 and user_row == "second row") or\
        (r in two_to_one_3 and user_row == "third row"):
            chips += bet*2
            result_label.config(text=f"Ball landed on {r} ({user_row})")
            chips_label.config(text=f"{chips} chips.")

        else:
            chips -= bet
            result_label.config(text="aids to code the lost message for this one")

            chips_label.config(text=f"{chips} chips.")

        if chips <= 0:
            chips += 10
            chips_label.config(text=f"{chips} chips.")

    save_user_data()
    bet_entry_r.delete(0, tk.END)


            
    
                
    



# --- Start App ---

show_login_frame()
#show_choice_frame()
root.mainloop()
