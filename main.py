import tkinter as tk
from tkinter import messagebox
from random import choice, shuffle
import pyperclip
import json

from cipher import encode, decode

UPPERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
          'V', 'W', 'X', 'Y', 'Z']
LOWERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Generate Random Password
def generate_pwd():
    chars = list(choice(choice((UPPERS, LOWERS, NUMBERS, SYMBOLS))) for _ in range(12))
    chars.append(choice(UPPERS))
    chars.append(choice(LOWERS))
    chars.append(choice(NUMBERS))
    chars.append(choice(SYMBOLS))
    shuffle(chars)
    password = ''.join(chars)
    entry_pwd.delete(0, 'end')
    entry_pwd.insert(0, password)
    pyperclip.copy(password)


# Add password
def add_pwd():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_pwd.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please make sure you haven't left any fields empty.")
    else:
        for char in password:
            if not any((char in UPPERS, char in LOWERS, char in NUMBERS, char in SYMBOLS)):
                messagebox.showerror(title="Wrong Char", message="All Characters must be Letter or number or symbol")
                break
        else:
            new_data = {
                website: {
                    'email': email,
                    'password': encode(password)
                }
            }
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                entry_website.delete(0, 'end')
                entry_pwd.delete(0, 'end')


# get password
def get_pwd():
    website = entry_website.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = decode(data[website]["password"])
            pyperclip.copy(password)
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# region User Interface
root = tk.Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)

# image
canvas = tk.Canvas(height=166, width=220)
image = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
label_website = tk.Label(text="Website      :", padx=12, pady=10)
label_website.grid(row=1, column=0, sticky="W")
label_email = tk.Label(text="Email          :", padx=12, pady=10)
label_email.grid(row=2, column=0, sticky="W")
label_pwd = tk.Label(text="Password    :", padx=12, pady=10)
label_pwd.grid(row=3, column=0, sticky="W")

# Entries
entry_website = tk.Entry()
entry_website.grid(row=1, column=1, sticky="EW")
entry_website.focus()
entry_email = tk.Entry()
entry_email.grid(row=2, column=1, columnspan=2, sticky="EW")
entry_email.insert(0, "ilyassari@mail.com")
entry_pwd = tk.Entry(width=21)
entry_pwd.grid(row=3, column=1, sticky="EW")

# Buttons
button_get = tk.Button(text="Get", padx=6, command=get_pwd)
button_get.grid(row=1, column=2, sticky="EW")
button_gen_pwd = tk.Button(text="Generate Password", padx=6, command=generate_pwd)
button_gen_pwd.grid(row=3, column=2, sticky="EW")
button_add = tk.Button(text="Add", command=add_pwd)
button_add.grid(row=4, column=1, columnspan=2, sticky="EW")
# endregion

root.mainloop()
