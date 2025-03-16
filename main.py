from audioop import add
from string import hexdigits
from tkinter import *
from tkinter import messagebox
from turtle import width
from unittest import mock
from tkinter import messagebox
import random
import pyperclip3
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip3.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get().capitalize()
    username = username_entry.get()
    password = password_entry.get()
    msg = f"\n Do you want to save these details?"
    detail = f"You entered the following:\n Username/Email: {username}\n Password: {password}"
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }
    if website == "" or password == "":
        messagebox.showwarning(title="Empty field",
                               message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=msg, detail=detail)
        if is_ok:
            try:
                with open('data.json', 'r') as file:
                    data = json.load(file)  # Reading old data
                    data.update(new_data)  # Updating old data with new data
            except FileNotFoundError:
                with open('data.json', mode='w') as file:
                    # Creating a new file and updating data
                    json.dump(new_data, file, indent=4)
            else:
                with open('data.json', mode='w') as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)

            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
# ---------------------------- Search login infos ------------------------------- #


def search():
    website = website_entry.get().capitalize()
    if website == "":
        messagebox.showwarning(title="Empty field",
                               message="Please enter the website name!")
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)  # Reading old data
        except FileNotFoundError:
            msg_error1 = "No data file found. Please insert some entries"
            messagebox.showerror(title="Empty Database",
                                 message=msg_error1, icon='error')
        else:
            try:
                msg_info = "Login credentials:"
                detail_info = f"Username: {data[website]['email']}\n Password: {data[website]['password']}"
                messagebox.showinfo(
                    title=website, message=msg_info, detail=detail_info)
            except KeyError:
                msg_error2 = "The entered website is not found in the database"
                messagebox.showerror(
                    title="Website Not Found", message=msg_error2, icon='error')

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1)

username_label = Label(text='Email/Username:')
username_label.grid(column=0, row=2)

username_entry = Entry(width=39)
username_entry.insert(0, "user0@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_pass_btn = Button(text='Generate Password', command=gen_pass)
generate_pass_btn.grid(column=2, row=3)

add_btn = Button(text='Add', width=37, command=save)
add_btn.grid(column=1, columnspan=2, row=4)

search_btn = Button(text='Search', width=15, command=search)
search_btn.grid(column=2, columnspan=2, row=1)


window.mainloop()
