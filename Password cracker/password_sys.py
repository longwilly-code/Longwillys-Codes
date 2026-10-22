#---imports---
import itertools
import string
import time

#--colors---
YELLOW = "\033[33m"
BLUE = "\033[34m"
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"



# --- allowed characters (94 total characters) ---
allowed_chars_list = list(string.ascii_letters + string.digits + string.punctuation)
#print(len(allowed_chars_list))

#--- sets the rules for colors of each unique stat---
combo_threshold = [
    (1_000_000, YELLOW),
    (1_000_000_000, RED)

]

seconds_threshold = [
    (300, YELLOW),
    (600, RED)

]




guess_count_threshold = [
    (1_000_000, YELLOW),
    (1_000_000_000, RED)
]


real_time_color_threshold = [
    (300, YELLOW),
    (600, RED)
]




#--- time calcolator / esstimated time ---
def time_calc(password):

    combinations = len(allowed_chars_list) ** len(password)

    guesses_per_sec = 1_000_000
    seconds = combinations / guesses_per_sec
    return combinations, seconds





#--- gets the password ---
def user():
    username = input("username: ")
    password = input("password: ") 
    return username, password
    

# --- tries to break the password ---
def cracker(password):
    
    guess_count = 0

    for length in range(1, len(password) + 1):
        for combo in itertools.product(allowed_chars_list, repeat=length):
            guess = "".join(combo) 
            guess_count += 1


            if guess == password:
                return guess, guess_count       

   
# --- actual time ---
def messure_time(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    elapsed = end - start

    return result, elapsed


# --- sets the color based on the thresholds ---
def get_color(value, threshold, default_color=GREEN):
    
    for limit , color in threshold:
        if value < limit:
            return color
    return default_color

    


# --- func for slow prints ---
def slow_print(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# --- ... animation for estimated time ---
def animation(seconds, color, cycles=3, delay=0.5):
    for _ in range(cycles):
        for dots in range(1, 4):
            print(f"\rEstimated Time: {color}{seconds:.2f}{'.' * dots} Seconds {RESET}   ", end="", flush=True)
            time.sleep(delay)
            
            while True:
                if password != cracked_password:
                    animation
                else:
                    break

    print()


# --- clears the terminal ---
def clear_terminal():
    for i in range(30):
        print("\n")
    return i




clear = clear_terminal()

username, password = user()

combinations, seconds = time_calc(password)
seconds_color = get_color(seconds, seconds_threshold)
combo_color = get_color(combinations, combo_threshold)

print(f"\ncombinations possible: {combo_color}{combinations}{RESET}")
animation(seconds, seconds_color, 5)





(cracked_password, guess_count), real_time = messure_time(cracker, password)

guess_count_color = get_color(guess_count, guess_count_threshold)
time_color = get_color(real_time, real_time_color_threshold)





slow_print(f"\n{GREEN}Results:{RESET}\n")
slow_print(f"\nusername: {BLUE}{username}{RESET}")
slow_print(f"\npassword: {GREEN}{cracked_password}{RESET}")
slow_print(f"\nguesses: {guess_count_color}{guess_count}{RESET}")
slow_print(f"\nsecceded in: {time_color}{real_time:.2f}{RESET} seconds")




