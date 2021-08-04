from tkinter import *
import backend

TIME_SLOTS = []

def submit():
    name = name_entry.get()
    backend.add_order(name, TIME_SLOTS)
    new_schedule = backend.generate_string(TIME_SLOTS)
    output_label.configure(text = new_schedule)


root = Tk()
root.geometry("300x300")
root.title("Giovanni's Cafe")
root.resizable(True, True)
root.configure(background = "Light Blue")

##Inputs
input_frame = Frame(root)
input_frame.grid(row=0, column = 0, padx = 10, pady = 10)
##Place name entry
name_entry = Entry(input_frame, width = 15, bg = 'white')
name_entry.grid(row = 0, column = 0, padx = 5, pady = 5)
##Place submit button
submit_button = Button(input_frame, text = "Submit Order", width = 15, command = submit)
submit_button.grid(row = 1, column = 0, padx = 5, pady = 5)

##Outputs
output_frame = Frame(root)
output_frame.grid(row = 0, column = 1, padx = 10, pady = 10)

output_label = Label(output_frame, text = '')
output_label.grid(row = 0, column = 0, padx = 5, pady = 5)


root.mainloop()