import tkinter
from PIL import ImageTk, Image
import subprocess as sa

# GUI Window
main_window = tkinter.Tk()
main_window.title("Roman Numeral Converter")
main_window.geometry("900x600")
main_window.resizable(width=False, height=False)

image_file = "learn.png"
img = Image.open(image_file)
img = img.resize((900, 600))
photo = ImageTk.PhotoImage(img)

image_label = tkinter.Label(main_window, image=photo, bg="white")
image_label.place(relx=0.5, rely=0.5, anchor="center")
image_label.photo = photo

main_window.mainloop()
