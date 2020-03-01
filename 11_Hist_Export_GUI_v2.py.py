from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Converter:
    def __init__(self, parent,):

        # Formatting variables...
        background_color = "light blue"

        # In actual program this is blank and is populated with user calculations
        self.all_calc_list = ['5 degrees C is -17.8 degrees F',
                              '6 degrees C is -16.7 degrees F',
                              '7 degrees C is -16.1 degrees F',
                              '8 degrees C is -15.8 degrees F',
                              '9 degrees C is -15.1 degrees F',
                                ]

        # self.all_calc_list = []

        # Converter Main screen GUI...
        self.converter_frame = Frame(width=600, height=600, bg=background_color)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="temperature Converter",
                                          font="Arial 16 bold",
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # History Button (row 1)
        self.history_button = Button(self.converter_frame, text="History",
                                     font=("Arial", "14"),
                                     padx=10, pady=10,
                                     command=lambda: self.get_history(self.all_calc_list))
        self.history_button.grid(row=1, pady=10)

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)

    def get_history(self, calc_history):
        History(self, calc_history)


class History:
    def __init__(self,partner, calc_history):

        background = "#a9ef99"     # Pale green

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (i.e: history box)
        self.history_box = Toplevel()

        # if users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame,text="Calculation History",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent "
                                  "calculations. Please use the "
                                  "export button to create a text "
                                  "file of all your calculations for "
                                  "this session", wrap=250,
                                  font="arial 10 italic",
                               justify=LEFT, width=40, bg=background, fg="maroon",
                                  padx=10, pady=10)
        self.history_text.grid(row=1)

        # History Output goes here.. (row 2)

        # Generate string from list of calculations...
        history_string = ""

        if len(calc_history) >= 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history)
                                               - item - 1]+"\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                               calc_history.index(item) -1] + "\n"
                self.history_text.config(text="Here is your calculation "
                                              "history. You can use the "
                                              "export button to save this "
                                              "data to a text file if "
                                              "desired.")

        # Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background, font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # Export / Dismiss Buttons frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold",
                                    command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        # Dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold",
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, calc_history):
        Export(self, calc_history)


class Export:
    def __init__(self, partner, calc_history):
        background = "#a9ef99"  # Pale green

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (i.e: export box)
        self.export_box = Toplevel()

        # if users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, bg=background)
        self.export_frame.grid()

        # Set up export heading (row)
        self.how_heading = Label(self.export_frame, text="export/Instruction",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Export Instruction (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename "
                                                         "in the box below "
                                                         "and press the Save "
                                                         "button to save your "
                                                         "calculation history "
                                                         "to a text file ",
                                 justify=LEFT, width=40,
                                 bg=background, wrap=250)
        self.export_text.grid(row=1)

        # warning text(label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename "
                                                         "you enter below "
                                                         "already exists, "
                                                         " its contents will "
                                                         "be replaced with "
                                                         "your calculation "
                                                         "history",
                                 justify=LEFT, bg="#ffafaf", fg="maroon",
                                 font="Arial 10 italic", wrap=225, padx=10,
                                 pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Save / cancel Frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and cancel Buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save")
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def close_export(self, partner):
        # Put export back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine:
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()