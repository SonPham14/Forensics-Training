from PIL import Image
import numpy as np

def Extract_data(p, c):
    if c == 'r':
        return bin(p)[-2]
    elif c == 'g':
        return bin(p)[-1]
    else:
        return bin(p)[-3]

img = Image.open("D:\\Training_Forensics\\Bai2_LSB.png").convert('RGB')
data = img.getdata()
message_bits = ""

for pixel in data:
    r, g, b = pixel
    message_bits += Extract_data(r, 'r')
    message_bits += Extract_data(g, 'g')
    message_bits += Extract_data(b, 'b')


i = 0
message = ""
while message_bits[i:i+8] != "11111111":
    message += chr(int(message_bits[i:i+8], 2))
    i += 8

print(message)
