from tkinter import *

# setting up local ip address and path to host file
host_path ='C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

# Hello Tal this is a feedback about your hackathon project. I really liked your app it is a good resource to share
# It was working great and is a useful tool for others to download.
# The only comment about it is that is not using OOP.
# Congratulations on your project and hope to see more of those from you



def block() -> None:
    """Converts user input from the text box into an array (for cases when user inputs a few websites simultaneously)
    Then opens hosts file, checks whether the website is already there 
    If not then writes it into the file
    When commad is executed creates a message for a user"""
    input_website = text_box.get(1.0,END)
    website = list(input_website.split(", "))

    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()

        for address in website:
            if address in file_content:
                message=Label(gui, text = 'You already blocked this website' , font = 'Helvetica')
                message.place(x=310, y= 390, anchor='center')
                message.after(1500, message.destroy)
                pass

            else:
                host_file.write(ip_address + " " + address + '\n')
                message = Label(gui, text = "Blocked", font = 'Helvetica')
                message.place(x=310, y= 390, anchor='center')
                message.after(1500, message.destroy)


        
         
            
def unblock() -> None:
    """Take the user input and convert it to a list.
    Then opens hosts file, checks whether the website is already there
    Then rewrite the file line by line excluding the line that has user input
    When commad is executed creates a message for a user"""

    input_website = text_box.get(1.0,END)
    website = list(input_website.split(", "))
    website[-1]= website[-1][0:-1]


    with open (host_path , 'r') as host_file: 
        file_content = host_file.readlines()    
    for address in website:
        print (address)
        if (ip_address + " " + address + '\n') in file_content:
            with open (host_path , 'w') as f:
                for line in file_content:
                    print(line)
                    if address not in line.strip(','):
                        f.write(line)
                        message = Label(gui, text = "Unblocked", font = 'Helvetica')
                        message.place(x=310, y=390, anchor='center')
                        message.after(1500, message.destroy)
                        
                        
        else:
            message = Label(gui, text = 'This website is not currently blocked' , font = 'Helvetica')
            message.place(x=310, y= 390, anchor='center')
            message.after(1500, message.destroy)



# Creating GUI

gui = Tk()
gui.geometry('600x400')
gui.resizable(0,0)
gui.title("Website Blocker by Tal")

text_box_label = Label(gui, text = "Enter the website address", font = 'Helvetica')
text_box_label.place(x=300, y=60, anchor ='center')

text_box = Text(gui, font = 'Helvetica', height = '1', width = '30')
text_box.place(x=300, y=110, anchor = 'center')


blocking_button = Button(gui, text = 'Block me!',font = 'Helvetica',pady = 5,command = block ,width = 10, bg = 'red', activebackground = 'grey')
blocking_button.place(x = 250, y = 200, anchor='center')

unblock_button = Button(gui, text = 'Set me free!',font = 'Helvetica',pady = 5,command = unblock ,width = 10, bg = 'green', activebackground = 'grey')
unblock_button.place(x = 370, y = 200, anchor='center')


gui.mainloop()




