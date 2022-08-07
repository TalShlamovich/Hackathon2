from tkinter import *

# setting up local ip address and path to host file
host_path =r'C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'



def block() -> None:
    
    website_list = text_box.get(1.0,END)
    website = list(website_list.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for address in website:
            if address in file_content:
                display=Label(gui, text = 'You already blocked this website' , font = 'helvetica')
                display.place(x=200,y=200)
                pass
            else:
                host_file.write(ip_address + " " + address + '\n')
                Label(gui, text = "Blocked", font = 'arial').place(x=230,y =200)



def unblock() -> None:
    
    website_list = text_box.get(1.0,END)
    website = list(website_list.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.readlines()
    for web in website:
            if web in website_list:
                with open (host_path , 'r+') as f:
                    for line in file_content:
                        if line.strip(',') != website_list:
                            f.write(line)
                            Label(gui, text = "Unblocked", font = 'arial').place(x=350,y =200)
                            pass
                        else:
                            display=Label(gui, text = 'This website is not currently blocked' , font = 'arial')
                            display.place(x=350,y=200)

# Creating GUI

gui = Tk()
gui.geometry('600x400')
gui.resizable(0,0)
gui.title("Website Blocker by Tal")

text_box_label = Label(gui, text = "Enter the website address", font = 'helvetica')
text_box_label.place(x=300, y=60, anchor ='center')

text_box = Text(gui, font = 'helvetica', height = '2', width = '30')
text_box.place(x=300, y=110, anchor = 'center')


blocking_button = Button(gui, text = 'Block me!',font = 'arial',pady = 5,command = block ,width = 10, bg = 'red', activebackground = 'grey')
blocking_button.place(x = 250, y = 200, anchor='center')

unblock_button = Button(gui, text = 'Set me free!',font = 'arial',pady = 5,command = unblock ,width = 10, bg = 'green', activebackground = 'grey')
unblock_button.place(x = 370, y = 200, anchor='center')

gui.mainloop()