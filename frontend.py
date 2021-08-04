from tkinter import *
import backend

TIME_SLOTS = []

def submit():
    name = name_entry.get()
    backend.add_order(name, TIME_SLOTS)
    new_schedule = backend.generate_string(TIME_SLOTS)
    output_label.delete(1.0,END)
    output_label.insert(1.0,new_schedule)

root = Tk()
root.geometry("600x425")
root.title("Giovanni's Cafe")
root.resizable(False, False)
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

sb = Scrollbar(
    output_frame,
    orient=VERTICAL
)
sb.pack(side = RIGHT, fill = Y)

output_label = Text(output_frame, height = 25, width = 50,yscrollcommand = sb.set)
output_label.pack(side = LEFT)

sb.config(command=output_label.yview)

root.mainloop()