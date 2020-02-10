from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Converter:
    def __init__(self, parent):

        # Formatting variables...
        background_color= "light blue"

        # Converter Main screen GUI...
        self.converter_frame =Frame(width=600, height=600, bg=background_color)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="temperature Converter",
                                font="Arial 16 bold",
                                    bg=background_color,
                                padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Help Button (row 1)
        self.help_button = Button(self.converter_frame, text="help", padx=10, pady=10)
        self.help_button.grid(row=1)


    def Help(self):
         print("You asked for help)")
         get_help = Help(self)
         get_help.help_text.configure(text="help text goes here")

class Help:
    def __init__(self,partner):

        background = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (i.e: help box)
        self.help_box = Toplevel()

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row)
        self.how_heading = Label(self.help_frame,text="help/Instruction",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)
        # Help text (label, row 1)

        # Dismiss button ( row 2)






# main routine:
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
