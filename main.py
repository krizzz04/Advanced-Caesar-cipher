import tkinter as tk
from tkinter import messagebox
import pyperclip

def caesar_cipher(text, shift, direction):
    result = ""
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            if direction == "encrypt":
                shifted = (ord(char) - start + shift) % 26 + start
            elif direction == "decrypt":
                shifted = (ord(char) - start - shift) % 26 + start
            result += chr(shifted)
        else:
            result += char
    
    return result

def perform_cipher():
    text = message_entry.get()
    shift = shift_entry.get()
    
    try:
        shift = int(shift)
        if shift < 1 or shift > 25:
            raise ValueError
        
        if action.get() == "Encrypt":
            result = caesar_cipher(text, shift, "encrypt")
        else:
            result = caesar_cipher(text, shift, "decrypt")
        
        result_label.config(text=f"Result: {result}")
        window.update()
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid shift value (1-25).")

def copy_to_clipboard():
    result_text = result_label.cget("text").replace("Result: ", "")
    if result_text:
        pyperclip.copy(result_text)
        messagebox.showinfo("Copied", "Result copied to clipboard!")

# Create the main window
window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("500x400")
window.configure(bg='#2b2b2b')  # Dark background for a modern look

# Title Label
title_label = tk.Label(window, text="Caesar Cipher Tool", font=("Helvetica", 22, 'bold'), fg='#00ffcc', bg='#2b2b2b')
title_label.pack(pady=20)

# Message Entry
message_label = tk.Label(window, text="Enter your message:", font=("Helvetica", 14), fg='#00ffcc', bg='#2b2b2b')
message_label.pack(pady=10)
message_entry = tk.Entry(window, width=50, font=("Helvetica", 14))
message_entry.pack(pady=5)

# Shift Entry
shift_label = tk.Label(window, text="Enter shift value (1-25):", font=("Helvetica", 14), fg='#00ffcc', bg='#2b2b2b')
shift_label.pack(pady=10)
shift_entry = tk.Entry(window, width=5, font=("Helvetica", 14))
shift_entry.pack(pady=5)

# Action Buttons
action = tk.StringVar()
action.set("Encrypt")
encrypt_button = tk.Radiobutton(window, text="Encrypt", variable=action, value="Encrypt", font=("Helvetica", 14), fg='#00ffcc', bg='#2b2b2b', selectcolor='#444444')
encrypt_button.pack(pady=5)
decrypt_button = tk.Radiobutton(window, text="Decrypt", variable=action, value="Decrypt", font=("Helvetica", 14), fg='#00ffcc', bg='#2b2b2b', selectcolor='#444444')
decrypt_button.pack(pady=5)

# Perform Button
perform_button = tk.Button(window, text="Perform", command=perform_cipher, font=("Helvetica", 14), bg='#00ffcc', fg='#2b2b2b', activebackground='#444444', activeforeground='#00ffcc')
perform_button.pack(pady=20)

# Result Label
result_label = tk.Label(window, text="Result: ", font=("Helvetica", 15), fg='#00ffcc', bg='#2b2b2b')
result_label.pack(pady=10)

# Copy Button
copy_button = tk.Button(window, text="Copy", command=copy_to_clipboard, font=("Helvetica", 14), bg='#00ffcc', fg='#2b2b2b', activebackground='#444444', activeforeground='#00ffcc')
copy_button.pack(pady=10)

# Start the GUI loop
window.mainloop()
