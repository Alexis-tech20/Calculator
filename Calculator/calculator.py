from ast import Lambda
from tkinter import *

# Create window/Center window
window = Tk()
window.title("Calculator")

window.configure(bg='#1F1F1F')

# Center 
app_width = 399
app_height = 368

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y= (screen_height / 2) - (app_height / 2)

window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

# input entry( used to accept single line text from the user)
e = Entry(window, width = 50, borderwidth = 6, bg = "#1F1F1F", fg = "#F8F8FF", font = 'Helvetica 9 bold')
e.grid(row = 0, column = 0, columnspan = 6, padx = 10, pady = 10)


def button_click(number):

    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(float(first_number))
    e.delete(0, END)
 
 # functions for button widgets
def button_equal():

    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(float(first_number))
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(float(first_number))
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(float(first_number))
    e.delete(0, END)

def delete():
        a = e.get()
        e.delete(first=len(a)-1, last="end")


#Define Buttons 
# lambda allows you to pass a perameter into a function
btn1 = Button(window, text = '1', bg = "#68838B", fg = "#F8F8FF",  font = 'Helvetica 9 bold', padx = 40, pady = 20, command = lambda: button_click(1))
btn2 = Button(window, text = '2', bg = "#68838B", fg = "#F8F8FF", font = 'Helvetica 9 bold', padx = 43, pady = 20, command = lambda: button_click(2))
btn3 = Button(window, text = '3', bg = "#68838B", fg = "#F8F8FF", font = 'Helvetica 9 bold', padx = 46, pady = 20, command = lambda: button_click(3))
btn4 = Button(window, text = '4', bg = "#68838B", fg = "#F8F8FF", font = 'Helvetica 9 bold', padx = 40, pady = 20, command = lambda: button_click(4))
btn5 = Button(window, text = '5', bg = "#68838B", fg = "#F8F8FF", font = 'Helvetica 9 bold', padx = 43, pady = 20, command = lambda: button_click(5))
btn6 = Button(window, text = '6', bg = "#68838B", fg = "#F8F8FF", font = 'Helvetica 9 bold', padx = 46, pady = 20, command = lambda: button_click(6))
btn7 = Button(window, text = '7', bg = "#68838B", fg = "#F8F8FF", font = 'Helvetica 9 bold', padx = 40, pady = 20, command = lambda: button_click(7))
btn8 = Button(window, text = '8', bg = "#68838B", fg = "#F8F8FF", font = 'Helvetica 9 bold', padx = 43, pady = 20, command = lambda: button_click(8))
btn9 = Button(window, text = '9', bg = "#68838B", fg = "#F8F8FF", font = 'Helvetica 9 bold', padx = 46, pady = 20, command = lambda: button_click(9))
btn0 = Button(window, text = '0', bg = "#68838B", fg = "#F8F8FF", font = 'Helvetica 9 bold', padx = 91, pady = 20, command = lambda: button_click(0))
btn_decimal = Button(window, text = '.', bg = "#68838B", fg = "#F8F8FF", font = 'Helvetica 9 bold', padx = 48, pady = 20, command=lambda: button_click('.'))

btn_equal = Button(window, text = '=', bg = "#FF7F00", fg = "#F8F8FF", font = 'Helvetica 9 bold', padx = 39, pady = 20, command = button_equal)
btn_clear = Button(window, text = 'Clear', bg = "#D3D3D3", font = 'Helvetica 9 bold', padx = 79, pady = 20, command =  button_clear)

btn_subtract = Button(window, text = '-', bg = "#FF7F00", fg = "#F8F8FF", font = 'Helvetica 9 bold', padx = 41, pady = 20, command = button_subtract)
btn_multiply = Button(window, text = '*', bg = "#FF7F00", fg = "#F8F8FF", font = 'Helvetica 9 bold', padx = 40, pady = 20, command = button_multiply)
btn_divide = Button(window, text = '/', bg = "#FF7F00", fg = "#F8F8FF", font = 'Helvetica 9 bold', padx = 41, pady = 20, command = button_divide)
btn_add = Button(window, text = '+', bg = "#FF7F00", fg = "#F8F8FF", font = 'Helvetica 9 bold', padx = 39, pady = 20, command = button_add)
btn_delete = Button(window, text = 'del', bg = "#D3D3D3", font = 'Helvetica 9 bold', padx = 41, pady = 20, command = delete)


# Put the button widgets where you would like
btn1.grid(row = 4, column = 0)
btn2.grid(row = 4, column = 1)
btn3.grid(row = 4, column = 2)

btn4.grid(row = 3, column = 0)
btn5.grid(row = 3, column = 1)
btn6.grid(row = 3, column = 2)

btn7.grid(row = 2, column = 0)
btn8.grid(row = 2, column = 1)
btn9.grid(row = 2, column = 2)

btn_decimal.grid(row=5, column=2)

btn0.grid(row = 5, column = 0, columnspan = 2)
btn_clear.grid(row = 1, column = 0, columnspan = 2)
btn_equal.grid(row = 5, column = 3)

btn_add.grid(row = 4, column = 3)
btn_subtract.grid(row = 3, column = 3)
btn_multiply.grid(row = 2, column = 3)
btn_divide.grid(row = 1, column = 3)
btn_delete.grid(row = 1, column = 2)


window.mainloop()