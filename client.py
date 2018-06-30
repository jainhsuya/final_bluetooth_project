import bluetooth

#serverMACAddress = 'D8:16:C1:55:E9:0A'
serverMACAddress = '48:D2:24:61:A6:4D'
port = 10
size=1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
print("connected with phone")
while 1:
    text = raw_input() # Note change to the old (Python 2) raw_input
    if text == "quit":
       break
    s.send(text)
    data = s.recv(size)
    if data:
      print(data)
sock.close()

