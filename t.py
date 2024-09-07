import serial, time
from serial.tools import list_ports
print("===>inicio")
port = list(list_ports.comports())
for p in port:
    print(p.device)
while True:
    ser=serial.Serial('COM15',baudrate=11500,bytesize=8,parity='N',stopbits=1)
    #ser = serial.Serial('COM15', 115200)
    #time.sleep(2)
    ser.write(b'3u')
    #respuesta=ser.readline().decode('utf-8')
    #respuesta=ser.readline().decode('ASCII')
    respuesta=ser.readline()
    res= (respuesta)
    print('RX '+str(res))
    time.sleep(1)
    ser.write(b'gustavo')
    ser.close()
    print("dentro del bucle")