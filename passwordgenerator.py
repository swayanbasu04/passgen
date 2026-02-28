import tkinter as tk
from tkinter import messagebox
import string as s
import secrets

def create_password(length: int, symbols: bool, uppercase: bool):
    # Define the base character set
    combination = s.ascii_lowercase + s.digits + s.punctuation 

    # Add uppercase letters if specified
    if uppercase:
        combination += s.ascii_uppercase
    # Add punctuation if specified
    if symbols:
        combination += s.punctuation 

    password = ''.join(
        combination[secrets.randbits(12)%len(combination)] for _ in range(length))
    return password

# User input

def generate_password():
    try:
        password_length = int(password_length_entry.get())
        if password_length <= 0:
            raise ValueError("Length must be a positive integer")
        include_symbols = symbols_var.get()
        include_uppercase = uppercase_var.get()
        
        generated_password = create_password(password_length, include_symbols, include_uppercase)
        output_text.delete(1.0, tk.END)  # Clear previous outputs
        output_text.insert(tk.END, f"Generated Password: {generated_password}\n")

        # Generating 5 additional passwords
        output_text.insert(tk.END, "\nGenerating 5 additional passwords:\n")
        for index in range(5):
            random_password = create_password(password_length, include_symbols, include_uppercase)
            output_text.insert(tk.END, f"{index + 1} >> {random_password}\n")
    
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
def copy_clipboard():
     copytext=output_text.get(1.0, tk.END).strip()
     if copytext:
         root.clipboard_clear()
         root.clipboard_append(copytext)
         messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Passphrase Generator")

#widgets
password_length_label = tk.Label(root, text="Enter desired passphrase length:", bg="white", fg="black")
password_length_label.pack(pady=10)

password_length_entry = tk.Entry(root)
password_length_entry.pack(pady=10)
generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.pack(pady=10)


symbols = ["Include symbols?", "Include uppercase letters?"]
checkboxes = {}
for symbol in symbols:
     var = tk.BooleanVar()
     chk = tk.Checkbutton(root, text=symbol, variable=var)  # Fixed here
     chk.pack(anchor=tk.W)
     checkboxes[symbol] = var

symbols_var = tk.BooleanVar()
uppercase_var = tk.BooleanVar()

symbols_checkbox = tk.Checkbutton(root, text="Include symbols?", variable=symbols_var)
symbols_checkbox.pack(anchor=tk.W)

uppercase_checkbox = tk.Checkbutton(root, text="Include uppercase letters?", variable=uppercase_var)
uppercase_checkbox.pack(anchor=tk.W)

output_text = tk.Text(root, height=10, width=50)
output_text.pack(pady=10)

clip_button= tk.Button(root, text="copy to clipboard", command=copy_clipboard)
clip_button.pack(pady=5)

root.mainloop()

