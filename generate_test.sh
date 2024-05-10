#!/bin/bash


function generate_test_path() {
  vpype --config vpype_config.toml \
  rect 10mm 10mm 100mm 100mm  \
  line 8mm 10mm 8mm 110mm \
  line 8mm 110mm 3mm 110mm \
  line 3mm 110mm 8mm 10mm \
  line 10mm 112mm 110mm 112mm \
  line 110mm 112mm 10mm 118mm \
  line 10mm 118mm 10mm 112mm \
  rotate 45 \
  translate 130mm 20mm \
  rect 10mm 10mm 100mm 100mm  \
  line 8mm 10mm 8mm 110mm \
  line 8mm 110mm 3mm 110mm \
  line 3mm 110mm 8mm 10mm \
  line 10mm 112mm 110mm 112mm \
  line 110mm 112mm 10mm 118mm \
  line 10mm 118mm 10mm 112mm \
  linesort \
  gwrite -p xyplotter "gcode/test.gcode"
}


# Ensure that directory for G-Codes exists
mkdir -p gcode

# Create test path
generate_test_path 0.5mm

