# ~~~~~~made by shivam mishra~~~~~~
# ------------------------main compontent-------------

from tkinter import *
import math
import tkinter.messagebox

# ~~~~~~~~main window
root = Tk()
root.title("Calculator")
root.geometry("365x535+350+100")
root.resizable(0, 0)
# -------------definations--------------


def btn1_clicked():
    if entry.get() == "0":
        entry.delete(0, END)
    lenght = len(entry.get())
    entry.insert(lenght, "1")


def btn2_clicked():
    if entry.get() == "0":
        entry.delete(0, END)
    lenght = len(entry.get())
    entry.insert(lenght, "2")


def btn3_clicked():
    if entry.get() == "0":
        entry.delete(0, END)
    lenght = len(entry.get())
    entry.insert(lenght, "3")


def btn4_clicked():
    if entry.get() == "0":
        entry.delete(0, END)
    lenght = len(entry.get())
    entry.insert(lenght, "4")


def btn5_clicked():
    if entry.get() == "0":
        entry.delete(0, END)
    lenght = len(entry.get())
    entry.insert(lenght, "5")


def btn6_clicked():
    if entry.get() == "0":
        entry.delete(0, END)
    lenght = len(entry.get())
    entry.insert(lenght, "6")


def btn7_clicked():
    if entry.get() == "0":
        entry.delete(0, END)
    lenght = len(entry.get())
    entry.insert(lenght, "7")


def btn8_clicked():
    if entry.get() == "0":
        entry.delete(0, END)
    lenght = len(entry.get())
    entry.insert(lenght, "8")


def btn9_clicked():
    if entry.get() == "0":
        entry.delete(0, END)
    lenght = len(entry.get())
    entry.insert(lenght, "9")


def btn0_clicked():
    if entry.get() == "0":
        pass
    else:
        lenght = len(entry.get())
        entry.insert(lenght, "0")


def btn_plus_clicked():
    all_text = entry.get()
    last = all_text[-1:]
    if last in ["+", "-", "*", "/"]:
        pass
    else:
        if entry.get() == "0":
            pass
        else:
            lenght = len(entry.get())
            entry.insert(lenght, "+")


def btn_minus_clicked():
    all_text = entry.get()
    last = all_text[-1:]
    if last in ["+", "-", "*", "/"]:
        pass
    else:
        if entry.get() == "0":
            pass
        else:
            lenght = len(entry.get())
            entry.insert(lenght, "-")


def btn_multiply_clicked():
    all_text = entry.get()
    last = all_text[-1:]
    if last in ["+", "-", "*", "/"]:
        pass
    else:
        if entry.get() == "0":
            pass
        else:
            lenght = len(entry.get())
            entry.insert(lenght, "*")


def btn_divide_clicked():
    all_text = entry.get()
    last = all_text[-1:]
    if last in ["+", "-", "*", "/"]:
        pass
    else:
        if entry.get() == "0":
            pass
        else:
            lenght = len(entry.get())
            entry.insert(lenght, "/")


def b1_clicked():
    if entry.get() == "0":
        entry.delete(0, END)
    lenght = len(entry.get())
    entry.insert(lenght, "(")


def b2_clicked():
    if entry.get == "0":
        entry.delete(0, END)
    lenght = len(entry.get())
    entry.insert(lenght, ")")


def C_clicked():
    entry.delete(0, END)
    entry.insert(0, "0")
    result.delete(0, END)
    result.insert(0, "0")


def back_clicked():
    lenght = len(entry.get())
    entry.delete(lenght - 1, END)
    if lenght == 1:
        entry.insert(0, "0")


def dot_clicked():
    all_text = entry.get()
    last = all_text[-1:]
    if last == ".":
        pass
    else:
        lenght = len(entry.get())
        entry.insert(lenght, ".")


histroy = []


def eq_clicked():
    try:
        if entry.get() == "()":
            tkinter.messagebox.showerror(
                "You Fool", "Please Enter Some function Between Brakets"
            )
            entry.delete(0, END)
            entry.insert(0, "0")
        lenght = entry.get()
        ans = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, "0")
        result.delete(0, END)
        result.insert(0, str(ans))
        histroy.append(lenght)
        histroy.reverse()
        status.configure(text="History : " + "|".join(histroy), font="Arial 20 bold")
    except Exception:
        tkinter.messagebox.showerror(
            "Value Error", "Check Your Value,Symbol Or Operator"
        )


