from tkinter import *
from tkinter import messagebox


def isInt(n):
    if n == '':
        return -1
    if n.isnumeric():
        return int(n) == float(n)
    else:
        return -1


def calculate_meat():
    value_result['text'] = ''
    men_over_90 = -1
    men_down_90 = -1
    wmn_over_70 = -1
    wmn_down_70 = -1
    children = -1
    if isInt(men_90_value.get()):
        men_over_90 = int(men_90_value.get())
        if men_over_90 < 0:
            return messagebox.showinfo('Error')
    else:
        return messagebox.showinfo('Error')
    if isInt(men_value.get()) and men_value.get().isnumeric():
        men_down_90 = int(men_value.get())
        if men_down_90 < 0:
            return messagebox.showinfo('Error')
    else:
        return messagebox.showinfo('Error')
    if isInt(wmn_70_value.get()) and wmn_70_value.get().isnumeric():
        wmn_over_70 = int(wmn_70_value.get())
        if wmn_over_70 < 0:
            return messagebox.showinfo('Error')
    else:
        return messagebox.showinfo('Error')
    if isInt(wmn_value.get()) and wmn_value.get().isnumeric():
        wmn_down_70 = int(wmn_value.get())
        if wmn_down_70 < 0:
            return messagebox.showinfo('Error')
    else:
        return messagebox.showinfo('Error')
    if isInt(cdrn_value.get()) and cdrn_value.get().isnumeric():
        children = int(cdrn_value.get())
        if children < 0:
            return messagebox.showinfo('Error')
    else:
        return messagebox.showinfo('Error')
    result_value = (men_over_90 * 0.6) + (men_down_90 * 0.5) + (wmn_over_70 * 0.5) + (wmn_down_70 * 0.4) + (children * 0.3)
    result = str(result_value)
    value_result['text'] = result
    return


window = Tk()
window.geometry('400x400')
window.title("Калькулятор мяса для шашлыка")
frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)
men_90_ = Label(
    frame,
    text="Мужчин, весом более 90 кг "
)
men_90_.grid(row=3, column=1)
men_90 = Label(
    frame,
    text="Мужчин, весом менее 90 кг ",
)
men_90.grid(row=4, column=1)
wmn_70_ = Label(
    frame,
    text="Женщин, весом более 70 кг "
)
wmn_70_.grid(row=5, column=1)
wmn_70 = Label(
    frame,
    text="Женщин, весом менее 70 кг",
)
wmn_70.grid(row=6, column=1)
cdrn = Label(
    frame,
    text="Детей "
)
cdrn.grid(row=7, column=1)
men_90_value = Entry(
    frame
)
men_90_value.grid(row=3, column=2)
men_value = Entry(
    frame,
)
men_value.grid(row=4, column=2, pady=5)
wmn_70_value = Entry(
    frame,
)
wmn_70_value.grid(row=5, column=2, pady=5)
wmn_value = Entry(
    frame,
)
wmn_value.grid(row=6, column=2, pady=5)
cdrn_value = Entry(
    frame,
)
cdrn_value.grid(row=7, column=2, pady=5)
frame2 = Frame(
    window,
    padx=10,
    pady=10
)
frame2.pack(expand=True)
value_result = Label(
    frame2,
    text=''
)
cal_btn = Button(
    frame,
    text='Рассчитать',
    command=calculate_meat
)
value_result.pack()
cal_btn.grid(row=10, column=2)
label_result = Label(
    frame2,
    text="Необходимо кг мяса дял шашлыка: "
)
label_result.pack()
window.mainloop()
