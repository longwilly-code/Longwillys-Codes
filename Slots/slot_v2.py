import tkinter as tk
import random
from pathlib import Path
from tkinter import *
from PIL import ImageTk, Image
import time

class Game:
    def __init__(self, root):

        #--- game rules ---

        self.balance = 1000
        self.bet = 50

        self.symbols = ["🍒", "🍋", "🔔", "7"]

        self.roll1 = ()
        self.roll2 = ()
        self.roll3 = ()


        #-- gui
        self.root = root
        self.root.geometry("1200x800")

        

        #--- images---
        self.folder = Path(__file__).parent
        
        self.casino_img_path = self.folder / "casino_img.webp"
        

        self.pil_img = Image.open(self.casino_img_path)
        self.pil_img = self.pil_img.resize((1200, 800), Image.Resampling.LANCZOS)
        
        self.tk_img = ImageTk.PhotoImage(self.pil_img)
        
        # --- background image ---
        self.bg_label = tk.Label(self.root, image=self.tk_img)
        self.bg_label.image = self.tk_img
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        
        
        #--- slot machine ---
        self.slot_machine_img_path = self.folder / "badbill.png"

        self.pil_slot_img = Image.open(self.slot_machine_img_path)
        self.pil_slot_img = self.pil_slot_img.resize((200, 500), Image.Resampling.LANCZOS)

        self.tk_slot_img = ImageTk.PhotoImage(self.pil_slot_img)

        self.slot_machine = tk.Label(root, image=self.tk_slot_img)
        self.slot_machine.image = self.tk_slot_img
        self.slot_machine.pack()

        
        #--- balance label ---
        self.create_widget()

        # --- result label / animation label ---

        self.result_label = tk.Label(root,
                                     bg="blue",
                                     fg="gold",
                                     text="SPIN",
                                     font=("Arial", 20))
        self.result_label.pack()

        # --- info label ---

        self.bet_info_label = tk.Label(root,
                                   text=f"{self.bet}⛃",
                                   font=("Arial", 10))
        self.bet_info_label.pack()

        #--- buttons ---
        self.spin_btn = tk.Button(root,
                             text="spin",
                             command=lambda: self.spin())
        self.spin_btn.pack()



        self.increse_bet_btn = tk.Button(root,
                                         text="+⛃",
                                         command=lambda: self.increse_bet())
        self.increse_bet_btn.pack()

        self.decrese_bet_btn = tk.Button(root,
                                         text="-⛃",
                                         command=lambda: self.decrese_bet())
        self.decrese_bet_btn.pack()

        


    # --- balance label 
    def create_widget(self):
        self.balance_label = tk.Label(self.root,
                                    text=f"Balance: {self.balance}⛃",
                                    font=("Arial", 20))
        self.balance_label.pack()

    # --- update balance label
    def upd_balance_label(self):
        self.balance_label.config(
            text=f"Balance: {self.balance}")
        


    def increse_bet(self):
        if self.bet < 100:
            self.bet += 25
        
        if self.bet == 100:
            self.bet_info_label.config(text="You cannot increase bet over 100 chips⛃")
            self.root.after(
                500,
                lambda: self.bet_info_label.config(text=f"{self.bet}⛃")
            )

        self.bet_info_label.config(text=f"{self.bet}⛃")

    def decrese_bet(self):
        if self.bet > 50:
            self.bet -= 25

       
        if self.bet == 50:
            self.bet_info_label.config(text="You cannot decrease bet under 50 chips⛃")
            self.root.after(
                500,
                lambda: self.bet_info_label.config(text=f"{self.bet}⛃")
            )

        self.bet_info_label.config(text=f"{self.bet}⛃")
            




    #--- spin logic ---
    # --- need to add cooldown ---
    def spin(self):
        self.spin_ani(0)
        
        
    def spin_ani(self, ticks):
        if ticks < 20:
    
            self.roll1 = random.choice(self.symbols)
            self.roll2 = random.choice(self.symbols)
            self.roll3 = random.choice(self.symbols)
            
            self.result_label.config(
                text=f"{self.roll1} {self.roll2} {self.roll3}")
            
            self.root.after(100,
                            lambda: self.spin_ani(ticks + 1))
        

        else:
            self.roll_slots()
            
            self.result_label.config(
                text=f"{self.roll1} {self.roll2} {self.roll3}")
            
            self.payout()
           


    # --- roll the 3 slots ---
    def roll_slots(self):
        
        self.roll1 = random.choice(self.symbols)
        self.roll2 = random.choice(self.symbols)
        self.roll3 = random.choice(self.symbols)
        

    # --- checks if the 3 slots win ---
    def check_win(self):
        if self.roll1 == self.roll2 == self.roll3 == "7":
            return "jackpot"
        elif self.roll1 == self.roll2 == self.roll3 != "7":
            return "three of a kind"
        elif self.roll1 == self.roll2 or self.roll1 == self.roll3 or self.roll2 == self.roll3:
            return "two of a kind"
        else:
            return "Loss"
                
    
    def payout(self):

        result = self.check_win()
        #---Jackpot---
        if result == "jackpot":
            self.balance += self.bet * 5
            
            self.result_label.config(text=f"Jackpot!")
            self.root.after(
                1000,
                lambda: self.result_label.config(
                    text=f"{self.roll1} {self.roll2} {self.roll3}"))

            self.upd_balance_label()

        #---Three of a Kind ---
        elif result == "three of a kind":
            self.balance += self.bet * 3

            self.result_label.config(text=f"Three of a Kind!")
            
            self.root.after(
                500,
                lambda: self.result_label.config(
                    text=f"{self.roll1} {self.roll2} {self.roll3}"))

        #--- Two of a Kind ---
        elif result == "two of a kind":
            self.balance += self.bet

            self.result_label.config(text=f"Two of a Kind!")
            
            self.root.after(
                500,
                lambda: self.result_label.config(
                    text=f"{self.roll1} {self.roll2} {self.roll3}"))

        #--- Nothing xD ---
        else:
            self.balance -= self.bet        
            self.result_label.config(text=f"{self.roll1} {self.roll2} {self.roll3}")


        self.upd_balance_label()


root = tk.Tk()
game = Game(root)
root.mainloop()