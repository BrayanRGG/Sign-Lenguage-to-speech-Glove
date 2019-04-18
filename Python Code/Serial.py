import serial

ser = serial.Serial(port='COM4', baudrate='9600', bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=2)
try:
	ser.isOpen()
	print("Serial port is open")
except:
	print("Error")
	exit()

if(ser.isOpen()):
	try:
		while(1):
			print(ser.readline())
	except EXCEPTION:
		print("Error")

else:
	print("Cannot Open Serial Port")
