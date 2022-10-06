import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(width=300, height=300, bg='white')
canvas.pack()

ball_r = canvas.create_oval(5, 5, 15, 15, fill='red')
ball_g = canvas.create_oval(5, 5, 15, 15, fill='green')
ball_b = canvas.create_oval(5, 5, 15, 15, fill='blue')


def motion_r():
    canvas.move(ball_r, 1, 0)
    if canvas.coords(ball_r[2]) > 300:
        canvas.coords(ball_r, 5, 5, 15, 15)
    canvas.after(100, motion_r)
def motion_g():
    canvas.move(ball_g, 0, 1)
    if canvas.coords(ball_g)[3] > 300:
        canvas.coords(ball_g, 5, 5, 15, 15)
    canvas.after(100, motion_g)
def motion_b():
    canvas.move(ball_b, 1, 1)
    if canvas.coords(ball_b)[2] > 300 or canvas.coords(ball_b)[3] > 300:
        canvas.coords(ball_b, 5, 5, 15, 15)
    canvas.after(100, motion_b)
motion_r()
motion_g()
motion_b()

window.mainloop()