def key_event(*args):
    if entry.get() == "0":
        entry.delete(0, END)


def standard():
    root.geometry("365x535+350+100")


def scientific():
    root.geometry("760x535+350+100")

    def sin_clicked():
        try:
            if switch is None:
                lenght = "Sin(" + entry.get() + ")"
                lengt = float(entry.get())
                ans = math.sin(lengt)
                entry.delete(0, END)
                entry.insert(0, "0")
                result.delete(0, END)
                result.insert(0, str(ans))
            else:
                lenght = "Sin(" + entry.get() + "°" + ")"
                lengt = float(entry.get())
                ans = math.sin(math.radians(lengt))
                entry.delete(0, END)
                entry.insert(0, "0")
                result.delete(0, END)
                result.insert(0, str(ans))
            histroy.append(lenght)
            histroy.reverse()
            status.configure(
                text="History : " + "|".join(histroy), font="Arial 20 bold"
            )
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your value and operator")

    def cos_clicked():
        try:
            if switch is None:
                lenght = "Cos(" + entry.get() + ")"
                lengt = float(entry.get())
                ans = math.cos(lengt)
                entry.delete(0, END)
                entry.insert(0, "0")
                result.delete(0, END)
                result.insert(0, str(ans))
            else:
                lenght = "Cos(" + entry.get() + "°" + ")"
                lengt = float(entry.get())
                ans = math.cos(math.radians(lengt))
                entry.delete(0, END)
                entry.insert(0, "0")
                result.delete(0, END)
                result.insert(0, str(ans))
            histroy.append(lenght)
            histroy.reverse()
            status.configure(
                text="History : " + "|".join(histroy), font="Arial 20 bold"
            )
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your value and operator")

    def tan_clicked():
        try:
            if switch is None:
                lenght = "Tan(" + entry.get() + ")"
                lengt = float(entry.get())
                ans = math.tan(lengt)
                entry.delete(0, END)
                entry.insert(0, "0")
                result.delete(0, END)
                result.insert(0, str(ans))
            else:
                lenght = "Tan(" + entry.get() + "°" + ")"
                lengt = float(entry.get())
                ans = math.tan(math.radians(lengt))
                entry.delete(0, END)
                entry.insert(0, "0")
                result.delete(0, END)
                result.insert(0, str(ans))
            histroy.append(lenght)
            histroy.reverse()
            status.configure(
                text="History : " + "|".join(histroy), font="Arial 20 bold"
            )
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your value and operator")

    def cosec_clicked():
        try:
            if switch is None:
                lenght = "Cosec(" + entry.get() + ")"
                lengt = float(entry.get())
                ans = (math.sin(lengt)) ** -1
                entry.delete(0, END)
                entry.insert(0, "0")
                result.delete(0, END)
                result.insert(0, str(ans))
            else:
                lenght = "Cosec(" + entry.get() + "°" + ")"
                lengt = float(entry.get())
                ans = (math.sin(math.radians(lengt))) ** -1
                entry.delete(0, END)
                entry.insert(0, "0")
                result.delete(0, END)
                result.insert(0, str(ans))
            histroy.append(lenght)
            histroy.reverse()
            status.configure(
                text="History : " + "|".join(histroy), font="Arial 20 bold"
            )
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your value and operator")

    def sec_clicked():
        try:
            if switch is None:
                lenght = "Sec(" + entry.get() + ")"
                lengt = float(entry.get())
                ans = (math.cos(lengt)) ** -1
                entry.delete(0, END)
                entry.insert(0, "0")
                result.delete(0, END)
                result.insert(0, str(ans))
            else:
                lenght = "Sec(" + entry.get() + "°" + ")"
                lengt = float(entry.get())
                ans = (math.cos(math.radians(lengt))) ** -1
                entry.delete(0, END)
                entry.insert(0, "0")
                result.delete(0, END)
                result.insert(0, str(ans))
            histroy.append(lenght)
            histroy.reverse()
            status.configure(
                text="History : " + "|".join(histroy), font="Arial 20 bold"
            )
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your value and operator")

    def cot_clicked():
        try:
            if switch is None:
                lenght = "Cot(" + entry.get() + ")"
                lengt = float(entry.get())
                ans = (math.tan(lengt)) ** -1
                entry.delete(0, END)
                entry.insert(0, "0")
                result.delete(0, END)
                result.insert(0, str(ans))
            else:
                lenght = "Cot(" + entry.get() + "°" + ")"
                lengt = float(entry.get())
                ans = (math.tan(math.radians(lengt))) ** -1
                entry.delete(0, END)
                entry.insert(0, "0")
                result.delete(0, END)
                result.insert(0, str(ans))
            histroy.append(lenght)
            histroy.reverse()
            status.configure(
                text="History : " + "|".join(histroy), font="Arial 20 bold"
            )
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your value and operator")

    def conv_clicked():
        global switch
        if switch is None:
            switch = True
            btn_cov["text"] = "Deg"
        else:
            switch = None
            btn_cov["text"] = "Rad"

    def ln_clicked():
        try:
            leb = "ln(" + entry.get() + ")"
            lengt = float(entry.get())
            ans = math.log(lengt)
            result.delete(0, END)
            result.insert(0, str(ans))
            entry.delete(0, END)
            entry.insert(0, "0")
            histroy.append(leb)
            histroy.reverse()
            status.configure(
                text="History : " + "|".join(histroy), font="Arial 20 bold"
            )
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check Your Value and Operator")

    def fac_clicked():
        lenght = int(entry.get())
        if lenght < 0:
            tkinter.messagebox.showerror(
                "Error", "Factorial Is Not Available For Negative Value"
            )
        elif lenght == 0:
            entry.delete(0, END)
            result.delete(0, END)
            result.insert(0, "1")
            entry.insert(0, "0")
        else:
            ans = math.factorial(lenght)
            entry.delete(0, END)
            result.delete(0, END)
            result.insert(0, str(ans))
            entry.insert(0, "0")

    def pi_clicked():
        if entry.get() == "0":
            entry.delete(0, END)
            entry.insert(0, str(math.pi))
        else:
            lenght = len(entry.get())
            entry.insert(lenght, str(math.pi))

    def per_clicked():
        if entry.get() == "0":
            pass
        else:
            lenght = float(entry.get())
            al = lenght / 100
            entry.delete(0, END)
            entry.insert(0, str(al))

    def e_clicked():
        if entry.get() == "0":
            entry.delete(0, END)
        lenght = len(entry.get())
        entry.insert(lenght, str(math.e))

    def log_clicked():
        try:
            lenght = "log(" + entry.get() + ")"
            lengt = int(entry.get())
            if lengt < 0:
                tkinter.messagebox.showerror("value error", "enter the positive value")
            else:
                ans = math.log10(lengt)
                entry.delete(0, END)
                entry.insert(0, "0")
                result.delete(0, END)
                result.insert(0, str(ans))
            histroy.append(lenght)
            histroy.reverse()
            status.configure(
                text="History : " + "|".join(histroy), font="Arial 20 bold"
            )
        except Exception:
            tkinter.messagebox.showerror("Error", "Check Your Value And Operator")

    def pow_clicked():
        lenght = len(entry.get())
        entry.insert(lenght, "**")

    def rot_clicked():
        lenght = int(entry.get())
        ans = (lenght) ** 0.5
        entry.delete(0, END)
        entry.insert(0, "0")
        result.delete(0, END)
        result.insert(0, ans)

    def round_clicked():
        lenght = float(result.get())
        ans = round(lenght)
        result.delete(0, END)
        result.insert(0, ans)

    btn_row_8 = Frame(root, bg="#fff800")
    btn_row_8.place(x=400, y=10, height=110, width=350)

    btn_row_9 = Frame(root, bg="#fff800")
    btn_row_9.place(x=400, y=140, height=50, width=350)

    btn_row_10 = Frame(root, bg="#fff800")
    btn_row_10.place(x=400, y=210, height=50, width=350)

    btn_row_11 = Frame(root, bg="#fff800")
    btn_row_11.place(x=400, y=280, height=50, width=350)

    btn_row_12 = Frame(root, bg="#fff800")
    btn_row_12.place(x=400, y=350, height=50, width=350)

    btn_row_13 = Frame(root, bg="#fff800")
    btn_row_13.place(x=400, y=420, height=50, width=350)

    label_1 = Label(
        btn_row_8,
        bg="#ff0000",
        bd=5,
        text="Scientific Part ",
        relief=GROOVE,
        font="Arial 30 bold ",
    )
    label_1.pack(expand=TRUE, side=LEFT, fill=BOTH)

    btn_sin = Button(
        btn_row_9,
        bg="red",
        bd=5,
        text="sin",
        relief=GROOVE,
        font="Arial 20 bold ",
        command=sin_clicked,
    )
    btn_sin.pack(expand=TRUE, side=LEFT, fill=BOTH)

    btn_cos = Button(
        btn_row_9,
        bg="red",
        bd=5,
        text="cos",
        relief=GROOVE,
        font="Arial 20 bold ",
        command=cos_clicked,
    )
    btn_cos.pack(expand=TRUE, side=LEFT, fill=BOTH)

    btn_tan = Button(
        btn_row_9,
        bg="red",
        bd=5,
        text="tan",
        relief=GROOVE,
        font="Arial 20 bold ",
        command=tan_clicked,
    )
    btn_tan.pack(expand=TRUE, side=LEFT, fill=BOTH)

    btn_cosec = Button(
        btn_row_10,
        bg="red",
        bd=5,
        text="sin^-1",
        relief=GROOVE,
        font="Arial 17 bold ",
        command=cosec_clicked,
    )
    btn_cosec.pack(expand=TRUE, side=LEFT, fill=BOTH)

    btn_sec = Button(
        btn_row_10,
        bg="red",
        bd=5,
        text="cos^-1",
        relief=GROOVE,
        font="Arial 17 bold ",
        command=sec_clicked,
    )
    btn_sec.pack(expand=TRUE, side=LEFT, fill=BOTH)

    btn_cot = Button(
        btn_row_10,
        bg="red",
        bd=5,
        text="tan^-1",
        relief=GROOVE,
        font="Arial 17 bold ",
        command=cot_clicked,
    )
    btn_cot.pack(expand=TRUE, side=LEFT, fill=BOTH)

    btn_cov = Button(
        btn_row_11,
        text="Rad",
        font="Arial 20 bold",
        relief=GROOVE,
        bd=5,
        command=conv_clicked,
        bg="#ff0000",
    )
    btn_cov.pack(side=LEFT, expand=TRUE, fill=BOTH)

    btn_ln = Button(
        btn_row_11,
        text="ln",
        font="Arial 20 bold",
        relief=GROOVE,
        bd=5,
        command=ln_clicked,
        bg="#ff0000",
    )
    btn_ln.pack(side=LEFT, expand=TRUE, fill=BOTH)

    btn_fac = Button(
        btn_row_11,
        text="X!",
        font="Arial 20 bold",
        relief=GROOVE,
        bd=5,
        command=fac_clicked,
        bg="#ff0000",
    )
    btn_fac.pack(side=LEFT, expand=TRUE, fill=BOTH)

    btn_pi = Button(
        btn_row_12,
        text="π",
        font="Arial 20 bold",
        relief=GROOVE,
        bd=5,
        command=pi_clicked,
        bg="#ff0000",
    )
    btn_pi.pack(side=LEFT, expand=TRUE, fill=BOTH)

    btn_per = Button(
        btn_row_12,
        text="%",
        font="Arial 20 bold",
        relief=GROOVE,
        bd=5,
        command=per_clicked,
        bg="#ff0000",
    )
    btn_per.pack(side=LEFT, expand=TRUE, fill=BOTH)

    btn_e = Button(
        btn_row_12,
        text="e",
        font="Arial 20 bold",
        relief=GROOVE,
        bd=5,
        command=e_clicked,
        bg="#ff0000",
    )
    btn_e.pack(side=LEFT, expand=TRUE, fill=BOTH)

    btn_log = Button(
        btn_row_13,
        text="log",
        font="Arial 20 bold",
        relief=GROOVE,
        bd=5,
        command=log_clicked,
        bg="#ff0000",
    )
    btn_log.pack(side=LEFT, expand=TRUE, fill=BOTH)

    btn_pow = Button(
        btn_row_13,
        text="X^Y",
        font="Arial 20 bold",
        relief=GROOVE,
        bd=5,
        command=pow_clicked,
        bg="#ff0000",
    )
    btn_pow.pack(side=LEFT, expand=TRUE, fill=BOTH)

    btn_rot = Button(
        btn_row_13,
        text="√x",
        font="Arial 20 bold",
        relief=GROOVE,
        bd=5,
        command=rot_clicked,
        bg="#ff0000",
    )
    btn_rot.pack(side=LEFT, expand=TRUE, fill=BOTH)

    btn_round = Button(
        btn_row_13,
        text="round",
        font="Arial 20 bold",
        relief=GROOVE,
        bd=5,
        command=round_clicked,
        bg="#ff0000",
    )
    btn_round.pack(side=LEFT, expand=TRUE, fill=BOTH)


