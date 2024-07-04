from tkinter import *
tk = Tk()

tk.geometry('1200x600')
mashina = []
canvas = Canvas(tk, height=550, width=1200, bg="Blue")
def drow_car():
    btn_drow.config(state="disable")
    btn_start.config(state ="normal")
    canvas.place(x=0, y=50)
    canvas.create_rectangle((0, 440), (1200, 600), fill='grey')
    #кузов машины
    points = ((60,400),(490,400),(490,285),(475,233),(360,217),(360,345),(60,345),(60,400))
    mashina.append(canvas.create_polygon(*points, outline="#313939", width=6, fill='Gray'))


#площадка под цестерной
    mashina.append(canvas.create_rectangle((120,330),(280,345), outline="#313939", width=6, fill='Black'))

#цестерна
    mashina.append(canvas.create_rectangle((65,212),(338,331), outline="#313939", width=4, fill='#FFD700'))
#колеса
    mashina.append(canvas.create_oval(74, 440, 153, 365, fill='black', outline='black'))
    mashina.append(canvas.create_oval(161, 440, 242, 365, fill='black', outline='black'))
    mashina.append(canvas.create_oval(393, 440, 475, 365, fill='black', outline='black'))
    mashina.append(canvas.create_oval(90, 381, 136, 425, fill='GRAY', outline='black'))
    mashina.append(canvas.create_oval(179, 381, 225, 425, fill='GRAY', outline='black'))
    mashina.append(canvas.create_oval(412, 381, 458, 425, fill='GRAY', outline='black'))
    mashina.append(canvas.create_oval(423, 391, 447, 414, fill='black', outline='black'))
    mashina.append(canvas.create_oval(190, 391, 214, 414, fill='black', outline='black'))
    mashina.append(canvas.create_oval(101, 391, 125, 414, fill='black', outline='black'))
#текст
    mashina.append(canvas.create_text(115, 254, font="Arial 24", anchor=NW, text="Доставка", fill="#004D40"))

def move_car():
    global speed
    btn_start.config(state="disabled")
    for i in mashina:
        canvas.move(i,speed,0)
    if ((canvas.coords(mashina[0])[2] >= 1200) or (canvas.coords(mashina[0])[0] <= 0)):
        speed *=-1
    canvas.after(100,move_car)


speed = 8
btn_drow = Button(tk,text = "Нарисовать",command = drow_car)
btn_drow.place(x = 120, y = 10)
btn_start = Button(tk, state = "disabled" ,text="Запустить",command = move_car)
btn_start.place(x = 10,y = 10)
tk.mainloop()

