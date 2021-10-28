from tkinter import *
from tkinter import ttk 
root = Tk()
root.title('P169')
root.geometry('500x500')

elements = ['Label','Button','Dropdown']
dropdown = ttk.Combobox(root,state='readonly',values=elements)
dropdown.pack()

class CreateElements:
    def __init__(self):
        print('This is CreateElements class')
        
        def createLabel(self):
            label = Label(root,text='A new label has been created using class',fg='blue')
            label.pack()
            
        def createButton(self):
            btn = Button(root,text='Button',command=self.message)
            btn.pack()
            
        def createDropdown(self):
            valueList = ['1','2','3']
            dropdown2 = ttk.Combobox(root,state='readonly',values=valueList)
            dropdown2.pack()
            
        def choose(self):
            comboBox_value = dropdown.get()
            if elements == "Label":
                self.createButton()
            if elements == "Button":
                self.createLabel()
            if elements == "Dropdown":
                self.createDropdown()
                
        def message(self):
            messagebox.showinfo('Warning','You clicked the button created using class')
            
object1 = CreateElements()
btn2 = Button(root,text='Create Element',command=object1.choose)
btn2.pack()

root.mainloop()