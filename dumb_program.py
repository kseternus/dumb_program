import tkinter as tk
import random


def dumb():

    for i in range(100):
        color = random.randint(111111, 999988)
        dumb_window = tk.Toplevel()
        dumb_window.geometry(f'500x600+{random.randint(0, 1960)}+{random.randint(0, 1000)}')
        dumb_window.config(background=f'#{color}')
        canvas = tk.Canvas(dumb_window, width=420, height=420, background='#000000')
        canvas.pack(pady=35)
        img = tk.PhotoImage(file=r'keksimus.gif')
        dumb_window.img = img
        canvas.create_image(0, 0, image=img, anchor='nw')
        dumb_trap = tk.Button(dumb_window, font='Futura 22', text='Close all windows ;)', background=f'#{color}',
                              activebackground=f'#{color + 11}', command=dumb)
        dumb_trap.pack()


def random_place():
    no_button.place(x=random.randint(50, 530), y=random.randint(100, 330))


root = tk.Tk()
root.title('dumb program')
root.geometry('600x400')
root.config(background='#a4ba97')
root.resizable(False, False)
root.config()


screen_frame = tk.LabelFrame(root, borderwidth=0, background='#a4ba97')
screen_frame.pack()

question = tk.Label(screen_frame, text='Are you dumb?', font='Futura 60', background='#a4ba97')
question.grid(row=0, column=0, pady=50)

yes_button = tk.Button(root, text='Yes', font='Futura 32', command=dumb, background='#a4ba97',
                       activebackground='#a4ba97')
yes_button.place(x=150, y=180)

no_button = tk.Button(root, text='No', font='Futura 32', command=random_place, background='#a4ba97',
                      activebackground='#a4ba97')
no_button.place(x=350, y=180)

root.mainloop()
