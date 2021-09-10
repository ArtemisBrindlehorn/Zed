# Are the jumpers in the correct spot on the board (pos. 2-3)?
# Is the USB converter properly placed in the socket?

from sys import argv
import time
import serial

my_sum = 0

script, com_port = argv

ser = serial.Serial(com_port, 19200)
print(ser.name)

# Frame structure
# Byte 0 : command
# Byte 1 : Board Address
# Byte 2 : Data
# Byte 3 : Check sum (XOR from Byte 0, Byte 1, Byte 2)

# Initialization command testing (send)
my_pack = bytearray(4)
my_pack[0] = 0x01 # command
my_pack[1] = 0x01 # Address
my_pack[2] = 0x00 # data (irrelevant for this example)
my_pack[3] = (my_pack[0] ^ my_pack[1] ^ my_pack[2])
print(my_pack)

# Control of relays by bit location
# K8 is bit 7, K7 is bit 6, ... , K1 is bit 0
print("Enter values for the relay(s) you wish to set.")
print("Each valid integer (from 1-8) will select a relay to set.")
print("Pressing ENTER without a valid integer will set the relays.")
while True:
    try:
        # check to see if the input is an integer
        numb = int(input("Select a relay to turn on: "))

        #bounding for the relay locations
        if (numb > 0) and (numb < 9):
            # offset calculation for proper bit setting
            my_sum += 1 << (numb - 1)
            print(my_sum)
    except ValueError:
        break

# Re-set the packet command, add the relay targets, recalculate XOR values
my_pack[0] = 0x03       # set relays
my_pack[2] = my_sum     # data from relay set loop above
my_pack[3] = (my_pack[0] ^ my_pack[1] ^ my_pack[2])



# for 1000 attempts, write to the serial port
# attempt number is large enough to see values on terminal monitor
for i in range(1000):
    ser.write(my_pack)
    time.sleep(0.01)

ser.close()
