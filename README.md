# XY Plotter CLI

Utilities and sample files for XY Plotter.

## Installing python dependencies

1. Install Python virtual environment: `pyhton -m pip venv .venv`
2. Activate the virtual environment: `source .venv/bin/activate`
3. Install required packages: `pip install -r requirements.txt`

## Generating G-Code from svg

For generatign G-Code fron svg files a command line utility `vpype` and it's plugin `vpype-gcode` is used. Configuration for `vpype-gcode` plugin is provided in file `vpype_config.toml`. It has to be specified manually when generating G-Code file. Consult `vpype` documentation for more details of how to use it.

Basic usage:

`vpype --config vpype_config.toml read in.svg gwrite -p xyplotter out.gcode`

## Plotting the G-Code file

A G-Code file can be plotted using `plot.py` utility as follows:

`python plot.py in.gcode --port /dev/ttyACM0`

In case we do not know the exact serial port the Plotter is connected to, `plot.py` utility can list all available serial ports when `-l` flag is specified:

`python plot.py in.gcode -l`
