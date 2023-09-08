#kinda main

import umyo_parser
import display_stuff

def select_port(port):
    devices = []
    port_selected = False
    print(f'Port:{port}')
    for i,p in enumerate(port):
        print(i,p.device)
        #device = p.device
        devices.append(p.device)
    while not port_selected:
        selected_port = input('Please Enter Port Number')
        try:
            device = devices[int(selected_port)]
            port_selected = True
        except:
            print(f'Error please enter an integer within range of 0 - {len(devices)}')
    print("===")
    print(f'{device} selected')
    return(device)

# list
from serial.tools import list_ports
port = list(list_ports.comports())
device = select_port(port) 
#read
import serial
ser = serial.Serial(port=device, baudrate=921600, parity=serial.PARITY_NONE, stopbits=1, bytesize=8, timeout=0)

print("conn: " + ser.portstr)
last_data_upd = 0
display_stuff.plot_init()
parse_unproc_cnt = 0
while(1):
    cnt = ser.in_waiting
    if(cnt > 0):
        print(parse_unproc_cnt,type(parse_unproc_cnt))
        cnt_corr = parse_unproc_cnt/200
        data = ser.read(cnt)
        parse_unproc_cnt = umyo_parser.umyo_parse_preprocessor(data)
        if type(parse_unproc_cnt) == "NoneType":
            pass
        parser_test = umyo_parser.umyo_get_list()
        if len(parser_test) > 0 :
            dat_id = display_stuff.plot_prepare(parser_test)
            d_diff = 0
            if not (dat_id is None):
                d_diff = dat_id - last_data_upd
            if(d_diff > 2 + cnt_corr):
                #display_stuff.plot_cycle_lines()
                display_stuff.plot_cycle_spg()
                last_data_upd = dat_id

