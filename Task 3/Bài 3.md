## Crack file Zip Task3.zip
### Cách 1: Dùng John the Ripper
-	Đầu tiên, sử dụng lệnh zip2john password-protected.zip > Hash.txt để lưu mã băm của file zip ra file Hash.txt.

		zip2john Task3.zip > Hash.txt

-	Sau đó, để bẻ khóa băm, gõ lệnh sau đây:

		sudo john --wordlist=/usr/share/wordlist/rockyou.txt Hash.txt

![John](https://user-images.githubusercontent.com/103044792/235297166-01958716-5734-4b11-b073-e47a5bbcbc83.png)

Vậy mật khẩu là MANCHESTERUNITED

### Cách 2: Dùng Hashcat
-   Bước đầu tương tự như John the Ripper, tuy nhiên cần sửa lại format của file Hash.txt theo đúng dạng sau đây: '$pkzip$...$/pkzip$'

![image](https://user-images.githubusercontent.com/103044792/235297502-3c1222c0-5606-40e0-9a46-fa6e4ce1979f.png)

-   Tiếp theo gõ lệnh:

        hashcat -a 3 -m 17225 Hash.txt /usr/share/wordlist/rockyou.txt

Giải nén file Zip với mật khẩu MANCHESTERUNITED, ta được 3 file bookmarks.txt, dat2fish_stash.zip và README.txt.


## Crack file Zip dat2fish_stash.zip
### Cách 1: Dùng bkcrack với plaintext có sẵn.
Nhận thấy trong file dat2fish_stash.zip cũng có file bookmarks.txt nên ta sẽ lấy file này làm plaintext. Trong file này còn thiếu file Zip của plaintext nên ta sẽ nén Zip file bookmarks.txt mới có thể sử dụng bkcrack được. 

-   Gõ lệnh sau và chờ khoảng vài phút:

        ./bkcrack  -C dat2fish_stash.zip -c bookmarks.txt -P bookmarks.zip -p bookmarks.txt -d cracked.zip

Vậy là đã crack xong.

![image](https://user-images.githubusercontent.com/103044792/235333070-65b3a8ce-78d1-4ffa-ae91-d732dbee7420.png)

*Ở cách này các bạn có thể sử dụng pkcrack với cú pháp tương tự, có điều chạy khá lâu. Máy mình chạy mất khoảng 1 tiếng trong khi bkcrack chỉ 2 phút mà thôi.

