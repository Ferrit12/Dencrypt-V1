import tkinter as tk
from tkinter import filedialog
import random
import string
import pyperclip

def encrypt_file():
    key = key_entry.get()
    file_path = file_path_entry.get()
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted_data = bytearray()
    for b in data:
        encrypted_data.append(b + key)
    with open(file_path, 'wb') as f:
        f.write(encrypted_data)
    pyperclip.copy(key)

def decrypt_file():
    key = key_entry.get()
    file_path = file_path_entry.get()
    with open(file_path, 'rb') as f:
        data = f.read()
    decrypted_data = bytearray()
    for b in data:
        decrypted_data.append(b - key)
    with open(file_path, 'wb') as f:
        f.write(decrypted_data)

def browse_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File")
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, filename)

def encrypt_or_decrypt():
    if encrypt_var.get():
        encrypt_file()
    else:
        decrypt_file()

window = tk.Tk()
window.title("File Encryptor/Decryptor")
window.geometry("400x250")

# generate random key
key = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=32))

# key entry
key_label = tk.Label(window, text="Key:")
key_label.grid(column=0, row=0)

key_entry = tk.Entry(window)
key_entry.grid(column=1, row=0)
key_entry.insert(0, key)

# file path entry
file_path_label = tk.Label(window, text="File path:")
file_path_label.grid(column=0, row=1)

file_path_entry = tk.Entry(window)
file_path_entry.grid(column=1, row=1)

# browse button
browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.grid(column=2, row=1)

# replace checkbox
replace_var = tk.BooleanVar(value=True)
replace_checkbox = tk.Checkbutton(window, text="Replace original file", variable=replace_var)
replace_checkbox.grid(column=0, row=2, columnspan=2)

# encrypt checkbox
encrypt_var = tk.BooleanVar(value=True)
encrypt_checkbox = tk.Checkbutton(window, text="Encrypt", variable=encrypt_var)
encrypt_checkbox.grid(column=2, row=2)

# encrypt/decrypt button
encrypt_button = tk.Button(window, text="Encrypt/Decrypt", command=encrypt_or_decrypt)
encrypt_button.grid(column=1, row=4)

window.mainloop()