import serial, time
print("===>inicio")
#ser=serial.Serial('COM15',baudrate=9600,bytesize=8,parity='N',stopbits=1)
ser = serial.Serial('COM16', 9600)
time.sleep(2)
ser.write(b'dato')
respuesta=ser.readline()
print(respuesta)
ser.close()
