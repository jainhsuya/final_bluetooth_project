import bluetooth
import lightblue
import Tkinter
from Tkinter import *
from PyOBEX.client import Client

top = Tkinter.Tk()


global Listbox1

target_name = "P55 Max"
file_to_send = "/home/anisha/Music/bluetoth_project/videoplayback.mp4"

obex_port = None
target_address = None

print("searching devices")

nearby_devices = bluetooth.discover_devices()

def show_devices():
        global Listbox1
        for bdaddr in nearby_devices:
            #print(bluetooth.lookup_name(bdaddr))
            Listbox1.insert(END, bluetooth.lookup_name(bdaddr))
            if(target_name == bluetooth.lookup_name(bdaddr)):
                 print("found the target device !!")
                 
                 target_address = bdaddr
                 #print(target_address)
                 break





print("searching for the object push service")
services = lightblue.findservices(target_address)
for service in services:
    if(service[2] == "OBEX Object Push"):
          obex_port = service[1]
          print("ok service '", service[2], "' is in port",service[1], "!")
          break



print("sending a file")
try:
   lightblue.obex.sendfile(target_address, service[1], file_to_send)
   print("completed!\n")

except:
     print("an error occurred while sending file\n")
     
     


#Button1 = Button(command = onclick)
#Listbox1 = Listbox() 



def main():
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("600x450+429+131")
        top.title("New Toplevel 1")
        top.configure(background="#1ea966")
        top.configure(highlightcolor="black")

        global Listbox1

        menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = menubar)



        Label1 = Label(top)
        Label1.place(relx=0.23, rely=0.02, height=38, width=276)
        Label1.configure(highlightbackground="#76d92c")
        Label1.configure(highlightcolor="#d30000")
        Label1.configure(highlightthickness="10")
        Label1.configure(relief=RIDGE)
        Label1.configure(state=ACTIVE)
        Label1.configure(text='''My Bluetooth Application''')
        Label1.configure(width=276)

        Label2 = Label(top)
        Label2.place(relx=0.28, rely=0.13, height=38, width=206)
        Label2.configure(foreground="#e43e00")
        Label2.configure(highlightbackground="#13f806")
        Label2.configure(highlightthickness="10")
        Label2.configure(text='''Available Bluetooth Devices''')
        Label2.configure(width=206)

        Listbox1 = Listbox(top)
        Listbox1.place(relx=0.28, rely=0.24, relheight=0.3, relwidth=0.34)
        Listbox1.configure(background="white")
        Listbox1.configure(font="TkFixedFont")
        Listbox1.configure(width=204)

        Button1 = Button(top)
        Button1.place(relx=0.38, rely=0.6, height=26, width=77)
        Button1.configure(activebackground="#d9d9d9")
        Button1.configure(highlightbackground="#fe1b16")
        Button1.configure(highlightthickness="0")
        Button1.configure(text='''Send''')
        Button1.configure(width=77)

        Label3 = Label(top)
        Label3.place(relx=0.02, rely=0.02, height=118, width=126)
        img1 = PhotoImage(file="/home/anisha/Music/bluetoth_project/final_bluetooth_project/bluetooth_icon.png")
        Label3.configure(image=img1)
        Label3.configure(text='''Label''')
        Label3.configure(width=126)

        Text1 = Text(top)
        Text1.place(relx=0.2, rely=0.82, relheight=0.14, relwidth=0.46)
        Text1.configure(background="white")
        Text1.configure(font="TkTextFont")
        Text1.configure(selectbackground="#c4c4c4")
        Text1.configure(width=276)
        Text1.configure(wrap=WORD)
        
        show_devices()

        top.mainloop()

if __name__ == '__main__':
     main()

       
