from tkinter import *
from tkinter import messagebox

def entertask():
    def add():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            listbox_task.insert(END, input_text)
            root1.destroy()

    root1 = Tk()
    root1.title("Add task")
    root1.configure(bg="black")  # Set background color

    entry_task = Text(root1, width=40, height=4, bg="lightgrey", fg="black", font=("Helvetica", 12))
    entry_task.pack(pady=10)

    button_temp = Button(root1, text="Add task", command=add, bg="lightblue", fg="black")
    button_temp.pack(pady=5)

    root1.mainloop()

def deletetask():
    selected = listbox_task.curselection()
    listbox_task.delete(selected[0])

def markcompleted():
    marked = listbox_task.curselection()
    temp = marked[0]
    temp_marked = listbox_task.get(marked)
    temp_marked += " ✔"
    listbox_task.delete(temp)
    listbox_task.insert(temp, temp_marked)

window = Tk()
window.title("To-Do App")
window.configure(bg="black")  # Set background color

frame_task = Frame(window, bg="black")  # Set background color
frame_task.pack(pady=20)

listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font=("Helvetica", 12))
listbox_task.pack(side=LEFT)

scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

entry_button = Button(window, text="Add Task", width=50, command=entertask, bg="lightblue", fg="black")
entry_button.pack(pady=5)

delete_button = Button(window, text="Delete Selected Task", width=50, command=deletetask, bg="lightblue", fg="black")
delete_button.pack(pady=5)

mark_button = Button(window, text="Mark as Completed", width=50, command=markcompleted, bg="lightblue", fg="black")
mark_button.pack(pady=5)

window.mainloop()
