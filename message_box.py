import tkinter as tk
from tkinter import Label, ttk
from tkinter import messagebox as m_box
win=tk.Tk()
#label frame
Label_frame=ttk.LabelFrame(win, text='contact Detail')
Label_frame.grid(row=0,column=0,padx=40,pady=10)

#labels
name_label=ttk.Label(Label_frame,text='Enter your name please:',font=('Helvtica',14))
age_label=ttk.Label(Label_frame,text='Enter your age please:',font=('Helvtica',14))

#entry box variables
name_var=tk.StringVar()
age_var=tk.StringVar()

#entrt boxes
name_entry=tk.Entry(Label_frame,width=36,textvariable=name_var)
age_entry=ttk.Entry(Label_frame,width=36,textvariable=age_var)

#grid
name_label.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
age_label.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)
name_entry.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
age_entry.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)

def submit():
    # m_box.showinfo('title','content of this message box !!')
    name=name_var.get()
    age=age_var.get()
    if name=='' or age=='':
        m_box.showerror('Error','Please fill both  name and age')
    else:
        try:
            age=int(age)
        except ValueError:
            m_box.showerror('Only  digits are allowed in age ')
        else:
            if age<18:
                m_box.showwarning('warning','you are not 18, visit this content on your own risk')  
            print(f'{name}:{age}')



submit_btn=ttk.Button(win,text='Submit',command=submit)
submit_btn.grid(row=1,columnspan=2,padx=40)
win.mainloop()

