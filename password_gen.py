import string, random, pyperclip, tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.withdraw()

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
digits = list(string.digits)
symbols = list(string.punctuation)
merged = lower + upper + digits + symbols
def generate(length=10):
    password = []
    global merged
    for x in range(length):
        password.append(random.choice(merged))
    pyperclip.copy(''.join(str(x)for x in password))
generate()
messagebox.showinfo('Success!!!', "New password copied to clipboard!")