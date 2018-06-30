import bluetooth

hostMACAddress = '4c:bb:58:fb:31:e8' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 6
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
try:
    client, clientInfo = s.accept()
    while 1:
        data = client.recv(size)
        if data:
            print(data)
        text1 = raw_input()
        if text1:    
           client.send(text1) # Echo back to client
except:	
    print("Closing socket")
    client.close()
    s.close()

