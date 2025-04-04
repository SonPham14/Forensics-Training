## Crack Task3.zip Zip file
### Method 1: Using John The Ripper
-	First, use the `zip2john` command followed by the name of the password-protected zip file and redirect the output to a file named Hash.txt to save the hash of the zip file.

		zip2john Task3.zip > Hash.txt

-	Then, to crack the hash, type the following command:

		sudo john --wordlist=/usr/share/wordlist/rockyou.txt Hash.txt

![John](https://user-images.githubusercontent.com/103044792/235297166-01958716-5734-4b11-b073-e47a5bbcbc83.png)

So password is `MANCHESTERUNITED`

### Method 2: Using Hashcat.
-   The first step is similar to John The Ripper, but we need to correct the format of the Hash.txt file in the following format: `$pkzip$...$/pkzip$`

![image](https://user-images.githubusercontent.com/103044792/235297502-3c1222c0-5606-40e0-9a46-fa6e4ce1979f.png)

-   Next type the following command:

        hashcat -a 3 -m 17225 Hash.txt /usr/share/wordlist/rockyou.txt

Extract the zip file with password `MANCHESTERUNITED`, we get 3 files `bookmarks.txt`, `dat2fish_stash.zip` and `README.txt`.


## Crack dat2fish_stash.zip Zip file.
### Method 1: Using `bkcrack` with available plaintext.
Noticing that the dat2fish_stash.zip file also contains the bookmarks.txt file, we can use this file as plaintext. The plaintext Zip file is missing in this file, so we will compress the bookmarks.txt file into a Zip file before we can use `bkcrack`.

-   Type the following command and wait for a few minutes:

        ./bkcrack  -C dat2fish_stash.zip -c bookmarks.txt -P bookmarks.zip -p bookmarks.txt

![image](https://user-images.githubusercontent.com/103044792/235562838-18fa9ed2-db71-470a-a8dc-63df5d2bb6b9.png)

We get 3 keys `99075ea6 102ed4f6 fcaa1b2b`, use it to change password of protected-zip file:

	./bkcrack -C dat2fish_stash.zip -k 99075ea6 102ed4f6 fcaa1b2b -U cracked.zip 123456

Finish. Unzip that file with password `123456`

**Note: In this method you can use `pkcrack` to solve this challenge.

### Method 2: Using `bkcrack` with unavailable plaintext.
This part will crack the zip file without using available plaintext. That is, based on the files contained in the zip file to crack.

I'll update this in the future if I can get it resolved.
