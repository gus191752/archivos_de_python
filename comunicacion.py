import serial, time
from serial.tools import list_ports
print("===>inicio")
port = list(list_ports.comports())
for p in port:
    print(p.device)
while True:
    ser=serial.Serial('COM14',baudrate=9600,bytesize=8,parity='N',stopbits=1)
    #ser = serial.Serial('COM15', 115200)
    time.sleep(2)
    ser.write(b'3')
    #respuesta=ser.read()
    #respuesta=ser.read().decode('ASCII')
    respuesta=ser.readline().decode('utf-8')
    res= (respuesta)
    print('RX '+str(res))
    ser.write(b'2')
    time.sleep(2)
    ser.write(b'1')
    time.sleep(2)
    ser.close()
    print("dentro del bucle")