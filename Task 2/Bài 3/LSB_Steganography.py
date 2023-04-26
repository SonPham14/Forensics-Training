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
    print(result)
    return result

img = Image.open('D:\\Training_Forensics\\Bai2.png').convert('RGB')
arr = np.array(img)

name = "Son"
bin_name = ''.join([bin(ord(i))[2:].zfill(8) for i in name])

for i in range(8):
    r, g, b = arr[0][i]
    r = int(change('r', bin(r)[2:].zfill(8), bin_name[3*i]), 2)
    g = int(change('g', bin(g)[2:].zfill(8), bin_name[3*i+1]), 2)
    b = int(change('b', bin(b)[2:].zfill(8), bin_name[3*i+2]), 2)
    
    arr[0][i] = [r, g, b]

new_img = Image.fromarray(arr)
new_img.save('D:\\Training_Forensics\\Bai2_LSB.png')
print("Success")
