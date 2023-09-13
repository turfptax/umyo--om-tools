#!python3

with open('lask-packets.txt') as f:
    lask_lines = f.readlines()

with open('umyo-packets.txt') as f:
    umyo_lines = f.readlines()


print(umyo_lines[0])
