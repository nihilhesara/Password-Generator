from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# This section is reserved for the password generator functionality.
# You can implement functions to generate a random, secure password here.

# ---------------------------- SAVE PASSWORD ------------------------------- #
# This section is reserved for the save password functionality.
# You can implement functions to save the password to a file or database here.

# ---------------------------- UI SETUP ------------------------------- #
# Create the main window
window = Tk()
window.title("Password Generator")  # Set the title of the window
window.config(padx=20, pady=20)  # Add padding around the window content

# Create a canvas widget to display the lock image
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")  # Load the image from file (ensure the file path is correct)
canvas.create_image(100, 100, image=lock_image)  # Position the image in the center of the canvas
canvas.grid(column=1, row=0)  # Place the canvas in the grid layout

# Create and place the 'Website' label
website_label = Label(text="Website :")
website_label.grid(column=0, row=1)

# Create and place the entry widget for the website input
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)  # Spanning across two columns for a wider input field

# Create and place the 'Email/Username' label
email_label = Label(text="Email/Username :")
email_label.grid(column=0, row=2)

# Create and place the entry widget for the email/username input
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)  # Spanning across two columns for a wider input field

# Create and place the 'Password' label
password_label = Label(text="Password :")
password_label.grid(column=0, row=3)

# Create and place the entry widget for the password input
password_entry = Entry(width=21)  # A narrower input field since it will be next to a button
password_entry.grid(column=1, row=3)

# Create and place the 'Generate Password' button
password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3)  # Position the button next to the password entry field

# Create and place the 'Add' button to save the data
add_button = Button(text="Add", width=36)  # The button spans the entire width under the input fields
add_button.grid(column=1, row=4, columnspan=2)

# Start the main event loop to make the window interactive
window.mainloop()
