#!/usr/bin/env python3
import argparse
import glob
import serial
import sys

from tqdm import tqdm


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def wait_for_ok(serial_port):
    message = serial_port.readline().decode().strip()
    if message == "OK" or message == "ERR":
        return message


def homing(serial_port):
    print("Homing...")
    serial_port.write("M3;\n".encode())
    wait_for_ok(serial_port)
    serial_port.write("G4 P200;\n".encode())
    wait_for_ok(serial_port)
    serial_port.write("G0 X0 Y0;\n".encode())
    wait_for_ok(serial_port)


# Handle command line arguments
parser = argparse.ArgumentParser(
    prog="XY Plotter CLI tool",
    description="Send G-Code to the Plotter."
)
parser.add_argument('filename',
                    help="File containing G-Code")
parser.add_argument("--port",
                    help="Serial port of Plotter",
                    default="/dev/ttyACM0")
parser.add_argument('-l',
                    help="List available serial ports and exit.",
                    action='store_true')
args = parser.parse_args()


# Print available serial ports
if args.l:
    print("Available serial ports:")
    for port in serial_ports():
        print(f"\t{port}")
    exit(0)


try:
    with serial.Serial(args.port, 115200) as serial_port, open(args.filename, "r") as gcode_file:
        serial_port.flushInput()

        lines = gcode_file.readlines()
        lines = [line.strip() for line in lines if line]  # remove line ends
        lines = [line for line in lines if line != ""]  # remove empty lines

        try:
            for line in tqdm(lines, desc="Plotting", unit="line"):
                serial_port.write(f"{line}\n".encode())
                wait_for_ok(serial_port)
        except KeyboardInterrupt:
            print("Interrupting...")
            wait_for_ok(serial_port)
            homing(serial_port)
except serial.serialutil.SerialException as e:
    print(f"Could not open serial port '{args.port}'", file=sys.stderr)
except FileNotFoundError as e:
    print(f"Could not open file '{args.filename}'", file=sys.stderr)
