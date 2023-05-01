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

        ./bkcrack  -C dat2fish_stash.zip -c bookmarks.txt -P bookmarks.zip -p bookmarks.txt -d cracked.zip

So the cracking is done.

![image](https://user-images.githubusercontent.com/103044792/235333125-f5a18387-7426-4a49-b412-f1dcfd35f264.png)

**Note: In this method you can use `pkcrack` with the same syntax, but it takes a long time to run. My computer runs for about 1 hour while `bkcrack` only takes 2 minutes.

