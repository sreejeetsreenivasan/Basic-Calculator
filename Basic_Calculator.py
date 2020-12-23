"""
The following program is an effective calculator built in Tkinter. It is basic in structure and does not have
higher level functionality that may be present in other calculator systems. Basic arithmetic along with other
relevant operations can be performed with this calculator.

"""
from tkinter import *
import random
import math

root = Tk()
root.title("Calculator")

entry = Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, padx=10, pady=10)

# Define two global variables
# Allows for the program to check to see which operation is being performed
# Keeps track of the first and second inputs when needed

global f_num
global math_to_do

# Define the various functions


def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_erase():
    entry.delete(0, END)


def button_addition():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "addition"
    f_num = float(first_number)
    entry.delete(0, END)


def button_subtraction():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "subtraction"
    f_num = float(first_number)
    entry.delete(0, END)


def button_multiplication():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "multiplication"
    f_num = float(first_number)
    entry.delete(0, END)


def button_division():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "division"
    f_num = float(first_number)
    entry.delete(0, END)


def button_decimals():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + ".")


def button_squares():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "squares"
    f_num = float(first_number)
    entry.delete(0, END)


def button_cubes():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "cubes"
    f_num = float(first_number)
    entry.delete(0, END)


def button_exponents():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "exponents"
    f_num = float(first_number)
    entry.delete(0, END)
    # needs additional code for actual computation in button_equals


def button_inversing():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "inverse"
    f_num = float(first_number)
    entry.delete(0, END)


def button_squareroot():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "square root"
    f_num = float(first_number)
    entry.delete(0, END)


def button_cuberoot():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "cube root"
    f_num = float(first_number)
    entry.delete(0, END)


def button_nthroot():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "nth root"
    f_num = float(first_number)
    entry.delete(0, END)


def button_naturallog():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "ln"
    f_num = float(first_number)
    entry.delete(0, END)


# This function is logarithm base 10 only, not an nth base logarithm


def button_logarithm():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "log"
    f_num = float(first_number)
    entry.delete(0, END)


def button_factorials():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "factorial"
    f_num = float(first_number)
    entry.delete(0, END)


# All trigonometric functions present only take in a value in radians as input
# Uses built-in math module for calculation


def button_sin():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "sine"
    f_num = float(first_number)
    entry.delete(0, END)


def button_cos():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "cosine"
    f_num = float(first_number)
    entry.delete(0, END)


def button_tan():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "tangent"
    f_num = float(first_number)
    entry.delete(0, END)


def button_arcsin():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "arc sine"
    f_num = float(first_number)
    entry.delete(0, END)


def button_arccos():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "arc cosine"
    f_num = float(first_number)
    entry.delete(0, END)


def button_arctan():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "arc tangent"
    f_num = float(first_number)
    entry.delete(0, END)


def button_percentage():
    first_number = entry.get()
    global f_num
    global math_to_do
    math_to_do = "percentage"
    f_num = float(first_number)
    entry.delete(0, END)


def button_rand():
    global math_to_do
    math_to_do = "random"


# Define the main function which allows for the calculator's functionality

def button_equals():
    second_number = entry.get()
    entry.delete(0, END)

    if math_to_do == "addition":
        entry.insert(0, f_num + float(second_number))

    elif math_to_do == "subtraction":
        entry.insert(0, f_num - float(second_number))

    elif math_to_do == "multiplication":
        entry.insert(0, f_num * float(second_number))

    elif math_to_do == "division":
        entry.insert(0, f_num / float(second_number))

    elif math_to_do == "squares":
        entry.insert(0, (f_num * f_num))

    elif math_to_do == "cubes":
        entry.insert(0, (f_num * f_num * f_num))

    elif math_to_do == "exponents":
        entry.insert(0, math.exp(f_num))

    elif math_to_do == "inverse":
        entry.insert(0, 1/f_num)

    elif math_to_do == "square root":
        entry.insert(0, math.sqrt(f_num))

    elif math_to_do == "cube root":
        entry.insert(0, (f_num ** (1/3)))

    elif math_to_do == "nth root":
        entry.insert(0, (float(second_number) ** (1/f_num)))

    elif math_to_do == "ln":
        entry.insert(0, math.log(f_num))

    elif math_to_do == "log":
        entry.insert(0, math.log10(f_num))

    elif math_to_do == "factorial":
        entry.insert(0, math.factorial(f_num))

    elif math_to_do == "sine":
        entry.insert(0, math.sin(f_num))

    elif math_to_do == "cosine":
        entry.insert(0, math.cos(f_num))

    elif math_to_do == "tangent":
        entry.insert(0, math.tan(f_num))

    elif math_to_do == "arc sine":
        entry.insert(0, math.asin(f_num))

    elif math_to_do == "arc cosine":
        entry.insert(0, math.acos(f_num))

    elif math_to_do == "arc tangent":
        entry.insert(0, math.atan(f_num))

    elif math_to_do == "percentage":
        entry.insert(0, f_num/100)

    elif math_to_do == "random":
        entry.insert(0, random.random())


