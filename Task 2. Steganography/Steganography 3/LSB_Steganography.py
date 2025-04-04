from PIL import Image
import numpy as np

# bit 1 of red, bit 0 of green, bit 2 of blue
def Change(s, b, c):
    if s == 'r':
        result = b[:6] + c + b[7:]
    elif s == 'g':
        result = b[:7] + c + b[8:]
    else:
        result = b[:5] + c + b[6:]
    return result

img = Image.open('D:\\Training_Forensics\\Bai2.png').convert('RGB')
arr = img.getdata()

# Convert name string to binary string
name = "PhamHongSon"
bin_name = ''.join([bin(ord(i))[2:].zfill(8) for i in name])

# Modifies the RGB values of each pixel to hide a message and color values are stored in a new array called `new_arr`.
i = 0
new_arr = []
for pixel in arr:
    if i < len(bin_name):
        r, g, b = pixel
        r = int(Change('r', bin(r)[2:].zfill(8), bin_name[i]), 2)
        i += 1
        if i < len(bin_name):
            g = int(Change('g', bin(g)[2:].zfill(8), bin_name[i]), 2)
            i += 1
        if i < len(bin_name):    
            b = int(Change('b', bin(b)[2:].zfill(8), bin_name[i]), 2)
            i += 1
        new_arr.append((r, g, b))
    else:
        new_arr.append(pixel)

# Apply the modified pixel data stored in `new_arr` and save a new image.
img.putdata(new_arr)
img.save('D:\\Training_Forensics\\Bai2_LSB.png')
print("Success")
