from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

TAN = "#FFF5E0"
PINK = "#FF6969"
RED = "#C70039"
DARK_BLUE = "#141E46"
LABEL_FONT = "ALIEN LEAGUE"
LABEL_SIZE = 14


# ---------------------------- PASSWORD GENERATOR --------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD -------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username}"
                                                                f" \nPassword: {password} \nIs it okay to save?")
        if is_okay:
            with open("data.txt", "a") as f:
                f.write(f"{website},{username},{password}\n")
                website_entry.delete(0, END)
                # username_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Create window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=PINK)

# Configure the grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
window.columnconfigure(2, weight=1)

# Create Canvas
canvas = Canvas(width=200, height=200, bg=PINK, highlightthickness=0)
logo_img = PhotoImage(file="logo2.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)

# Create labels
website_label = Label(text="Website:", bg=PINK, fg=DARK_BLUE, font=(LABEL_FONT, LABEL_SIZE, "bold"))
website_label.grid(row=1, column=0, padx=5, pady=5)

username_label = Label(text="Username:", bg=PINK, fg=DARK_BLUE, font=(LABEL_FONT, LABEL_SIZE, "bold"))
username_label.grid(row=2, column=0, padx=5, pady=5)

password_label = Label(text="Password:", bg=PINK, fg=DARK_BLUE, font=(LABEL_FONT, LABEL_SIZE, "bold"))
password_label.grid(row=3, column=0, padx=5, pady=5)

# Create Entry Boxes
website_entry = Entry(borderwidth=0, width=47, bg=TAN, font=(LABEL_FONT, 12, "bold"))
website_entry.grid(row=1, column=1, columnspan=2, sticky=W, padx=5, pady=5)
website_entry.focus()

username_entry = Entry(borderwidth=0, width=47, bg=TAN, font=(LABEL_FONT, 12, "bold"))
username_entry.insert(0, "astralplaydoh@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2, sticky=W, padx=5, pady=5)

password_entry = Entry(borderwidth=0, width=30, bg=TAN, font=(LABEL_FONT, 12, "bold"))
password_entry.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Create buttons
generate_password = Button(borderwidth=0, width=13, text="Generate", command=generate_password, font=(LABEL_FONT, 12, "bold"), bg=RED, fg="white")
generate_password.grid(row=3, column=2, sticky=W, padx=5, pady=5)

add_password = Button(borderwidth=0, width=42, text="Add", command=save, font=(LABEL_FONT, 12, "bold"), bg=RED, fg="white")
add_password.grid(row=4, column=1, columnspan=2, sticky=W, padx=5, pady=5)

# Window loop
window.mainloop()
