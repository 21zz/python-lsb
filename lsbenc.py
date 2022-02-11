import sys
from datetime import datetime
from PIL import Image
import imghdr

debug = False
# file path
file_path = sys.argv[1]
# message to embed
message = sys.argv[2]

# ensure PNG file
if imghdr.what(file_path) != 'png':
    print("only png files")
    exit(-1)

# try to read file as binary then make a list of pixels
try:
    with open(file_path, "rb") as fp:
        img = Image.open(fp)
        pixels = list(img.getdata())
except IOError:
    print("not correct file path dumbass")
    exit(1)

# make message into binary string
binary_message = ''.join(format(ord(i), '08b') for i in message)
if debug:
    print(binary_message)

i = 0
width, height = img.size
for x in range(0, width):
    for y in range(0, height):
        pixel = list(img.getpixel((x, y)))
        for n in range(0, 3):
            if(i < len(binary_message)):
                pixel[n] = pixel[n] & ~1 | int(binary_message[i])
                i += 1
        img.putpixel((x, y), tuple(pixel))

# embedded_HH-MM-SS.png
filename = "embedded_" + datetime.now().strftime("%H-%M-%S") + ".png"
img.save(filename, "PNG")
print("Saved message to " + filename)
