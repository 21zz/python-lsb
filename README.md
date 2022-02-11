# Least Significant Bit
Extremely simple LSB scripts for embedding messages in the least significant bit of a pixel's color in PNG images. I'm sure you could do this
with other image types, but I'm not confident in the reliability.
<br>
Well, I don't particularly care either. Not my specialization.

## How to Use
embed message: `python lsbenc.py /path/to/image.png "message to embed in the image"`

extract message: `python lsbdec.py /path/to/image.png`

## Credits
Yoinked code from [Juan Cortes](https://itnext.io/steganography-101-lsb-introduction-with-python-4c4803e08041)
for the main algorithm.

Also used code from [geeksforgeeks](https://www.geeksforgeeks.org/python-program-to-convert-binary-to-ascii/) to convert binary data to ASCII.

## TODO
 * Turn into one file as functions
 * Use argparse to choose functions to use (enc/dec)