# Define the buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=87, pady=20, command=lambda: button_click(0))
button_e = Button(root, text="e", padx=56, pady=20, command=lambda: button_click(math.e))
button_pi = Button(root, text="π", padx=56, pady=20, command=lambda: button_click(math.pi))
button_add = Button(root, text="+", padx=40, pady=20, command=lambda: button_addition())
button_equal = Button(root, text="=", padx=40, pady=20, command=lambda: button_equals())
button_clear = Button(root, text="Clear", padx=123, pady=20, command=lambda: button_erase())
button_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: button_subtraction())
button_multiply = Button(root, text="x", padx=40, pady=20, command=lambda: button_multiplication())
button_divide = Button(root, text="/", padx=41, pady=20, command=lambda: button_division())
button_decimal = Button(root, text=".", padx=42, pady=20, command=lambda: button_decimals())
button_square = Button(root, text="x^2", padx=44, pady=20, command=lambda: button_squares())
button_cube = Button(root, text="x^3", padx=40, pady=20, command=lambda: button_cubes())
button_exponent = Button(root, text="e^x", padx=48, pady=20, command=lambda: button_exponents())
button_inverse = Button(root, text="1/x", padx=50, pady=20, command=lambda: button_inversing())
button_square_root = Button(root, text="√x", padx=45, pady=20, command=lambda: button_squareroot())
button_cube_root = Button(root, text="∛x", padx=42, pady=20, command=lambda: button_cuberoot())
button_nth_root = Button(root, text="n√x", padx=46, pady=20, command=lambda: button_nthroot())
button_natural_log = Button(root, text="ln", padx=54, pady=20, command=lambda: button_naturallog())
button_log = Button(root, text="log", padx=51, pady=20, command=lambda: button_logarithm())
button_factorial = Button(root, text="x!", padx=54, pady=20, command=lambda: button_factorials())
button_sine = Button(root, text="sin", padx=44, pady=20, command=lambda: button_sin())
button_cosine = Button(root, text="cos", padx=40, pady=20, command=lambda: button_cos())
button_tangent = Button(root, text="tan", padx=48, pady=20, command=lambda: button_tan())
button_arcsine = Button(root, text="arcsin", padx=40, pady=20, command=lambda: button_arcsin())
button_arccosine = Button(root, text="arccos", padx=40, pady=20, command=lambda: button_arccos())
button_arctangent = Button(root, text="arctan", padx=40, pady=20, command=lambda: button_arctan())
button_percent = Button(root, text="%", padx=45, pady=20, command=lambda: button_percentage())
button_random = Button(root, text="Rand", padx=39, pady=20, command=lambda: button_rand())

# Place the buttons on the screen

button_1.grid(row=4, column=7)
button_2.grid(row=4, column=8)
button_3.grid(row=4, column=9)
button_4.grid(row=3, column=7)
button_5.grid(row=3, column=8)
button_6.grid(row=3, column=9)
button_7.grid(row=2, column=7)
button_8.grid(row=2, column=8)
button_9.grid(row=2, column=9)
button_0.grid(row=5, column=7, columnspan=2)

button_add.grid(row=4, column=10)
button_subtract.grid(row=3, column=10)
button_multiply.grid(row=2, column=10)
button_divide.grid(row=1, column=10)
button_decimal.grid(row=5, column=9)
button_equal.grid(row=5, column=10)
button_clear.grid(row=1, column=7, columnspan=3)

button_square.grid(row=2, column=2)
button_cube.grid(row=2, column=3)
button_exponent.grid(row=2, column=4)

button_inverse.grid(row=4, column=5)
button_square_root.grid(row=3, column=2)
button_cube_root.grid(row=3, column=3)
button_nth_root.grid(row=3, column=4)
button_natural_log.grid(row=3, column=5)
button_log.grid(row=3, column=6)

button_factorial.grid(row=4, column=6)
button_sine.grid(row=4, column=2)
button_cosine.grid(row=4, column=3)
button_tangent.grid(row=4, column=4)
button_e.grid(row=2, column=5)

button_random.grid(row=5, column=2)
button_percent.grid(row=5, column=3)
button_arcsine.grid(row=5, column=4)
button_arccosine.grid(row=5, column=5)
button_arctangent.grid(row=5, column=6)
button_pi.grid(row=2, column=6)

root.mainloop()
