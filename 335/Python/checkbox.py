from tkinter import *
master = Tk()

def var_states():
    if var1.get() and var2.get():
        print("You can only pick one!")
    elif var1.get():
        print("DUDELY")
    elif var2.get():
        print("Girl power!")
    else:
        print("Who are you, anyway?")
#   print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))

Label(master, text="Are you a boy?  Or are you a girl?").grid(row=0, sticky=W)
isMale = IntVar()
Checkbutton(master, text="BOY", variable=isMale).grid(row=1, sticky=W)
isFemale = IntVar()
Checkbutton(master, text="GIRL", variable=isFemale).grid(row=2, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
mainloop()
