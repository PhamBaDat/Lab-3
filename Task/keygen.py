import tkinter as tk
import random
import string
import pygame
import os
from PIL import Image, ImageTk

SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = "[033[H"

RED = "#c6260d"
WHITE = "#ffffff"
BLACK = "#000000"
GREEN = "#22e11f"
YELLOW = "#fef65b"
BLUE = "#2a7cc1"

directory_path = os.path.dirname(__file__) if '__file__' in globals() else os.getcwd()
icon_path = os.path.join(directory_path, 'icon.ico')
image_path = os.path.join(directory_path, 'image.png')
music_path = os.path.join(directory_path, 'Spin The Wheel.mp3')
original_image = Image.open(image_path)

def resize_image(event):
    new_width = event.width
    new_height = event.height
    resized_image = original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    root.bg_img = ImageTk.PhotoImage(resized_image)
    label.config(image = root.bg_img)

def init_GUI():
    global root, label
    root =  tk.Tk()
    root.title("Keygen")
    root.geometry("1000x800")

    #set icon
    root.iconbitmap(icon_path)

    #set background
    root.bg_img = ImageTk.PhotoImage(file = image_path)
    label = tk.Label(root, image = root.bg_img)
    label.pack(fill='both', expand = True)
    
    root.bind('<Configure>', resize_image)

def keyGenerate():
    alphabet = string.ascii_uppercase
    letter1 = random.choice(alphabet)
    letter2 = random.choice(alphabet)
    
    num1 = ord(letter1) - ord("A") + 1
    if num1 < 10:
        num1_fix = f'0{num1}'
    else: num1_fix = num1
    num2 = ord(letter2) - ord("A") + 1
    if num2 < 10:
        num2_fix = f'0{num2}'
    else: num2_fix = num2

    while letter1 == letter2:
        letter2 = random.choice(alphabet)
        num2 = ord(letter2) - ord("A") + 1

    if num1 < num2:
        interval = alphabet[num1 - 1: num2]
    else:
        interval = alphabet[num2 - 1: num1]


    part = "".join(random.choices(interval, k=7))
    key = f'{num1_fix} {part} {num2_fix}'

    key_entry.delete(0, tk.END)
    key_entry.insert(0, key)

def exit(music, root):
    music.stop()
    root.destroy()

def clear(show_key):
    key_entry.delete(0, tk.END)

if __name__ == '__main__':
    init_GUI()

    frame = tk.Frame(root, bg=BLACK, width=300, height=100)
    frame.place(relx=0.2, rely=1, anchor='s', y=-20)

    key_entry = tk.Entry(frame, width=25, font=("Cambria", 15), bg=YELLOW, justify="center")
    key_entry.place(relx=0.5, rely=0.2, anchor="n")

    key_gen_button = tk.Button(frame, text="Generate Key", width=12, bg=BLUE, fg=WHITE, command=keyGenerate)
    key_gen_button.place(relx=0.2, rely=0.7, anchor="center")

    clear_button = tk.Button(frame, text='CLEAR',width=8, command=lambda: clear(key_entry))
    clear_button.place(relx=0.55, rely=0.7, anchor="center")

    close_button = tk.Button(frame, text="EXIT", width=8, bg=RED, command=lambda: exit(pygame.mixer.music, root))
    close_button.place(relx=0.85, rely=0.7, anchor="center")


    # Initialize Pygame mixer
    pygame.mixer.init()
    # Load and play background music 
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)  # -1 means loop indefinitely

    root.mainloop()
