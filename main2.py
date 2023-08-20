import tkinter
from PIL import ImageTk, Image
import subprocess as s

# GUI Window
main_window = tkinter.Tk()
main_window.title("Roman Numeral Converter")
main_window.geometry("900x600")
main_window.resizable(width=False, height=False)

image_file = "main2png.png"
img = Image.open(image_file)
img = img.resize((900, 600))
photo = ImageTk.PhotoImage(img)

image_label = tkinter.Label(main_window, image=photo, bg="white")
image_label.place(relx=0.5, rely=0.5, anchor="center")
image_label.photo = photo

# Conversion logic for Roman numeral to decimal
def convert_to_decimal(roman_numeral):
    roman_symbols = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    decimal_number = 0
    i = 0
    while i < len(roman_numeral):
        if i + 1 < len(roman_numeral) and roman_numeral[i:i + 2] in roman_symbols:
            decimal_number += roman_symbols[roman_numeral[i:i + 2]]
            i += 2
        else:
            decimal_number += roman_symbols[roman_numeral[i]]
            i += 1

    return decimal_number

def rotate():
    main_window.destroy()
    s.Popen(['python', "main.py"])

def on_convert():
    roman_number = entry_roman.get()
    if is_roman_numeral(roman_number):
        decimal_number = convert_to_decimal(roman_number)
        entry_decimal.delete(0, tkinter.END)
        entry_decimal.insert(tkinter.END, decimal_number)
    else:
        entry_decimal.delete(0, tkinter.END)
        entry_decimal.insert(tkinter.END, "Invalid Input")


# Check if a string is a valid Roman numeral
def is_roman_numeral(roman_numeral):
    valid_symbols = "IVXLCDM"
    for char in roman_numeral:
        if char not in valid_symbols:
            return False
    return True


# Entry for Roman numeral
entry_roman = tkinter.Entry(main_window, width=20, bg="white", fg="black")
entry_roman.place(x=255, y=210, anchor="center")

# Output for decimal number
entry_decimal = tkinter.Entry(main_window, width=20, bg="white", fg="black")
entry_decimal.place(x=255, y=360, anchor="center")

# Convert button
convert_button = tkinter.Button(main_window, width=5, text="Convert", bg='red', command=on_convert)
convert_button.place(x=660, y=190)

# Rotate button
rotate_button = tkinter.Button(main_window, width=5, text="Rotate", bg='red', command=rotate)
rotate_button.place(x=660, y=286)

# Learn button
def learnwindow():
    main_window.destroy()
    s.Popen(['python', "learn.py"])
convert_button = tkinter.Button(main_window, width=5, text="Learn", bg='red',command=learnwindow)
convert_button.place(x=660, y=380)


main_window.mainloop()
