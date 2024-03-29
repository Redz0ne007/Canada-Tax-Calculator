from tkinter import *
def centerwindow(window,width,height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

def update_selected_option(var, selected_province):
    def inner(*args):
        selected_province.set(var.get())
    return inner