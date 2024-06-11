import tkinter as tk

root = tk.Tk()
root.title("Add task")

def add_todo():
    todo = entry.get()
    if todo:
        listbox.insert(tk.END, todo)
        entry.delete(0, tk.END)

def delete_todo():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        pass

entry = tk.Entry(root)
entry.pack()

add_button = tk.Button(root, text="add", command=add_todo)
add_button.pack()

listbox = tk.Listbox(root)
listbox.pack()

delete_button = tk.Button(root, text="delete", command=delete_todo)
delete_button.pack()

root.mainloop()