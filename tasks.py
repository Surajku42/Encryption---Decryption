import tkinter as tk
from tkinter import scrolledtext, messagebox


def caesar_cipher(text, shift, mode):
    result = ''
    for ch in text:
        if ch.isalpha():
            start = ord('A') if ch.isupper() else ord('a')
            if mode == 'encrypt':
                shifted = (ord(ch) - start + shift) % 26 + start
            else:  
                shifted = (ord(ch) - start - shift) % 26 + start
            result += chr(shifted)
        else:
            result += ch  
    return result


def encrypt_text():
    msg = input_text.get("1.0", tk.END).strip()
    if not msg:
        messagebox.showwarning("Input Missing", "Please enter some text to encrypt.")
        return
    shift = shift_value.get()
    encrypted = caesar_cipher(msg, shift, 'encrypt')
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted)

def decrypt_text():
    msg = input_text.get("1.0", tk.END).strip()
    if not msg:
        messagebox.showwarning("Input Missing", "Please enter some text to decrypt.")
        return
    shift = shift_value.get()
    decrypted = caesar_cipher(msg, shift, 'decrypt')
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted)

def clear_all():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)


root = tk.Tk()
root.title("Caesar Cipher Encryptor/Decryptor")
root.geometry("500x450")


tk.Label(root, text="Enter your message:").pack(pady=5)
input_text = scrolledtext.ScrolledText(root, width=60, height=5)
input_text.pack()


tk.Label(root, text="Shift value:").pack(pady=5)
shift_value = tk.IntVar(value=3)
tk.Scale(root, from_=1, to=25, orient='horizontal', variable=shift_value).pack()


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Encrypt", width=12, command=encrypt_text).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Decrypt", width=12, command=decrypt_text).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Clear", width=12, command=clear_all).grid(row=0, column=2, padx=5)


tk.Label(root, text="Output:").pack(pady=5)
output_text = scrolledtext.ScrolledText(root, width=60, height=5)
output_text.pack()

root.mainloop()
