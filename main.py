from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)

    #automatic password copying
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #saving updated data
                json.dump(new_data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0,END)

def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(message=f"Website: {website}\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
pass_img = PhotoImage(file='logo.png')
canvas.create_image(120, 90, image=pass_img)
canvas.grid(column=1,row=0)

#labels
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

#buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2,row=3)
search_button = Button(text="Search", command=find_password, width=13)
search_button.grid(column=2,row=1)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1,row=4, columnspan=2)

#entries
website_input = Entry(width=20, bg="#A9A9A9", fg="black")
website_input.grid(column=1, row=1)
website_input.focus()
email_input = Entry(width=37, bg="#A9A9A9", fg="black")
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "dworak404@gmail.com")
password_input = Entry(width=20, bg="#A9A9A9", fg="black")
password_input.grid(column=1, row=3)






window.mainloop()