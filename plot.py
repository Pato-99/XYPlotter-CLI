#!/usr/bin/env python3

import serial
import sys
from tqdm import tqdm

ser = serial.Serial("/dev/ttyACM0", 115200)
ser.flushInput()


def wait_for_ok():
    message = ser.readline().decode().strip()
    if message == "OK" or message == "ERR":
        return message


try:
    with open(sys.argv[1], "r") as gcode_file:
        lines = gcode_file.readlines()
        lines = [line.strip() for line in lines if line]  # remove line ends
        lines = [line for line in lines if line != ""]  # remove empty lines
        # lines = insert_dwell(lines, 120)  # pen up/down delays

        total_lines = len(lines)

        for line in tqdm(lines, desc="Plotting", unit="line"):
            # print(line)
            ser.write(f"{line}\n".encode())
            wait_for_ok()

except KeyboardInterrupt:
    print("Interrupting...")
    wait_for_ok()
    print("Homing...")
    ser.write("M3\n".encode())
    wait_for_ok()
    ser.write("G4 P120\n".encode())
    wait_for_ok()
    ser.write("G0 X0 Y0\n".encode())
    wait_for_ok()
