import itertools
import getpass
import multiprocessing as mp
# allowed symbols for the password
symbols_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ0123456789_-!?=@#")

# segregated lists from symbols_list
letter_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ")
number_list = list("0123456789")
sym_list = list("_-!?=@#")

# user password
def user_password(symbols_list):
    while True:
        print("\n allowed characters:\n",symbols_list, "\n\nuse MAX 6 letters, symbols or numbers\n")
        p = getpass.getpass(prompt="\ninsert a password: ", echo_char='*').upper() #password
        if len(p) > 6:
            print("\nPassword too long, try again.\n")
            continue
    

        if all(char in symbols_list for char in p):
            return p
        else:
            print("\nthose are not accepted letter(s)")

# mutations on words
from itertools import product
def mutation(word, max_len):
    mutations = set()

    mutations.add(word)
    # for lower and cap letters. not in use rn
    #mutations.add(word.upper())
    #mutations.add(word.capitalize())

    max_digits = 2
    max_sym = 2
    max_letters = 2

    remaining = max_len - len(word)
    if remaining <= 0:
        return mutations

    remaining_digits = min(max_digits, max_len - len(word))
    remaining_sym = min(max_sym, max_len - len(word))
    remaining_letters = min(max_letters, max_len - len(word))

    # digits
    for length in range(1, remaining_digits + 1):
        for combo in product(number_list, repeat=length):
            mutations.add(word + "".join(combo))
    
    # Symbols
    for length in range(1, remaining_sym + 1):
        for combo in product(sym_list, repeat=length):
            mutations.add(word + "".join(combo))

    # letters
    for length in range(1, remaining_letters + 1):
        for combo in product(letter_list, repeat=length):
            mutations.add(word + "".join(combo))
        
    return mutations




# guessing the password
def password_guess(password):    
    guess_count = 0
    max_len = len(password)

    # importing a list of common passwords
    from pathlib import Path

    password_list_file = Path(__file__).parent / "Password_list.txt"

    with open(password_list_file, "r", encoding="utf-8") as f:
        for line in f:
            base = line.strip().upper()

            if not base or len(base) > max_len:
                continue
                
            for guess in mutation(base, max_len):
                guess_count += 1
                if guess == password:
                    print("\namount of guesses: ", guess_count)
                    print("\nPassword found in common password list: ", password)
                    return guess
                
    # imports english dictionary
    eng_dict_file = Path(__file__).parent / "english words.txt"

    with open(eng_dict_file, "r", encoding="utf-8") as f:
        for line in f:
            base = line.strip().upper()

            if not base or len(base) > max_len:
                continue

            for guess in mutation(base, max_len):
                guess_count += 1
                if guess == password:
                    print("\namount of guesses: ", guess_count)
                    print("\nPassword found in the English dictionary", password, "\n")
                    return guess
                
    # imports norwegian dictionary
    nor_dict_file = Path(__file__).parent / "nor dict.txt"

    with open(nor_dict_file, "r", encoding="utf-8") as f:
        for line in f:
            base = line.strip().upper()

            if not base or len(base) > max_len:
                guess_count += 1
                if guess == password:
                    print("\nAmount of guesses: ", guess_count)
                    print("\nPassword found in Norwegian dictionary", password, "\n")
                    return guess

    # uses itertools for all posible combos with symbols_list
    for length in range(1, max_len + 1):
        for combo in itertools.product(symbols_list, repeat=length):
            guess_count +=1
            guess = "".join(combo)
            if guess == password:
                print("\nAttempts used: ", guess_count)
                print("\nSuccess: ", guess, "\n")
                return guess
        
    print("\nno password found")


password = user_password(symbols_list)
passg = password_guess(password) # password guess


