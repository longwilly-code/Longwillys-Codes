import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path
import random



class Game:
    def __init__(self, root):
        self.root = root
        
        

        # ---Game state---
        self.symbols = ["cherry", "lemon", "bell", "star", "7"]
        self.chips = 100
        self.bet = 10
        self.spinning = False

        #---UI---
        self.reel1 = tk.Label(root, text="?", font=("Arial", 30))
        self.reel2 = tk.Label(root, text="?", font=("Arial", 30))
        self.reel3 = tk.Label(root, text="?", font=("Arial", 30))

        self.reel1.grid(row=0, column=0, padx=10)
        self.reel2.grid(row=0, column=1, padx=10)
        self.reel3.grid(row=0, column=2, padx=10)

        #--- Game Label (is going to update the user on all types of info.)--- 
        self.info = tk.Label(root,
                              text=self.status_text(),
                              font=("Arial", 15),)
        self.info.grid(row=1, column=0, columnspan=3)


        self.spin_btn = tk.Button(root, text="SPIN", command=self.start_spin)
        self.spin_btn.grid(row=2, column=1)

    
    
    def status_text(self):
        return f"Balance: {self.chips} | Bet: {self.bet}"
    

    #---Betting---

    def change_bet(self, amount):
        self.bet = max(1, self.bet + amount)

        self.info.config(text=self.status_text())

    
    #---Spinning---

    def start_spin(self):
        if self.spinning:
            return
        if self.chips < self.bet:
            self.info.config(text="Not enough chips")
            return
        
        self.chips -= self.bet
        self.spinning = True
        self.spinning_animation(0)


    def spin_animation(self, ticks):
        if ticks < 10:
            
            self.reel1.config(text=random.choice(self.symbols))
            self.reel2.config(text=random.choice(self.symbols))
            self.reel3.config(text=random.choice(self.symbols))

            self.root.after(100, lambda: self.spin_animation(ticks + 1))
        else:
            self.finish_spin()



    
    def finish_spin(self):
        #--- final symbol ---
        r1 = random.choice(self.symbols)
        r2 = random.choice(self.symbols)
        r3 = random.choice(self.symbols)

        self.reel1.config(text=r1)
        self.reel2.config(text=r2)
        self.reel3.config(text=r3)


        if r1 == r2 == r3:
            win = self.bet * 5
            self.chips += win

            self.info.config(text=f"JACKPOT!!! + {win} CHIPS")
        else:
            loss_msg = ["Damn you lost to the BAD B$LL", "Scammer gets scammed", "XD", "Xd", "Thanks$$", "lol"]
            self.info.config(text=random.choice(loss_msg))


        self.spinning = False



#--- Path for images ---
folder = Path(__file__).parent

# --- Images ---
casino_img_path = folder / "casino_img.webp"


#--- GUI ---

root = tk.Tk()
root.title("Slots!!!")
root.geometry("1200x800")

# --- bridge the image, cuz for some reason tk hates .webp files :( ---
pil_img = Image.open(casino_img_path)
pil_img = pil_img.resize((1200, 800), Image.Resampling.LANCZOS)

tk_img = ImageTk.PhotoImage(pil_img)

bg_label = tk.Label(root, image=tk_img)
bg_label.image = tk_img
bg_label.pack(fill="both", expand=True)












game = Game(root)
root.mainloop()