import tkinter as ttk
import customtkinter as ctk
import tkinter.messagebox as messagebox
import keyboard


def copy_text(event):
    text = event.widget['text']
    root.clipboard_clear()
    root.clipboard_append(text)
    messagebox.showinfo("Copied", f"Text '{text}' copied to clipboard!")

def add_task():
    task = todo_entry.get()
    task_label = ctk.CTkLabel(task_list_frame, wraplength= 480, text=task)
    task_label.pack(pady=8)
    task_label.bind("<Button-1>", copy_text)
    todo_entry.delete(0, ctk.END)

def on_focus_in(event):
    keyboard.add_hotkey("enter", add_task)

def on_focus_out(event):
    keyboard.remove_hotkey("enter")


# init
root = ctk.CTk()
root.geometry("750x450")
root.title("Clipboard App by Tommy")
root.resizable(False, False)

# widgets
title_label  = ctk.CTkLabel(root, text="Clipboard App", font=ctk.CTkFont(size=30, weight="bold", family="Segoe UI"))

task_list_frame = ctk.CTkScrollableFrame(root, width = 500, height = 200)

add_button = ctk.CTkButton(root, text="Add", width=500, command=add_task)

todo_entry = ctk.CTkEntry(root, placeholder_text="Add to List", width=520)

todo_entry.bind("<FocusIn>", on_focus_in)
todo_entry.bind("<FocusOut>", on_focus_out)


# packing
title_label.pack(pady=(40, 20))
todo_entry.pack(pady=(0, 20))
task_list_frame.pack()
add_button.pack(pady=20)



# run
root.mainloop()