import tkinter
from PIL import ImageTk, Image
import subprocess as s

# GUI Window
main_window = tkinter.Tk()
main_window.title("Roman Numeral Converter")
main_window.geometry("900x600")
main_window.resizable(width=False, height=False)

image_file = "mainpng.png"
img = Image.open(image_file)
img = img.resize((900, 600))
photo = ImageTk.PhotoImage(img)

image_label = tkinter.Label(main_window, image=photo, bg="white")
image_label.place(relx=0.5, rely=0.5, anchor="center")
image_label.photo = photo

# Conversion logic for decimal to Roman numeral
def convert_to_roman(decimal_number):
    roman_symbols = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    roman_numeral = ""
    for value, symbol in roman_symbols.items():
        while decimal_number >= value:
            roman_numeral += symbol
            decimal_number -= value

    return roman_numeral

def rotate():
    main_window.destroy()
    s.Popen(['python', "main2.py"])

def on_convert():
    decimal_number_str = entry_decimal.get()
    try:
        decimal_number = int(decimal_number_str)
        roman_number = convert_to_roman(decimal_number)
        entry_roman.delete(0, tkinter.END)
        entry_roman.insert(tkinter.END, roman_number)
    except ValueError:
        entry_roman.delete(0, tkinter.END)
        entry_roman.insert(tkinter.END, "Invalid Input")

# Entry for decimal number
entry_decimal = tkinter.Entry(main_window, width=20, bg="white", fg="black")
entry_decimal.place(x=255, y=210, anchor="center")

# Output for Roman number
entry_roman = tkinter.Entry(main_window, width=20, bg="white", fg="black")
entry_roman.place(x=255, y=360, anchor="center")

# Convert button
convert_button = tkinter.Button(main_window, width=5, text="Convert", bg='red', command=on_convert)
convert_button.place(x=660, y=190)

# Rotate button
convert_button = tkinter.Button(main_window, width=5, text="Rotate", bg='red',command=rotate)
convert_button.place(x=660, y=286)

# Learn button
def learnwindow():
    main_window.destroy()
    s.Popen(['python', "learn.py"])


convert_button = tkinter.Button(main_window, width=5, text="Learn", bg='red',command=learnwindow)
convert_button.place(x=660, y=380)



main_window.mainloop()
