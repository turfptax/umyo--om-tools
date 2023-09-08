
# list serial devices


def serial_autofind():
    from serial.tools import list_ports
    print('1. Please unplug the uMyo Base Station USB stick')
    input('press enter to confirm')
    port = list(list_ports.comports())
    print('2. Please plug in uMyo Base Station')
    input('press enter to confirm')
    port_with_base_station = list(list_ports.comports())
    uMyoPort = False
    if port != port_with_base_station:
        for i,x in enumerate(port_with_base_station):
            if x not in port:
                uMyoPort = x
                print(f'uMyo port found: {x}')
    else:
        print('You may need to install the usb driver for uMyo Base Station')
        print('IF Device Manager(windows) Shos the following')
        print('CP2102N USB to UART Bridge Controller')
        print('you will need to download driver: https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers')
    return(uMyoPort)


def find_serial_port():
    from serial.tools import list_ports
    port = list(list_ports.comports())
    print('Listed Devices:')
    for i,p in enumerate(port):
        print(i,p.device)
        device = p.device
    print(i+1,'Autofind Serial Port')
    reply = int(input('Select device or run autofind: '))
    print('reply: ',reply,'len(port): ',len(port))
    print(f'{reply < len(port)}')
    if reply < len(port):
        device=port[reply]
        return device
    else:
        uMyoPort = serial_autofind()
        return uMyoPort

serial_port = str(find_serial_port()).split(' ')[0]
print(serial_port)

# read serial device
import serial
ser = serial.Serial(
    port=serial_port,\
    baudrate=921600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)
count=1

duration = 10000
data = []
print('serial status',ser.is_open)

print('starting loop')
for i in range(duration):
    line = ser.readline()
    if len(line) > 0:
        data.append(line)
        print(line)

print(ser.readline())
ser.close()
