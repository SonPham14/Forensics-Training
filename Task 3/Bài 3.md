Giải chall dưới đây, thử giải bằng 2 cách sử dụng pkcrack hoặc bkcrack. Viết lại các bước làm kể cả cách đó không hoạt động.
Gợi ý: File Zip đầu dùng John/Hash, file Zip sau dùng bkcrack/pkcrack.

#### Cách 1: Dùng John the Ripper
-	Đầu tiên, sử dụng lệnh zip2john password-protected.zip > Hash.txt để lưu mã băm của file zip ra file Hash.txt.

		zip2john Task3.zip > Hash.txt

-	Sau đó, để bẻ khóa băm, gõ lệnh sau đây:

		sudo john --wordlist=/usr/share/wordlist/rockyou.txt Hash.txt

![John](https://user-images.githubusercontent.com/103044792/235297166-01958716-5734-4b11-b073-e47a5bbcbc83.png)

Vậy mật khẩu là MANCHESTERUNITED

#### Cách 2: Dùng Hashcat
-   Bước đầu tương tự như John the Ripper, tuy nhiên cần sửa lại format của file Hash.txt theo đúng dạng sau đây: $pkzip$...$/pkzip$

![image](https://user-images.githubusercontent.com/103044792/235297502-3c1222c0-5606-40e0-9a46-fa6e4ce1979f.png)

-   Tiếp theo gõ lệnh:

        hashcat -a 3 -m 17225 Hash.txt /usr/share/wordlist/rockyou.txt
        
