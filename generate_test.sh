#!/bin/bash


vpype --config vpype_config.toml \
penwidth 0.5mm \
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
gwrite -p xyplotter out.gcode


#G00 X8 Y-10
#M4;
#G4 P200;
#G01 X8 Y-110;
#G01 X3 Y-110;
#G01 X8 Y-10;
#M3;
#G4 P200;
#
#G00 X10 Y-112;
#M4;
#G4 P200;
#G01 X110 Y-112;
#G
