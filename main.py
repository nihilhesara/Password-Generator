from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    # Password Generator Functionality
    # Lists of possible characters for the password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Randomly select the number of letters, symbols, and numbers
    num_letters = random.randint(8, 10)
    num_symbols = random.randint(2, 4)
    num_numbers = random.randint(2, 4)

    # Create lists of random characters based on the selected quantities
    password_letters = [random.choice(letters) for _ in range(num_letters)]
    password_symbols = [random.choice(symbols) for _ in range(num_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(num_numbers)]

    # Combine all characters and shuffle them
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    # Join the list into a single string
    password = "".join(password_list)

    # Insert the generated password into the password entry field
    password_entry.insert(0, password)

    # Copy the password to the clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Get the current values from the entry fields
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email":email,
            "password":password,
        }
    }

    # Check if any fields are empty
    if len(website) == 0 or len(password) == 0:
        # Show an error message if fields are empty
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        # Save the data to a file if user confirms
        with open("data.json", "r") as data_file:
            #json.dump(new_data,data_file,indent=4) # json.dump = file.write (dictionary name,file variable name,to indent and clear the output to user

            # Reading old data
            data = json.load(data_file)
            # Updating old data with new data
            data.update(new_data)
        
        with open("data.json", "w") as data_file:
            # Saving updated data
            json.dump(data,data_file,indent=4)

            # Clear the website and password entry fields after saving
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# Create the main window
window = Tk()
window.title("Password Generator")  # Set the title of the window
window.config(padx=50, pady=50)  # Add padding around the window content

# Create a canvas widget to display the lock image
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")  # Load the image from file (ensure the file path is correct)
canvas.create_image(100, 100, image=lock_image)  # Position the image in the center of the canvas
canvas.grid(column=1, row=0)  # Place the canvas in the grid layout

# Create and place the 'Website' label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="E")  # Align label to the right

# Create and place the entry widget for the website input
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2, sticky="W")  # Span across two columns and align left
website_entry.focus()  # Set focus on the website entry field

# Create and place the 'Email/Username' label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="E")  # Align label to the right

# Create and place the entry widget for the email/username input
email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2, sticky="W")  # Span across two columns and align left
email_entry.insert(0, "nihil@gmail.com")  # Pre-fill the email field with a default value

# Create and place the 'Password' label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="E")  # Align label to the right

# Create and place the entry widget for the password input
password_entry = Entry(width=25)  # A narrower input field since it will be next to a button
password_entry.grid(column=1, row=3, sticky="W")  # Align left

# Create and place the 'Generate Password' button
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="W")  # Position the button next to the password entry field

# Create and place the 'Add' button to save the data
add_button = Button(text="Add", width=40, command=save)  # The button spans the entire width under the input fields
add_button.grid(column=1, row=4, columnspan=2)

# Start the main event loop to make the window interactive
window.mainloop()