def heloo():
    responce = tkinter.messagebox.askokcancel(
        "You Need Help ? ", "Kindly Contact Shivam Mishra"
    )
    if responce == 1:
        tkinter.messagebox.showinfo("Info", "Contact at '<shivamyash742@gmail.com>'")
    else:
        pass


def clear_H():
    histroy.clear()
    status.config(text="History :")


my_menu = Menu(root, bg="black")
root.config(menu=my_menu)

# create a menu item
file_menu = Menu(my_menu, bg="red")
my_menu.add_cascade(label="file", menu=file_menu)

file_menu.add_command(label="standard", command=standard)
file_menu.add_separator()
file_menu.add_command(label="scientific", command=scientific)
file_menu.add_separator()
file_menu.add_command(label="Clear History", command=clear_H)
file_menu.add_separator()
file_menu.add_command(label="exit", command=root.quit)

my_menu_2 = Menu(my_menu)
my_menu.add_cascade(label="help", menu=my_menu_2)
my_menu_2.add_command(label="help", command=heloo)

btn_row_1 = Frame(root, bg="#ffff00")
btn_row_1.place(x=8, y=10, height=50, width=350)

btn_row_2 = Frame(root, bg="#ffff00")
btn_row_2.place(x=8, y=70, height=50, width=350)

