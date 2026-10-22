import random

class Equipment:
    # dmg = damage | hp = health points | de = defence
    def __init__(self, name ,item_type, dmg, hp, de, price):
        self.name = name
        self.item_type = item_type
        self.dmg = dmg
        self.hp = hp
        self.de = de
        self.price = price

    def __repr__(self):
        if self.item_type == "Weapon":
            return f"{self.name} | {self.item_type} | DMG {self.dmg} | {self.price} Gold"
        
        return f"{self.name} | {self.item_type} | DEF {self.de} | {self.price} Gold"

# add the items that the store should contain
store = [
    # name | item type | dmg | hp | de | price

    # weapons
    Equipment("Wood Sword", "Weapon", 1, 0, 0, 100),

    # armours
    Equipment("Leather Armour", "Armour", 0, 0, 2, 150),
]

# clears the terminal
def clear_terminal():
    print("\033[H\033[J", end="")


def store_or_fight_choice():
    return input(f"\nGold: {current_gold}\n1. Enter The Store\n2. Fight For Gold\nInput: ")
    
    

def show_store():
    print("---STORE---")
    print(f"Gold: {current_gold}")
    print("\n0: Exit\n")
    for i, item in enumerate(store, start=1):
        print(f"{i}: {item}")

# a little hint system for the player. Gives an advice about upgrading weapons
def hint_rng():

    hint = ["\n\n*hint* Better weapons give more money per fight ;)", ""]
    weights = [33, 67]

    rng = random.choices(hint, weights=weights, k=1)[0]
    print(rng)

# long name, but its a weight system, just like the hint system. 
# the difference (not really) is this one will always guarantee a response, whereas the hint rng can reply with "". which is empty. 
def store_clerk_not_enough_money_rng():

    msg = ["Sorry Player, I can't give credit.", "Come back when you're a little... mmm... richer!"]
    weights = [50, 50]

    rng = random.choices(msg, weights=weights, k=1)[0]
    print(rng)

# here is the players gold
starter_gold = 100
current_gold = 0
current_gold += starter_gold

current_hp = 0
starter_hp = 100
current_hp += starter_hp


# the dmg does not really matter, but for when i make a armour version the defence and hp could act as extra energy for fighting. 
# you have to buy equipment or else inventory wont have anything 
inventory = {
    "Weapon": None, 
    "Armour": None
    }

# if the inventory has a weapon it returns that weapon
def current_weapon():
    if inventory["Weapon"] is not None:
        return inventory["Weapon"]
    
    else:
        return None

# might have to get the defence stat aswell
def current_armour():
    if inventory["Armour"] is not None:
        return inventory["Armour"]

    else:
        return None



cart = []
while True:


    print(current_hp)
    s_or_f = store_or_fight_choice()

    # 1 is to enter the store
    if s_or_f == "1":
        while True:
            show_store()
            

            choice = input()
            # if the choice is a digit and if that digit fits in the stores lenght
            if choice.isdigit() and 1 <= int(choice) <= len(store):
                item = store[int(choice) - 1]

                #does the player have enough gold
                if current_gold >= item.price:
                    cart.append(item)
                    print(f"{item.name} added to cart\n\n")
                
                else: 
                    print("Not enough gold")
            
            else:
                print("\n\nInvalid")





            # if choice is 0 then exit
            if choice == "0":
                clear_terminal()

                # if the cart is empty you wont get a receipt for buying stuff
                if not cart:
                    print("Have a nice day!")
                    break

                
                # prints the receipt
                else:
                    # another cool way to clear out the terminal
                    #print("\x1b[2J\x1b[H", end="")

                    for item in cart:
                        print(f"\n-{item}:{item.price} Gold")

                    total_price = sum(item.price for item in cart) 

                    # if the player cant afford their cart
                    if total_price > current_gold:
                        store_clerk_not_enough_money_rng()
                        cart.clear()
                        break

                    else:
                        print(f"\nTotal: {total_price} Gold\nHave a nice day!")

                        current_gold -= total_price

                        for item in cart:

                            #replacing old armour, cant have swords that give health because it will also count
                            old_armour = inventory[item.item_type]
                            if old_armour is not None:
                                current_hp -= old_armour.hp
                            
                            current_hp += item.hp
                            inventory[item.item_type] = item

                        cart.clear()
                        break



    # this is how you get money, for now im thinking that the player gets a random amount of money but uses 1 energy bar.
    if s_or_f == "2":

        # how much you lose per run
        # you start with 100 hp, when you buy armour that gets increased along with damage reduction.
        # alternitively i could make a player that stores weapon and armour. something like: player = [current_armour, current_weapon]
        # hp_loss / damage reduction = new hp loss
        
        
        # current_hp gets a bonus by armour_hp. lets say armour.hp = 15, then current_hp becomes 115.
        # the armour.de reduces incoming damage by hp_loss. lets say, armour.de = 5, then incoming damage with this armour would be:
        # player_health = 105 (5 because of defence) - 25 hp = 80 remaining hp    
        # so if i really want to i can just make the defence stat do devision, but for now it does the same as armour_hp    
        hp_loss = 25

        armour = current_armour()

        defence = armour.de if armour else 0

        after_armour_hp_loss = hp_loss - defence

        current_hp -= after_armour_hp_loss

        if current_hp <= 0:
            print("Game Over")
            break
        


        while True:
            # will make it so it consumes hp of off the player, and so better weapons yeild a better reward
             

            weapon = current_weapon()

            if weapon is None:
                current_gold += random.randint(1, 25)
                
            elif weapon.name == "Wood Sword":
            
                current_gold += random.randint(25, 50)

            hint_rng()
            print(f"\n{current_gold} Gold")
            break


