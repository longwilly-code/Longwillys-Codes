import tkinter as tk
import random
from pathlib import Path
from tkinter import *
from PIL import ImageTk, Image
import winsound



class Game:
    def __init__(self, root):

        #--- game rules ---

        self.balance = 1000
        self.bet = 50

        self.symbols = ["🍒", "🍋", "🔔", "7"]

        self.roll1 = ()
        self.roll2 = ()
        self.roll3 = ()


        #-- gui ---
        self.root = root
        self.root.geometry("1200x800")
        self.root.resizable(False, False)

        




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
        self.pil_slot_img = self.pil_slot_img.resize((300, 600), Image.Resampling.LANCZOS)

        self.tk_slot_img = ImageTk.PhotoImage(self.pil_slot_img)

        self.slot_machine = tk.Label(self.root, image=self.tk_slot_img)
        self.slot_machine.image = self.tk_slot_img
        self.slot_machine.place(relx=0.5, rely=1,
                                anchor="s")
        


        
        
        
        #--- Sound ---

        #  #--- win sound (jackpot) ---
        self.jackpot_sound = self.folder / "floraphonic-playful-casino-slot-machine-jackpot-3-183921.wav"
        
        #--- payout sound ---
        self.payout_sound = self.folder / "floraphonic-jackpot-slot-machine-coin-loop-6-216072.wav"

        #--- spin sound ---
        self.spin_sound = self.folder / "mixkit-slot-machine-wheel-1932.wav"






        #--- balance label ---
        self.create_widget()

        # --- result label / animation label ---

        self.result_label = tk.Label(root,
                                     bg="blue",
                                     fg="gold",
                                     text="SPIN",
                                     font=("Arial", 18))
        self.result_label.place(relx=0.46, rely=0.4)

        # --- info label ---

        self.bet_info_label = tk.Label(root,
                                   text=f"{self.bet}⛃",
                                   font=("Arial", 10),
                                   bg="blue", fg="gold")
        self.bet_info_label.place(relx=0.49, rely=0.5)

        #--- buttons ---
        self.spin_btn = tk.Button(root,
                             text="spin",
                             bg="green", fg="orange",
                             command=lambda: self.spin())
        self.spin_btn.place(relx=0.49, rely=0.54)



        self.increse_bet_btn = tk.Button(root,
                                         text="+⛃",
                                         font=("Areal", 13),
                                         bg="orange", fg="green",
                                         command=lambda: self.increse_bet())
        self.increse_bet_btn.place(relx=0.55, rely=0.54)

        self.decrese_bet_btn = tk.Button(root,
                                         text="-⛃",
                                         font=("Areal", 13),
                                         bg="red", fg="gold",
                                         command=lambda: self.decrese_bet())
        self.decrese_bet_btn.place(relx=0.43, rely=0.53)

        


    # --- balance label 
    def create_widget(self):
        self.balance_label = tk.Label(self.root,
                                    text=f"Balance: {self.balance}⛃",
                                    font=("Arial", 13),
                                    bg="blue", fg="gold")
        self.balance_label.place(relx=0.45, rely=0.32)

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

        winsound.PlaySound(str(self.spin_sound), winsound.SND_FILENAME | winsound.SND_ASYNC)

        self.root.after(2000, self.stop_sound)
        
    
    def stop_sound(self):
        winsound.PlaySound(None, winsound.SND_PURGE)

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
            winsound.PlaySound(str(self.jackpot_sound), winsound.SND_FILENAME | winsound.SND_ASYNC)
            self.root.after(2000, lambda: winsound.PlaySound(str(self.payout_sound), winsound.SND_FILENAME | winsound.SND_ASYNC))

            self.balance += self.bet * 5
            
            self.result_label.config(text=f"Jackpot!")
            self.root.after(
                1000,
                lambda: self.result_label.config(
                    text=f"{self.roll1} {self.roll2} {self.roll3}"))

            self.upd_balance_label()

        #---Three of a Kind ---
        elif result == "three of a kind":
            winsound.PlaySound(str(self.payout_sound), winsound.SND_FILENAME | winsound.SND_ASYNC)
            self.balance += self.bet * 3

            self.result_label.config(text=f"Three of a Kind!")
            
            self.root.after(
                500,
                lambda: self.result_label.config(
                    text=f"{self.roll1} {self.roll2} {self.roll3}"))

        #--- Two of a Kind ---
        elif result == "two of a kind":
            winsound.PlaySound(str(self.payout_sound), winsound.SND_FILENAME | winsound.SND_ASYNC)
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