btn_row_3 = Frame(root, bg="#ffff00")
btn_row_3.place(x=8, y=140, height=50, width=350)

btn_row_4 = Frame(root, bg="#ffff00")
btn_row_4.place(x=8, y=210, height=50, width=350)

btn_row_5 = Frame(root, bg="#ffff00")
btn_row_5.place(x=8, y=280, height=50, width=350)

btn_row_6 = Frame(root, bg="#ffff00")
btn_row_6.place(x=8, y=350, height=50, width=350)

btn_row_7 = Frame(root, bg="#ffff00")
btn_row_7.place(x=8, y=420, height=50, width=350)

# -----------------entry and result--------------------

switch = None

entry = Entry(
    btn_row_1, bg="red", bd=5, relief=GROOVE, font="Arial 20 bold", justify=RIGHT
)
entry.bind("<Return>", eq_clicked)
entry.bind("<Escape>", C_clicked)
entry.bind("<Key-1>", key_event)
entry.bind("<Key-2>", key_event)
entry.bind("<Key-3>", key_event)
entry.bind("<Key-4>", key_event)
entry.bind("<Key-5>", key_event)
entry.bind("<Key-6>", key_event)
entry.bind("<Key-7>", key_event)
entry.bind("<Key-8>", key_event)
entry.bind("<Key-9>", key_event)
entry.bind("<Key-0>", key_event)
entry.bind("<Key-.>", key_event)
entry.bind("<Key-(>", key_event)
entry.bind("<Key-)>", key_event)
entry.insert(0, "0")
entry.focus_set()
entry.pack(expand=TRUE, fill=BOTH)

