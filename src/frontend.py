from tkinter import *
from backend import add_order, generate_strings

TIME_SLOTS = []

def submit():
    name = name_entry.get()
    add_order(name, TIME_SLOTS)
    new_schedule = generate_strings(TIME_SLOTS)
    schedule_cols = list(zip(*new_schedule))

    seq_label.delete(1.0,END)
    time_label.delete(1.0,END)
    task_label.delete(1.0,END)
    name_label.delete(1.0,END)
    seq_label.insert(1.0, '\n'.join(list(schedule_cols[0])))
    time_label.insert(1.0, '\n'.join(list(schedule_cols[1])))
    task_label.insert(1.0, '\n'.join(list(schedule_cols[2])))
    name_label.insert(1.0, '\n'.join(list(schedule_cols[3])))
    

root = Tk()
root.geometry("800x425")
root.title("Giovanni's Cafe")
root.resizable(False, False)
root.configure(background = "Light Blue")

##Inputs
input_frame = Frame(root)
input_frame.pack(side = LEFT)
##Place name entry
name_entry = Entry(input_frame, width = 15, bg = 'white')
name_entry.grid(row = 0, column = 0, padx = 5, pady = 5)
##Place submit button
submit_button = Button(input_frame, text = "Submit Order", width = 15, command = submit)
submit_button.grid(row = 1, column = 0, padx = 5, pady = 5)



sb = Scrollbar(
    root,
    orient=VERTICAL
)
sb.pack(side = RIGHT, fill = Y)

output_canvas = Canvas(root, yscrollcommand = sb.set)
output_canvas.pack(side = RIGHT)

##Outputs
output_frame = Frame(output_canvas)
output_frame.grid(row = 0, column = 1, padx = 10, pady = 10)

seq_label = Text(output_frame, height = 25, width = 10)
seq_label.pack(side = LEFT)
time_label = Text(output_frame, height = 25, width = 20)
time_label.pack(side = LEFT)
task_label = Text(output_frame, height = 25, width = 20)
task_label.pack(side = LEFT)
name_label = Text(output_frame, height = 25, width = 20)
name_label.pack(side = LEFT)

sb.config(command=output_canvas.yview)

root.mainloop()