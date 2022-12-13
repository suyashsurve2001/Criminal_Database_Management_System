import pymongo
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
global url 
url = "mongodb://localhost:27017/"
db = pymongo.MongoClient(url)
db_name = "criminal_db"
crud_db = db[db_name]
collection_name="criminal"
employee = crud_db[collection_name] 

# url = "mongodb://localhost:27017/"
# db = pymongo.MongoClient(url)
# db_name = "cruddb"
# crud_db = db[db_name]
# collection_name="employee"
# employee = crud_db[collection_name] 

def create():
    name = cname.get()
    id = cid.get()
    phone = cphone.get()
    Gender = cGender.get()
    Age = cAge.get()  
    Crime = cCrime.get()
    Address = cAddress.get()
    if(name=="" or id=="" or phone=="" or Gender=="" or Crime=="" or Age=="" or Address==""):
        messagebox.showinfo("Create","All fiedls are required")
    else:
        read = employee.find_one({'id':id})
        if(read):
            messagebox.showinfo("Create","criminal with this id allready present")
            cname.delete(0,END)
            cid.delete(0,END)
            cphone.delete(0,END)
            cGender.delete(0,END)
            cAge.delete(0,END)
            cCrime.delete(0,END)
            cAddress.delete(0,END)
        else:
            data = {
                'name': name,
                'id':id,
                'phone':phone,
                'Gender': Gender,
                'Age': Age,
                'Crime': Crime,
                'Address': Address
            }
            employee.insert_one(data)
            messagebox.showinfo("Create","Data Inserted successfully")
            cname.delete(0,END)
            cid.delete(0,END)
            cphone.delete(0,END)
            cGender.delete(0,END)
            cAge.delete(0,END)
            cCrime.delete(0,END)
            cAddress.delete(0,END)
            
            
            
def reset():
    cname.delete(0,END)
    cid.delete(0,END)
    cphone.delete(0,END)
    cGender.delete(0,END)
    cAge.delete(0,END)
    cCrime.delete(0,END)
    cAddress.delete(0,END)
    
    
    
def update():
    name = cname.get()
    id = cid.get()
    phone = cphone.get()
    Gender = cGender.get()
    Age = cAge.get()
    Crime = cCrime.get()
    Address = cAddress.get(0,END)
    if(name=="" or id=="" or phone=="" or Gender=="" or Age=="" or Crime=="" or Address==""):
        messagebox.showinfo("Create   ","All fiels are required")
    else:
        read = employee.find_one({'id':id})
        if(read):
            current = employee.find_one({'id':id})
            new={'$set':{'name':name,'phone':phone,'Gender':Gender,'Age':Age,'Crime':Crime,'Address':Address}}
            employee.update_one(current,new)
            messagebox.showinfo("Create","criminal Data Updated successfully")
            cname.delete(0,END)
            cid.delete(0,END)
            cphone.delete(0,END)
            cGender.delete(0,END)
            cAge.delete(0,END)
            cCrime.delete(0,END)
            cAddress.delete(0,END)
        else:
            messagebox.showinfo("Update",f"NO criminal with {id} exists")
            cid.delete(0,END)
            
            
            
            
def read():
    data = employee.find({})
    list_of_list = []
    name = []
    id = []
    phone = []
    Gender = []
    Age = []
    Crime = []
    Address = []  
    for i in data:
        name.append(i['name'])
        id.append(i['id'])
        phone.append(i['phone'])
        Gender.append(i['Gender'])
        Age.append(i['Age'])
        Crime.append(i['Crime'])
        Address.append(i['Address'])
    list_of_list.append(name)
    list_of_list.append(id)
    list_of_list.append(phone)
    list_of_list.append(Gender)
    list_of_list.append(Age)
    list_of_list.append(Crime)
    list_of_list.append(Address)
    if(data):
        subwindow = Toplevel(root)
        subwindow.title("Criminal Data")
        subwindow.minsize(900,300)
        subwindow.geometry("900x300")
        rowtitle = ["name","id","phone","Gender","Age","Crime","Address"]
        for k in range(7):
            e = Entry(subwindow,width=20)
            e.grid(row=0,column=k)
            e.insert(END,rowtitle[k])
        for i in range(7):
            for j in range(len(list_of_list[0])):
                e = Entry(subwindow,width=20)
                e.grid(row=j+1,column=i)
                e.insert(END,list_of_list[i][j])
    else:
        messagebox.showinfo("Read","No criminal Data found")
        
        
        
