import serial, time
from serial.tools import list_ports
print("===>inicio")
port = list(list_ports.comports())
for p in port:
    print(p.device)
while True:
    ser=serial.Serial('COM16',baudrate=9600,bytesize=8,parity='N',stopbits=1)
    #ser = serial.Serial('COM3', 9600)
    time.sleep(2)
    ser.write(b'dato')
    respuesta=ser.readline()
    print(respuesta)
    ser.close()
    print("dentro del bucle")


    
