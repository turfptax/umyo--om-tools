import binascii

# Demo packet from serial USB receiver
data = b'O\xd5Bc8\xe2$\xb2\x8cX\x00\xb9d\x00 *\x06*\x1c*X*\x98*\xa0*J*\x05*\x08R\t\x01F\x00]\x00\x17\xb7t\xfa\xa2e\x14\xf5?\xc0\xa0\x03K\x0f\xab\xf9\x8d\x00\x00\x06\xcdO\xd5Bd8\xe2$\xb2\x8cX\x00\xb9d\x00!)\xf9)\xf9* *2*s*\x98*\xd3*\xa4R\xc6\x01\x92\x00\x97\x00[\xb7\x97\xfa\xa2e-\xf5E\xc2d\x03x\x0f\xfd\xf9\x8e\x00\x00\x06\xcaO\xd5Be8\xe2$\xb2\x8cX\x00\xb9d\x00"*9*\x02*\x06*\x04*"*H*\x8d*\xdfR\x1b\x01j\x00\xa2\x00k\xb7\xbd\xfa\xa0eI\xf5G\xc4\xa4\x04.\x11\x84\xf9\x8e\x00\x00\x06\xc7O\xd5Bf8\xe2$\xb2\x8cX\x00\xb9d\x00#+\t+\x0b*\xb7*C*\x1f*.*R*hT\x14\x01\xdc\x00\x91\x00;\xb7\xdf\xfa\x9dea\xf5H\xc6\x11\x04\xfd\x12p\xf9\x8d\x00\x00\x06\xc4'

import umyo_parser

#Creates the uMyo Devices array and uMyo class to the devices
umyo_parser.umyo_parse_preprocessor(data)

print(umyo_parser.umyo_list[0].batt)

# Set local variable to the 1st device in the umyo_list
umyo = umyo_parser.umyo_list[0]

# Prints the class of the umyo data
print(dir(umyo))

# Find these in umyo_class
var_names = ['last_pack_id',
             'unit_id',
             'packet_type',
             'data_count',
             'batt',
             'version',
             'steps',
             'data_id',
             'prev_data_id',
             'data_array',
             'device_spectr',
             'Qsg',
             'zeroQ', #[0,0,0,0]
             'yaw',
             'pitch',
             'roll',
             'dev_yaw',
             'dev_pitch',
             'dev_roll',
             'update_time',
             'yaw_speed',
             'roll_speed']

#print all of the variables in the umyo class object specified by var_names
print('-----Begin Packet Dump-----')
for i in var_names:
    print(i,eval(f'umyo.{i}'))

