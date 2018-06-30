import bluetooth
import lightblue
import sys
from PyOBEX.client import Client

#print("enter the device name to send file/audio/video")
#target_name = sys.argv[1]
#target_name = sys.argv[1]
#target_name = "akanksha-HP-Pavilion-g4-Notebook-PC"
#target_name = "GT-S5282"
#target_name = "P55 Max"
#file_to_send = "/home/anisha/Music/bluetoth_project/l2capserver.py"
#file_to_send = "/home/anisha/Music/bluetoth_project/videoplayback.mp4"
#file_to_send = "/home/anisha/Music/Imagine Dragons - Demons.mp3"


obex_port = None
target_address = None

print("searching devices")

nearby_devices = bluetooth.discover_devices()

print("following are the bluetooth devices available nearby:")

for bdaddr in nearby_devices:
    print(bluetooth.lookup_name(bdaddr))
    

print("enter the device name to send file/audio/video")

target_name = raw_input()
print("enter file name to send with path")
file_to_send = raw_input()

for bdaddr in nearby_devices:
    #print(bluetooth.lookup_name(bdaddr))
    if(target_name == bluetooth.lookup_name(bdaddr)):
         print("found the target device !!")
         
         target_address = bdaddr
         print(target_address)
         break

#target_address = "48:D2:24:61:A6:4D" 
print("searching for the object push service")
services = lightblue.findservices(target_address)

#print("till here connected")
#services = lightblue.findservices(addr=lightblue.selectdevice()[0],servicetype=lightblue.OBEX)
#services = lightblue.findservices(addr=target_address,servicetype=lightblue.OBEX)
#address, serviceport, servicename = lightblue.selectservice()
#lightblue.obex.sendfile(address, serviceport, file_to_send)

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
            
