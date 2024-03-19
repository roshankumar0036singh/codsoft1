import customtkinter
from tkinter import *
from tkinter import messagebox
app=customtkinter.CTk()
app.title('TO DO LIST')
app.geometry('350x450')
app.config(bg='#20948B')
font1=('Arial',30,'bold')
font2=('Arial',18,'bold')
font3=('Arial',10,'bold')

def add():
    task=entry.get()
    if task:
        li_t.insert(0,task)
        entry.delete(0,END)
        save()
    else:
        messagebox.showerror('ERROR','Enter a task.')
def remove():
    selected=li_t.curselection()
    if selected:
        li_t.delete(selected[0])
        save()
    else:
        messagebox.showerror('ERROR','Choose a task to delete')
def save():
    with open("task.txt","w") as f:
        task=li_t.get(0,END)
        for task in task:
            f.write(task+"/n")
def load():
    try:
        with open("task.txt","r")as f:
            task=f.readlines()
            for task in task:
                li_t.insert(0,task.strip())
    except FileNotFoundError:
        pass
       

titlelabel=customtkinter.CTkLabel(app,font=font1,text='TO DO LIST',text_color='#fff',bg_color='#20948B')
titlelabel.place(x=100,y=20)

addbutton=customtkinter.CTkButton(app,command=add,font=font2,text_color='#fff',text='ADD',fg_color='#06911f',bg_color='#20948B',corner_radius=5,width=120)
addbutton.place(x=40,y=80)

removebutton=customtkinter.CTkButton(app,command=remove,font=font2,text_color='#fff',text='REMOVE',fg_color='#96061c',hover_color='#96061c',bg_color='#20948B',corner_radius=5,)
removebutton.place(x=180,y=80)

entry=customtkinter.CTkEntry(app,font=font2,text_color='#000',fg_color='#fff',border_color='#fff',width=280)
entry.place(x=40,y=120)
li_t=Listbox(app,width=39,height=15,font=font3)
li_t.place(x=40,y=180)


        
    


load()
app.mainloop()




