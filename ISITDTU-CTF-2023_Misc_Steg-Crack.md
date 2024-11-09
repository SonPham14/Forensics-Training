## Description
Description: Can you find the flag?
- md5sum raw.png `1ff6f4c2c06eec13cb5712f77bc57b64`
- md5sum chall.zip `1c2772dc487472a3c273f6f7318fd11a`

## Solving

### Cracking
The challenge give 2 file: chall.zip file is a ZIP archive's password and raw.png file.

In this challenge, we use `bkcrack` (or `pkcrack`) to crack zip archive. To know why and how to use this tools, go to [Reference](https://hackmd.io/_uploads/ByUvBY5-a.png)


First, seeing a list of entry names and metadata in chall.zip:

![](https://hackmd.io/_uploads/B1vEHtqZa.png)


We can see the zip file contains chall.png which has encryption is ZipCrypto. We also see that chall.png is stored uncompressed.

Create a plaintext that we know in a PNG file. We can take the first 33 bytes from raw.png:

![](https://hackmd.io/_uploads/Sy72rtc-6.png)

Use `bkcrack` with follow command:
`bkcrack -C chall.zip -c chall.png -p plain`

When we have 3 keys, we can create a new encrypted archive based on chall.zip with a new password and `123` in an example:
`bkcrack -C chall.zip -k 0661a350 4d92a8d8 3458f39e -U cracked.zip 123`

Unzip `cracked.zip` with the new password `123`, we get chall.png.


### Steganography

The chall.png and raw.png is the same. Let's compare some pixels.

If red is greater, print 1, else print 0 or vice versa. Write a code to get binary strings.

Open the text editor, edit the width with 58 characters we can see something interesting.

![](https://hackmd.io/_uploads/HkRfUFqb6.png)

That is a QR code. We can use some tool or coding to get a QR code image from binary string. Scan it and get the flag.

![](https://hackmd.io/_uploads/SJiZLt5-T.png)

flag: `ISITDTU{4vv3s0M3_y0u_f0uNd_M333!!E4sy_riGHt?}`


## References

[https://github.com/kimci86/bkcrack](https://github.com/kimci86/bkcrack)

[https://github.com/keyunluo/pkcrack](https://github.com/keyunluo/pkcrack)
