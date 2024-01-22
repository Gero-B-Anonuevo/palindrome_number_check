import tkinter as tk 
from tkinter import simpledialog

number = tk.simpledialog.askinteger("Hello!", "Input your number: ")
reverse_number_string = str(number)[::-1]
if number == float:
    reverse_number = float(reverse_number_string)
else:
    reverse_number = int(reverse_number_string)

print("Original number: ", number)
if number == reverse_number:
    print("Yes, the number is a palindrome number")
else:
    print("No, the number is not a palindrome number")