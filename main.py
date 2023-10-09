from tkinter import messagebox
from tkinter import *
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import random

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
    # password = ""
    # for char in password_list:
    #   password += char

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Empty fields are not allowed")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Are the entered details correct:\n\n Email: {email}\n"
                                                              f" Password = {password}")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website}, {email}, {password} \n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
photo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
email_input = Entry(width=35)
email_input.insert(0, "dheerajarya@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)
password_input = Entry(width=17)
password_input.grid(row=3, column=1)
gen_password = Button(text="Generate password", command=generate_password)
gen_password.grid(row=3, column=2)
add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