def delete():
    id = cid.get()
    data = employee.find_one({'id':id})
    if(id=="" ):
        messagebox.showinfo("Delete","id field is compulsory ")
    else:
        if(data):
            data = employee.delete_one({'id':id})
            messagebox.showinfo("Create","criminal data  Deleted successfully")
            cid.delete(0,END)
        else:
            messagebox.showinfo("Read","No criminal Data found")
            
            
root = Tk()
# root.minsize(900,900)
root.geometry('900x900')
root.title("CRUD Application")
root.config(bg="#2c3e50")
root.state("zoomed")

entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Criminal DataBase", font=("Calibri", 18, "bold"), bg="#535c68", fg="white", justify='center')
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")





id = Label(entries_frame, text="Criminal ID.:-", font=("Calibri", 16), bg="#535c68", fg="white")
id.grid(row=1, column=0, padx=10, pady=10, sticky="w")
cid= Entry(entries_frame,  font=("Calibri", 16), width=21)
cid.grid(row=1, column=1, padx=0, pady=10, sticky="w")


name = Label(entries_frame, text="Name:-", font=("Calibri", 16), bg="#535c68", fg="white")
name.grid(row=2, column=0, padx=10, pady=10, sticky="w")
cname = Entry(entries_frame,  font=("Calibri", 16), width=21)
cname.grid(row=2, column=1, padx=0, pady=10, sticky="w")


phone = Label(entries_frame,text="Enter Contact No:- : ", font=("Calibri", 16), bg="#535c68", fg="white")
phone.grid(row=3, column=0, padx=10, pady=10, sticky="w")
cphone = Entry(entries_frame, font=("Calibri", 16), width=21)
cphone.grid(row=3, column=1, padx=0,pady=10, sticky="w")

Gender= Label(entries_frame, text="Gender:-", font=("Calibri", 16), bg="#535c68", fg="white")
Gender.grid(row=1, column=2, padx=0, pady=10, sticky="w")
cGender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=19, state="readonly")
cGender['values'] =("Male", "Female") 
cGender.grid(row=1, column=3, padx=0, pady=10, sticky="w")

Age = Label(entries_frame, text="Age:-", font=("Calibri", 16), bg="#535c68", fg="white")
Age.grid(row=2, column=2, padx=0, pady=10, sticky="w")
cAge= Entry(entries_frame, font=("Calibri", 16), width=21)
cAge.grid(row=2, column=3, padx=0, pady=10, sticky="w")

Crime = Label(entries_frame, text="Crime:-", font=("Calibri", 16), bg="#535c68", fg="white")
Crime.grid(row=3, column=2, padx=0, pady=10, sticky="w")
cCrime = ttk.Combobox(entries_frame, font=("Calibri", 16), width=19,  state="readonly")
cCrime['values'] = ("Corruption and Bribery", "Drugs Dealing","Stolen Things","Assault and Armed Robbery")
cCrime.grid(row=3, column=3, padx=0, sticky="w")

Address = Label(entries_frame, text="Address:-", font=("Calibri", 16), bg="#535c68", fg="white")
Address.grid(row=4, column=0, padx=10, pady=10, sticky="w")
cAddress = Entry(entries_frame,  font=("Calibri", 16), width=51)
cAddress.grid(row=4, column=0, columnspan=10, padx=110, sticky="w"  )

# Button

create = Button(root,text="Create", width=18, font=("Calibri", 16, "bold"), fg="white",bg="#16a085", bd=0,command=create)
create.place(x=120,y=430)

reset = Button(root,text="Reset", width=18, font=("Calibri", 16, "bold"), fg="white", bg="#2980b9",bd=0,command=reset)
reset.place(x=360,y=430)

update = Button(root,text="Update", width=18, font=("Calibri", 16, "bold"), fg="white", bg="#c0392b",bd=0,command=update)
update.place(x=600,y=430)

read = Button(root,text="Read", width=18, font=("Calibri", 16, "bold"), fg="white",bg="#f39c12",bd=0,command=read)
read.place(x=840,y=430)

delete = Button(root,text="Delete", width=18, font=("Calibri", 16, "bold"), fg="white",bg="#9db009",bd=0,command=delete)
delete.place(x=1080,y=430)


root.mainloop()