from tkinter import *


def block():
    import interface as inf
    website_lists = inf.text_box.get(1.0,END)
    to_be_blocked = list(website_lists.split(","))
    with open (inf.host_path , 'r+') as host_file:
        file_content = host_file.read()
        for address in to_be_blocked:
            if address in file_content:
                display=Label(inf.gui, text = 'You already blocked this website' , font = 'helvetica')
                display.place(x=200,y=200)
                pass
            else:
                host_file.write(inf.ip_address + " " + address + '\n')
                Label(inf.gui, text = "Blocked", font = 'arial').place(x=230,y =200)



def unblock():
    import interface as inf
    website_lists = inf.text_box.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (inf.host_path , 'r+') as host_file:
        file_content = host_file.readlines()
    for web in Website:
            if web in website_lists:
                with open (inf.host_path , 'r+') as f:
                    for line in file_content:
                        if line.strip(',') != website_lists:
                            f.write(line)
                            Label(inf.gui, text = "Unblocked", font = 'arial').place(x=350,y =200)
                            pass
                        else:
                            display=Label(inf.gui, text = 'This website is not currently blocked' , font = 'arial')
                            display.place(x=350,y=200)