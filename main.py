from tkinter import *
from tkinter import messagebox
import time
window = Tk()
window.title("CPM by Lakvinu")
window.state('zoomed')
def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'

window.configure(background=rgbtohex(43,135,209))
window.resizable(0,0)
main_label = Label(window, text = "Start", font=("Arial",40,'bold'), bg=rgbtohex(43,135,209), fg = 'white')
main_label.place(anchor = "center", relx = 0.5, rely = 0.5)

stage = 0
def effect():
    global stage
    stage = 2
    result()

def result():
    global stage
    cur = int(main_label['text'])
    res = cur / 10
    messagebox.showinfo("Result", "Your Result is \n" + str(res))
    stage = 3


def first():
    window.configure(background=rgbtohex(43,135,209))


def command_function(event):
    global stage

    if stage == 0:
        window.after(10000, effect)
        stage = 1
        main_label['text'] = "0"

    if stage == 1:
        res = int(main_label['text']) + 1
        main_label['text'] = str(res)

    if stage == 3:
        stage = 0


window.bind("<Button-1>", command_function)


window.mainloop()