label = Label(
    btn_row_2, bg="red", bd=5, relief=GROOVE, font="Arial 20 bold ", text="Result : → "
)
label.pack(expand=TRUE, fill=BOTH, side=LEFT)

result = Entry(
    btn_row_2, bg="red", relief=GROOVE, bd=4, font="Arial 20 bold", justify=RIGHT
)
result.pack(expand=TRUE, fill=BOTH)
result.insert(0, "0")

btn_1 = Button(
    btn_row_3,
    bg="red",
    bd=3,
    text="1",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=btn1_clicked,
)
btn_1.pack(expand=TRUE, side=LEFT, fill=BOTH)

btn_2 = Button(
    btn_row_3,
    bg="red",
    bd=3,
    text="2",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=btn2_clicked,
)
btn_2.pack(expand=TRUE, side=LEFT, fill=BOTH)

btn_3 = Button(
    btn_row_3,
    bg="red",
    bd=3,
    text="3",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=btn3_clicked,
)
btn_3.pack(expand=TRUE, side=LEFT, fill=BOTH)

btn_p = Button(
    btn_row_3,
    bg="red",
    bd=3,
    text="+",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=btn_plus_clicked,
)
btn_p.pack(expand=TRUE, side=LEFT, fill=BOTH)

btn_4 = Button(
    btn_row_4,
    bg="red",
    bd=3,
    text="4",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=btn4_clicked,
)
btn_4.pack(expand=TRUE, side=LEFT, fill=BOTH)

