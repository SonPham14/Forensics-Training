from PIL import Image
import numpy as np

#bit 1 của red, bit 0 của green, bit 2 của blue
def change(s, b, c):
    if s == 'r':
        result = b[:6] + c + b[7:]
    elif s == 'g':
        result = b[:7] + c + b[8:]
    else:
        result = b[:5] + c + b[6:]
    return result

img = Image.open('D:\\Training_Forensics\\Bai2.png').convert('RGB')
arr = img.getdata()
new_arr = []
name = "PhamHongSon"
bin_name = ''.join([bin(ord(i))[2:].zfill(8) for i in name])

i = 0
for pixel in arr:
    if i < len(bin_name):
        r, g, b = pixel
        r = int(change('r', bin(r)[2:].zfill(8), bin_name[i]), 2)
        i += 1
        if i < len(bin_name):
            g = int(change('g', bin(g)[2:].zfill(8), bin_name[i]), 2)
            i += 1
        if i < len(bin_name):    
            b = int(change('b', bin(b)[2:].zfill(8), bin_name[i]), 2)
            i += 1
        new_arr.append((r, g, b))
    else:
        new_arr.append(pixel)
    
img.putdata(new_arr)
img.save('D:\\Training_Forensics\\Bai2_LSB.png')
print("Success")
