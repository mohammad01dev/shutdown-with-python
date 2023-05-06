import tkinter
import os

def shutdown():
    os.system("shutdown /s")


root = tkinter.Tk()

root.title("First_Program")

labels = tkinter.Label(root, text = "Hello How Are You? \n Welcome To Are First Program")
labels.pack()

buttons = tkinter.Button(root, text = "Shut Down", bg="red", font="sans-serif", fg="white", command=shutdown)
buttons.pack()

root.mainloop()