btn_5 = Button(
    btn_row_4,
    bg="red",
    bd=3,
    text="5",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=btn5_clicked,
)
btn_5.pack(expand=TRUE, side=LEFT, fill=BOTH)

btn_6 = Button(
    btn_row_4,
    bg="red",
    bd=3,
    text="6",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=btn6_clicked,
)
btn_6.pack(expand=TRUE, side=LEFT, fill=BOTH)

btn_s = Button(
    btn_row_4,
    bg="red",
    bd=3,
    text="-",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=btn_minus_clicked,
)
btn_s.pack(expand=TRUE, side=LEFT, fill=BOTH)

btn_7 = Button(
    btn_row_5,
    bg="red",
    bd=3,
    text="7",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=btn7_clicked,
)
btn_7.pack(expand=TRUE, side=LEFT, fill=BOTH)

btn_8 = Button(
    btn_row_5,
    bg="red",
    bd=3,
    text="8",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=btn8_clicked,
)
btn_8.pack(expand=TRUE, side=LEFT, fill=BOTH)

btn_9 = Button(
    btn_row_5,
    bg="red",
    bd=3,
    text="9",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=btn9_clicked,
)
btn_9.pack(expand=TRUE, side=LEFT, fill=BOTH)

btn_m = Button(
    btn_row_5,
    bg="red",
    bd=3,
    text="*",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=btn_multiply_clicked,
)
btn_m.pack(expand=TRUE, side=LEFT, fill=BOTH)

btn_b1 = Button(
    btn_row_6,
    bg="red",
    bd=3,
    text="(",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=b1_clicked,
)
btn_b1.pack(expand=TRUE, side=LEFT, fill=BOTH)

btn_0 = Button(
    btn_row_6,
    bg="red",
    bd=3,
    text="0",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=btn0_clicked,
)
btn_0.pack(expand=TRUE, side=LEFT, fill=BOTH)

btn_b2 = Button(
    btn_row_6,
    bg="red",
    bd=3,
    text=")",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=b2_clicked,
)
btn_b2.pack(expand=TRUE, side=LEFT, fill=BOTH)

btn_d = Button(
    btn_row_6,
    bg="red",
    bd=3,
    text="/",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=btn_divide_clicked,
)
btn_d.pack(expand=TRUE, side=LEFT, fill=BOTH)

btn_cl = Button(
    btn_row_7,
    bg="red",
    bd=3,
    text="C",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=C_clicked,
)
btn_cl.pack(expand=TRUE, side=LEFT, fill=BOTH)

btn_do = Button(
    btn_row_7,
    bg="red",
    bd=3,
    text=".",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=dot_clicked,
)
btn_do.pack(expand=TRUE, side=LEFT, fill=BOTH)

btn_ba = Button(
    btn_row_7,
    bg="red",
    bd=3,
    text="⌫",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=back_clicked,
)
btn_ba.pack(expand=TRUE, side=LEFT, fill=BOTH)

btn_eq = Button(
    btn_row_7,
    bg="red",
    bd=3,
    text="=",
    relief=GROOVE,
    font="Arial 20 bold ",
    command=eq_clicked,
)
btn_eq.pack(expand=TRUE, side=LEFT, fill=BOTH)

status = Label(
    root,
    bg="red",
    bd=3,
    text="History : ",
    relief=GROOVE,
    font="Arial 20 bold ",
    anchor=W,
)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
# 2JPtFQJI4LkA5bfTk3mh
