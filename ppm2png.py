#! /usr/bin/env python3

# Converts raw pixel data into a PNG
# Usage ./ppm2png.py [file] [width] [height]

import os
import sys
from PIL import Image

if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} [file] [width] [height]")
    sys.exit(-1)

name, ext = os.path.splitext(sys.argv[1])

try:
    with open(sys.argv[1], 'rb') as infile:
        data = infile.read()
        image = Image.frombytes('RGB', (int(sys.argv[2]), int(sys.argv[3])), data, 'raw', 'BGRX')
        image.save(f"{name}.png")
except FileNotFoundError:
    print(f"Could not open file: {sys.argv[1]}")
    sys.exit(-1)
