from backend import login, get_unfollowers, driver, followers, following
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
driver = driver()


from tkinter import *
w = Tk()
w.geometry("800x620")
w.title("Insta:)Bot")
bg = PhotoImage(file = "bg.png")
label1 = Label( w  , image = bg)
label1.place(x = 0, y = 0)

def about():
    w2 = Toplevel()
    w2.geometry("400x400")
    w2.title("About... ")
    bg = PhotoImage(file="bg.png")
    label1 = Label(w2 , image=bg)
    label1.place(x=0, y=0)
    listbox = Listbox(w2 , height = 20 , width=35, font=("Helvetica", 12))
    listbox.place(x=20, y=20)
    w2.mainloop()

def win2():
    w2 = Toplevel()
    w2.geometry("400x400")
    w2.title("Direct Message ")
    bg = PhotoImage(file="bg.png")
    label1 = Label(w2 , image=bg)
    label1.place(x=0, y=0)
    Text(w2 , height = 15 , width = 32).place(x=50 , y = 100)
    Checkbutton(w2 , text= "followers").place(x=55 , y = 40)
    Checkbutton(w2, text="following").place(x=180, y=40)
    w2.mainloop()


#labels and entries
lab1 = Label(w, text='Instagram bot' , font=("Helvetica", 32) , bg = "#b1eff2").place(x=250,y=20)
Label(w, text=' INSTAGRAM ID : ' ,font=("Helvetica", 12) , bg = "#b1eff2").place(x=230,y=100)
Label(w, text='PASSWORD :' ,font=("Helvetica", 12) ,  bg ="#b1eff2" ).place(x=250,y=140)
id = StringVar()
id.set("Login id")
pas = StringVar()
e1 = Entry(w, textvariable= id , font=("Helvetica", 12) ).place(x=370,y=100)
e2 = Entry(w, textvariable = pas , font=("Helvetica", 12) , show = "*").place(x=370,y=140)

#menu
menu = Menu(w)
w.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=w.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About' , command = about )



#listbox
listbox = Listbox(w,  width=75, font=("Helvetica", 12))
listbox.place(x= 60 , y = 300 )


def log():
    username=id.get()
    pw= pas.get()
    if login(driver, username, pw):
        listbox.insert(END , "Login successfull....!" , "\n")
    else :
        listbox.insert(END, "Login unsuccessfull....!")
def unfol():
    username = id.get()
    listbox.delete(0,END)
    unfollowers = get_unfollowers(driver, username)
    for i in range(len(unfollowers)):
        n = i+1
        listbox.insert(END , (n ,":" ,unfollowers[i]) , "\n")

def foll():
    username = id.get()
    listbox.delete(0, END)
    follower = followers(driver, username)
    for i in range(len(follower)):
        n = i+1
        listbox.insert(END , (n ,":" ,follower[i] ), "\n")
def foling():
    username = id.get()
    listbox.delete(0, END)
    followin = following(driver, username)
    for i in range(len(followin)):
        n = i+1
        listbox.insert(END , (n ,":" ,followin[i] ) , "\n")







#buttons

button1 = Button(w, text='Log In', width=15 ,activebackground = "magenta2" , bd= 3 , bg = "LightSkyBlue1" , font = "Lato" , command = log)
button1.place(x= 310 , y = 180)
button2 = Button(w, text='Un-followers', width=15 , activebackground = "magenta2" , bd= 3 , bg = "plum1", font = "Lato" , command = unfol )
button2.place(x= 90 , y= 250 )
button3 = Button(w, text='Followers', width=15, activebackground = "magenta2" , bd= 3 , bg = "plum1" , font = "Lato" , command = foll)
button3.place(x= 240 , y= 250 )
button4 = Button(w, text='Following', width=15 , activebackground = "magenta2" , bd= 3 , bg = "plum1" , font = "Lato" , command = foling )
button4.place(x= 390 , y= 250 )
button4 = Button(w, text='new', width=15 , activebackground = "magenta2" , bd= 3 , bg = "plum1" , font = "Lato" , command = win2)
button4.place(x= 540 , y= 250 )






w.mainloop()
driver.close()

