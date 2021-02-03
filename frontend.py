from backend import login, get_unfollowers, driver, followers, following
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
driver = driver()


from tkinter import *
w = Tk()
w.geometry("1000x620")
bg = PhotoImage(file = "bg.png")
label1 = Label( w , image = bg)
label1.place(x = 0, y = 0)

#labels and entries
Label(w, text=' INSTAGRAM ID : ' ).place(x=300,y=60)
Label(w, text='PASSWORD :').place(x=300,y=100)
id = StringVar()
id.set("Login id")
pas = StringVar()
e1 = Entry(w, textvariable= id).place(x=400,y=60)
e2 = Entry(w, textvariable = pas , show = "*").place(x=400,y=100)



#listbox
listbox = Listbox(w,  width=100, font=("Helvetica", 12))
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
button1.place(x= 350 , y = 150)
button2 = Button(w, text='Un-followers', width=15 , activebackground = "magenta2" , bd= 3 , bg = "plum1", font = "Lato" , command = unfol )
button2.place(x= 90 , y= 200 )
button3 = Button(w, text='Followers', width=15, activebackground = "magenta2" , bd= 3 , bg = "plum1" , font = "Lato" , command = foll)
button3.place(x= 240 , y= 200 )
button4 = Button(w, text='Following', width=15 , activebackground = "magenta2" , bd= 3 , bg = "plum1" , font = "Lato" , command = foling )
button4.place(x= 390 , y= 200 )






w.mainloop()
driver.close()

