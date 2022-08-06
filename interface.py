from tkinter import *
from block_unblock import block, unblock

# setting up local ip address and path to host file

host_path =r'C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'


# Creating GUI

gui = Tk()
gui.geometry('600x400')
gui.resizable(0,0)
gui.title("Website Blocker by Tal")

text_box_label = Label(gui, text = "Enter the website address", font = 'helvetica')
text_box_label.place(x=300, y=60, anchor ='center')

text_box = Text(gui, font = 'helvetica', height = '2', width = '30')
text_box.place(x=300, y=110, anchor = 'center')


blocking_button = Button(gui, text = 'Block me!',font = 'arial',pady = 5,command = block ,width = 6, bg = 'royal blue1', activebackground = 'grey')
blocking_button.place(x = 230, y = 150)

unblock_button = Button(gui, text = 'Set me free!',font = 'arial',pady = 5,command = unblock ,width = 6, bg = 'royal blue1', activebackground = 'grey')
unblock_button.place(x = 350, y = 150)

gui.mainloop()