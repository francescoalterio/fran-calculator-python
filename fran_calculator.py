import tkinter as ttk
from tkinter import font

root = ttk.Tk()
root.geometry("320x500")
root.title("Fran Calculator")
root.resizable(0,0)

resultFrame = ttk.Frame(root, height=150)
resultFrame.pack(fill=ttk.X)

operation = ttk.Entry(resultFrame, justify=ttk.RIGHT, font=font.Font(size=20))
operation.place(rely=0.35, relx=0.1, width=250, height=40)

buttonsFrame = ttk.Frame(root)
buttonsFrame.pack(fill=ttk.BOTH, expand=True)

isLastOp = False

def addNumberOrOperator(btnPress, isOp):
    if len(operation.get()) > 0:
        lastCharacter = operation.get()[-1]
        if lastCharacter == '+' or lastCharacter == '-' or lastCharacter == '*' or lastCharacter == '/' or lastCharacter == '.':
            print('eee')
            if not isOp:
                operation.insert(len(operation.get()), btnPress)
        else:
            operation.insert(len(operation.get()), btnPress)
    else:
        if not isOp:
            operation.insert(len(operation.get()), btnPress)

        

def pressEqual():
    equation = operation.get()
    result = eval(equation)
    operation.delete(0, len(operation.get()))
    operation.insert(0, result)

def pressAC():
    operation.delete(0, len(operation.get()))

def pressDEL():
    operation.delete(len(operation.get()) - 1, len(operation.get()))
#buttons
ttk.Button(buttonsFrame, text="AC", width=10, height=4, command=pressAC).grid(column=0, row=0, sticky="we", columnspan=2)
ttk.Button(buttonsFrame, text="DEL", width=10, height=4, command=pressDEL).grid(column=2, row=0, sticky="we")
ttk.Button(buttonsFrame, text="/", width=10, height=4, command=lambda: addNumberOrOperator("/", True)).grid(column=3, row=0, sticky="we")

ttk.Button(buttonsFrame, text="7", width=10, height=4, command=lambda: addNumberOrOperator("7", False)).grid(column=0, row=1, sticky="we")
ttk.Button(buttonsFrame, text="8", width=10, height=4, command=lambda: addNumberOrOperator("8", False)).grid(column=1, row=1, sticky="we")
ttk.Button(buttonsFrame, text="9", width=10, height=4, command=lambda: addNumberOrOperator("9", False)).grid(column=2, row=1, sticky="we")
ttk.Button(buttonsFrame, text="*", width=10, height=4, command=lambda: addNumberOrOperator("*", True)).grid(column=3, row=1, sticky="we")

ttk.Button(buttonsFrame, text="4", width=10, height=4, command=lambda: addNumberOrOperator("4", False)).grid(column=0, row=2, sticky="we")
ttk.Button(buttonsFrame, text="5", width=10, height=4, command=lambda: addNumberOrOperator("5", False)).grid(column=1, row=2, sticky="we")
ttk.Button(buttonsFrame, text="6", width=10, height=4, command=lambda: addNumberOrOperator("6", False)).grid(column=2, row=2, sticky="we")
ttk.Button(buttonsFrame, text="-", width=10, height=4, command=lambda: addNumberOrOperator("-", True)).grid(column=3, row=2, sticky="we")

ttk.Button(buttonsFrame, text="1", width=10, height=4, command=lambda: addNumberOrOperator("1", False)).grid(column=0, row=3, sticky="we")
ttk.Button(buttonsFrame, text="2", width=10, height=4, command=lambda: addNumberOrOperator("2", False)).grid(column=1, row=3, sticky="we")
ttk.Button(buttonsFrame, text="3", width=10, height=4, command=lambda: addNumberOrOperator("3", False)).grid(column=2, row=3, sticky="we")
ttk.Button(buttonsFrame, text="+", width=10, height=4, command=lambda: addNumberOrOperator("+", True)).grid(column=3, row=3, sticky="we")

ttk.Button(buttonsFrame, text="0", width=10, height=4, command=lambda: addNumberOrOperator("0", False)).grid(column=0, row=4, sticky="we", columnspan=2)
ttk.Button(buttonsFrame, text=".", width=10, height=4, command=lambda: addNumberOrOperator(".", True)).grid(column=2, row=4, sticky="we")
ttk.Button(buttonsFrame, text="=", width=10, height=4, command=pressEqual).grid(column=3, row=4, sticky="we")


root.mainloop()