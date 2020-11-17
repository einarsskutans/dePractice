import googletrans
import tkinter as tk
from tkinter.filedialog import *
from tkinter import *

# Initialize Screen
screen = tk.Tk()
screen.geometry("1080x480")
screen.title("dePractice")
screen.resizable(width=FALSE, height=FALSE)
screen.config(bg="white")
dark = False

# Text Entry
text_entry = tk.Text(screen, width=54, height=104)
text_entry.pack(side="left")

# Scrollbar
scroll_bar = tk.Scrollbar(screen, orient="vertical", command=text_entry.yview)
scroll_bar.pack(side="left", fill="y")

text_entry.configure(yscrollcommand=scroll_bar.set)

# Live Translator
input_translate = tk.Text(screen, width=40, height=1)
input_translate.place(x=460, y=450)
translated_label = tk.Label()
quick_translator = tk.Label(text="Quick Translator", bg="white")
quick_translator.place(x=460, y=425)

lang1_label = tk.Label(bg='white', text='ENG')
lang2_label = tk.Label(bg='white', text='DEU')

switch = 0
source = 'en'
destination = 'de'


def invert():
    global switch
    global source
    global destination

    if switch == 0:
        switch = 1
        source = 'de'
        destination = 'en'
        lang1_label.config(text='DEU')
        lang2_label.config(text='ENG')
        print(source, destination)
        print(switch)
    elif switch == 1:
        switch = 0
        source = 'en'
        destination = 'de'
        lang1_label.config(text='ENG')
        lang2_label.config(text='DEU')
        print(source, destination)
        print(switch)


invert_button = tk.Button(text="⇄", command=invert)
invert_button.place(x=610, y=420)

lang1_label.place(x=580, y=420)
lang2_label.place(x=640, y=420)

tbg = 'white'
tfg = 'black'


def translate_command():
    translator = googletrans.Translator(service_urls=['translate.google.com'])
    saved_input = input_translate.get(0.0, END)
    print(saved_input)
    try:
        global tbg
        global tfg
        if dark == True:
            tbg = '#323232'
            tfg = 'white'
        else:
            tbg = 'white'
            tfg = 'black'
        translated_text = translator.translate(saved_input, src=source, dest=destination).text
        translated_label.config(text=translated_text, font="Arial 12", bg=tbg, fg=tfg)
        translated_label.place(x=800, y=420)
        print(translated_text)
    except AttributeError:
        screen.after(333, translate_command)


translate_button = tk.Button(text='Enter', command=translate_command)
translate_button.place(x=700, y=420)

# Button Commands
close_cases_button = tk.Button(screen, text="X", width=5, height=1)
img_cases = tk.PhotoImage(file="cases.gif")
cases_image = Label(screen, image=img_cases)


def close_cases():
    cases_image.pack_forget()
    close_cases_button.pack_forget()


close_cases_button.config(command=close_cases)


def cases():
    close_cases_button.pack()
    cases_image.pack(side="top")


def pronouns():
    screen_pronouns = tk.Toplevel()
    screen_pronouns.title("Possessive Pronouns")
    screen_pronouns.geometry("1064x623")
    screen_pronouns.resizable(width=FALSE, height=FALSE)

    img_pronouns = tk.PhotoImage(file="pp.gif")
    pronouns_image = Label(screen_pronouns, image=img_pronouns)
    pronouns_image.pack()

    screen_pronouns.mainloop()


# Grammar Buttons
cases = tk.Button(text="Cases", width=20, height=2, highlightthickness=0, command=cases)
cases.pack(side="top")
pronouns = tk.Button(text="Possessive Pronouns", width=20, height=2, highlightthickness=0, command=pronouns)
pronouns.place(x=540, y=0)


# File Managing/Defining Commands


def open_file(event=None):
    ask_open = askopenfile(mode='r')
    try:
        text = ask_open.read()
        ask_open.close()
        text_entry.delete(0.0, END)
        text_entry.insert(END, text)
    except AttributeError:
        print("Something happened, closed file explorer on opening process?")


def save_as_file(event=None):
    saved_as_text = text_entry.get(0.0, END)
    ask_save = asksaveasfile(mode='w', defaultextension=".txt")
    try:
        ask_save.write(saved_as_text)
        ask_save.close()
    except AttributeError:
        print("Something happened, closed file explorer on saving process?")
    print(saved_as_text)


# Theme Modes


def theme1_command():
    global dark
    dark = False
    screen.config(bg="white")
    text_entry.config(bg="white", fg="black")
    cases.config(bg="SystemButtonFace", fg="black")
    pronouns.config(bg="SystemButtonFace", fg="black")
    close_cases_button.config(bg="SystemButtonFace", fg="black")
    quick_translator.config(bg="white", fg="black")
    input_translate.config(bg="white", fg="black")
    translate_button.config(bg="SystemButtonFace", fg="black")
    lang1_label.config(bg="white", fg='black')
    lang2_label.config(bg="white", fg="black")
    translated_label.config(bg="white", fg="black")


def theme2_command():
    global dark
    dark = True
    screen.config(bg="#323232")
    text_entry.config(bg="#323232", fg='white')
    cases.config(bg="#323232", fg="white")
    pronouns.config(bg="#323232", fg="white")
    close_cases_button.config(bg="#323232", fg="white")
    quick_translator.config(bg="#323232", fg="white")
    input_translate.config(bg="gray", fg="white")
    translate_button.config(bg="#323232", fg="white")
    lang1_label.config(bg="#323232", fg="white")
    lang2_label.config(bg="#323232", fg="white")
    translated_label.config(bg="#323232", fg="white")


theme_button1 = tk.Button(screen, text="Light", width=5, height=2, command=theme1_command)
theme_button2 = tk.Button(screen, text="Dark", width=5, height=2, command=theme2_command)
theme_button1.place(x=1030, y=390)
theme_button2.place(x=1030, y=430)

# Menu
menu_bar = tk.Menu(screen)

file = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file)

file.add_command(label='Open...', command=open_file)
file.add_command(label='Save As', command=save_as_file)
file.add_separator()
file.add_command(label='Exit', command=screen.destroy)

# KeyBind
screen.bind("<Control-s>", save_as_file)
screen.bind("<Control-e>", open_file)

# Misc
screen.config(menu=menu_bar)
screen.mainloop()
