import sys
import re
import datetime
from PIL import Image

# file path
file_path = sys.argv[1]

# try to read file as binary then make a list of pixels
try:
    with open(file_path, "rb") as fp:
        img = Image.open(fp)
        pixels = list(img.getdata())
except IOError:
    print("not correct file path dumbass")
    exit(1)

msg_out = []
width, height = img.size
i = 0
for x in range(0, width):
    for y in range(0, height):
        pixel = list(img.getpixel((x, y)))
        for n in range(0, 3):
            msg_out.append(pixel[n] & 1)


data = "".join([str(x) for x in msg_out])

letters = []

try:
    i = 0
    while i < len(data)-7:
        newstr = ""
        for j in range(i, i+8):
            newstr += data[j]
        binary_int = int(newstr, 2)
        byte_number = binary_int.bit_length() + 7 // 8
        binary_array = binary_int.to_bytes(byte_number, "big")
        ascii_text = binary_array.decode()
        letters.append(ascii_text.strip())
        i += 8
except:
    None

for l in letters:
    if l != "":
        print(l, end="")
