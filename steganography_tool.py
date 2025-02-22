from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from stegano import lsb

#Main window
win = Tk()
win.geometry('850x600')
win.title("Steganography Tool")
win.config(bg='#1e1e1e')

#Global var
hide_msg = None
open_file = None


def open_img():
    global open_file
    open_file = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           title='Select Image File',
                                           filetypes=(('PNG file', '*.png'), ('JPG file', '*.jpg')))
    if open_file:
        img = Image.open(open_file)
        img = img.resize((300, 220), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        img_label.config(image=img)
        img_label.image = img


def hide_and_save():
    global hide_msg
    if not open_file:
        messagebox.showerror('Error', 'Image not selected! Please choose an image first.')
        return

    password = code.get()
    if password == '0000':
        msg = text_input.get(1.0, END).strip()
        if not msg:
            messagebox.showerror('Error', 'Please enter a message to hide.')
            return
        hide_msg = lsb.hide(str(open_file), msg)
        hide_msg.save('Secret_image.png')
        messagebox.showinfo('Success', 'Message hidden and image saved successfully.')
        reset()
    elif not password:
        messagebox.showerror('Error', 'Please enter a secret key.')
    else:
        messagebox.showerror('Error', 'Wrong Secret Key.')
        code.set('')


def show():
    password = code.get()
    if password == '0000':
        if open_file:
            show_msg = lsb.reveal(open_file)
            text_input.delete(1.0, END)
            text_input.insert(END, show_msg)
        else:
            messagebox.showerror('Error', 'No image selected.')
    elif not password:
        messagebox.showerror('Error', 'Please enter a secret key.')
    else:
        messagebox.showerror('Error', 'Wrong Secret Key.')
        code.set('')


def reset():
    global hide_msg, open_file
    hide_msg = None
    open_file = None
    img_label.config(image='')
    text_input.delete(1.0, END)
    code.set('')
    messagebox.showinfo('Reset', 'Application has been reset!')


# Logo
logo = ImageTk.PhotoImage(Image.open('logo.jpg'))
logo_label = Label(win, image=logo, width=60, height=60, bd=0, bg='#1e1e1e')
logo_label.place(x=150, y=20)

# Heading
heading = Label(win, text='STEGANOGRAPHY TOOL', font='Helvetica 24 bold', fg='#f1f1f1', bg='#1e1e1e')
heading.place(x=230, y=30)


#Imageframe
img_frame = Frame(win, width=320, height=240, bd=5, bg='#3a3a3a', relief=SOLID)
img_frame.place(x=80, y=130)
img_label = Label(img_frame, bg='#3a3a3a')
img_label.place(x=0, y=0, width=310, height=230)

#Textframe
text_frame = Frame(win, width=320, height=150, bd=5, bg='#3e3e3e', relief=SOLID)
text_frame.place(x=460, y=130)
text_input = Text(text_frame, font='Arial 14', wrap=WORD, bd=2, relief=GROOVE, fg='#f1f1f1', bg='#2a2a2a')
text_input.place(x=0, y=0, width=310, height=140)

#keybox
Label(win, text='Enter Secret Key:', font='Arial 12', fg='#f1f1f1', bg='#1e1e1e').place(x=460, y=300)
code = StringVar()
entry = Entry(win, textvariable=code, bd=2, font='Arial 12', show='*', relief=SOLID)
entry.place(x=590, y=300, width=120)


# Button Hover Effects
def button_style(event):
    event.widget.config(bg='#555555')


def reset_button_style(event):
    event.widget.config(bg='#444444')


#Buttons
button_frame = Frame(win, bg='#1e1e1e')
button_frame.place(x=180, y=450)

buttons = [
    ("Open Image", open_img),
    ("Hide & Save", hide_and_save),
    ("Show Data", show),
    ("Reset", reset)
]

for i, (text, cmd) in enumerate(buttons):
    btn = Button(button_frame, text=text, bg='#444444', fg='#f1f1f1', font='Arial 12 bold', cursor='hand2',
                 relief=SOLID, bd=0, command=cmd, width=12, height=2)
    btn.grid(row=0, column=i, padx=10)
    btn.bind("<Enter>", button_style)
    btn.bind("<Leave>", reset_button_style)

#main loop
win.mainloop()
