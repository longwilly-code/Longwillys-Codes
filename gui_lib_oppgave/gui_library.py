import tkinter as tk
from tkinter import messagebox
import json
from PIL import ImageTk, Image
from pathlib import Path



# two variables use current page, so best to use global
global current_page

current_page = 0
max_books_per_page = 5

def save_json():

    if not entry_book_pages.get().strip() or not entry_book_name.get().strip():
        return

    # checks if the page input is numbers.
    try:
        pages = int(entry_book_pages.get().strip())
    except ValueError:
        messagebox.showinfo("Error", "Not an int")
        return


    # if the page input is lower than 1 show an error
    if pages < 1:
        messagebox.showinfo("Error", "Books must atleast have one page.")
        return


    # how books get saved in the json and the json configs
    book_data = {
        "book_name": entry_book_name.get(),
        "pages": pages
    }



    json_book_list = []
        


    try:
        with open("library.json", "r", encoding="utf-8") as file:
            json_book_list = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        json_book_list = []

    json_book_list.append(book_data)


    

    with open("library.json", "w", encoding="utf-8") as file:
        json.dump(json_book_list, file, indent=4)

    messagebox.showinfo("Saved successful", "file saved as library.json")




def open_json():
    main_frame.forget()
    library_frame.pack()
    show_books()


def go_back():
    library_frame.forget()
    main_frame.pack()


def book_clicked(book_name, book_pages):
    messagebox.showinfo(f"Book: {book_name}", f"Pages: {book_pages}")




root = tk.Tk()
root.title("Library")
root.geometry("800x800")
root.resizable(False, False)


#background images: had to resize the jpg
lib_img_path = Path(__file__).parent / "library_img.jpg"
main_frame_bg = Image.open(lib_img_path)

main_frame_bg = main_frame_bg.resize((800, 800), Image.Resampling.LANCZOS)
main_frame_photo = ImageTk.PhotoImage(main_frame_bg)


#background for the json frame
json_img_path = Path(__file__).parent / "browse_lib_img.jpg"
json_img_bg = Image.open(json_img_path)

json_img_bg = json_img_bg.resize((800, 800), Image.Resampling.LANCZOS)
json_frame_photo = ImageTk.PhotoImage(json_img_bg)




# frames
main_frame = tk.Frame(root, width=800, height=800)
main_frame.propagate(False)
main_frame.pack()


library_frame = tk.Frame(root, width=800, height=800)
library_frame.propagate(False)
library_frame.pack()



# using the backgrounds
main_frame_background = tk.Label(main_frame,
                                 image=main_frame_photo)
main_frame_background.place(relheight=1, relwidth=1)

library_frame_background = tk.Label(library_frame,
                                    image=json_frame_photo)
library_frame_background.place(relheight=1, relwidth=1)




# hiding the frames
main_frame.forget()
library_frame.forget()

#show the main frame at the start
main_frame.pack()

# widget enteries
tk.Label(main_frame, text="book name:", font=("Arial", 20)).place(relx=0.5, rely=0.2, anchor="center")
entry_book_name = tk.Entry(main_frame)
entry_book_name.place(relx=0.5, rely=0.25, anchor="center")

tk.Label(main_frame, text="pages:", font=("Arial", 20)).place(relx=0.5, rely=0.3, anchor="center")
entry_book_pages = tk.Entry(main_frame)
entry_book_pages.place(relx=0.5, rely=0.35, anchor="center")






# save button
save_btn = tk.Button(main_frame,
                      text="Save", font=("Arial", 14), bg="Green",
                      command=save_json)
save_btn.place(relx=0.5, rely=0.5, anchor= "center")






# open library/json
open_lib_btn = tk.Button(main_frame,
                         text="Check library", font=("Arial", 14), bg="Blue",
                         command=open_json)
open_lib_btn.place(relx=0.5, rely=0.6, anchor="center")


# back button
back_btn = tk.Button(library_frame,
                     text="Back", font=("Arial", 14), bg="Green",
                     command=go_back)
back_btn.place(relx=0.1, rely=0.9, anchor="w")




# interactable books. 

def show_books():
    #delete all 'books' but keeps the buttons 'back', 'next', 'previous' and the background img 
    for widget in library_frame.winfo_children():
        if widget != back_btn and widget != next_page_btn and widget != previous_page_btn and widget != library_frame_background:
            widget.destroy()



    start = current_page * max_books_per_page
    end = start + max_books_per_page



    try:
        with open("library.json", "r") as file:
            books = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        books = []

    #slices the json so that only buttons that are ment to be created is created
    for book in books[start:end]:
        book_btn_name = book["book_name"]
        book_btn_pages = book["pages"]

        # shows the book as a button with the book name, when clicked it will pup up a msg box displaying its name and pages.
        btn = tk.Button(library_frame,
                        text=book_btn_name,
                        width=2,
                        height=2,
                        font=("Arial", 14), fg="White", bg="Black",
                        command=lambda book_name=book_btn_name, pages=book_btn_pages: book_clicked(book_name, pages))
        btn.pack(pady=30, fill=tk.X, padx=20)



    






# functions to go to the next page of books
def next_page():
    global current_page

    try:
        with open("library.json", "r") as file:
            books = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
            books = []

    books_len = len(books)

    if (current_page +1) * max_books_per_page < books_len:
        current_page += 1
    else:
        current_page == current_page



    show_books()

# goes back a page. if it is the page it stops you from going back
def previous_page():
    global current_page
    if current_page == 0:
        current_page = 0
    else:
        current_page -= 1 
        show_books()   

next_page_btn = tk.Button(library_frame,
                          text="Next", font=("Arial", 14),
                          command=next_page)
next_page_btn.place(relx=0.9, rely=0.9, anchor="center")

previous_page_btn = tk.Button(library_frame,
                              text="Previous", font=("Arial", 14),
                              command=previous_page)
previous_page_btn.place(relx=0.8, rely=0.9, anchor="center")

root.mainloop()