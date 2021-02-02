from backend import login, get_unfollowers, driver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from tkinter import *
w = Tk()
w.geometry("1000x620")
bg = PhotoImage(file = "bg.png")
label1 = Label( w, image = bg)
label1.place(x = 0, y = 0)

#labels and entries
Label(w, text=' INSTAGRAM ID : ' ).place(x=300,y=40)
Label(w, text='PASSWORD :').place(x=300,y=80)
id = StringVar()
pas = StringVar()
e2 = Entry(w, textvariable= id)
e1 = Entry(w, textvariable = pas)
e2.place(x=400,y=40)
e1.place(x=400,y=80)



#listbox
frm = Frame(w)
frm.grid(row=1, column=2, sticky=N+S)
frm.place(x=40,y=250)
w.rowconfigure(5, weight=1)
w.columnconfigure(5, weight=1)
scrollbar = Scrollbar(frm, orient="vertical")
scrollbar.pack(side=RIGHT, fill=Y)
listNodes = Listbox(frm,  width=100, yscrollcommand=scrollbar.set, font=("Helvetica", 12))
listNodes.pack(expand=True, fill=Y)
scrollbar.config(command=listNodes.yview)



username = id.get()
pw = pas.get()
driver = driver()
def unfol():
    get_unfollowers(driver, username)
    for i in range(len(get_unfollowers(driver, username))):
        listNodes.insert(END, get_unfollowers(driver, username)[i])






#buttons

button1 = Button(w, text='LOGIN', width=15, command=lambda:login(driver, username, pw))
button1.pack()
button1.place(x= 350 , y = 120)
button2 = Button(w, text='UNFOLLOWERS', width=15, command= unfol )
button2.pack()
button2.place(x= 100 , y= 180 )
button3 = Button(w, text='FOLLOWERS', width=15,)
button3.pack()
button3.place(x= 250 , y= 180 )
button4 = Button(w, text='FOLLOWING', width=15,)
button4.pack()
button4.place(x= 400 , y= 180 )




w.mainloop()
driver.close()

