#!/bin/bash

# Ensure that gcode directory exists
mkdir -p gcode

# CVUT sample
vpype --config vpype_config.toml \
read svg/cvut.svg \
scale -o 0 0 2 2 \
linesort \
gwrite -p xyplotter gcode/cvut.gcode

# Flower sample
vpype --config vpype_config.toml \
read svg/flower.svg \
linesort \
gwrite -p xyplotter gcode/flower.gcode

# Maker Faire sample
vpype --config vpype_config.toml \
read svg/mfprague-logo.svg \
linesort \
scale -o 0 0 0.5 0.5 \
translate 20mm 20mm \
linesort \
gwrite -p xyplotter gcode/mfprague-logo.gcode

# Benchmark sample
./generate_test.sh
