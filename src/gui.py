import tkinter as tk


root = tk.Tk()
root.title('League Account Manager')
root.geometry('500x500')

button = tk.Button(text='Add Account', command=lambda: print('Pressed'))
button.pack()

listbox = tk.Listbox(root)
listbox.pack()
root.mainloop()
