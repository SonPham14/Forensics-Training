## 1. File Structure
### Một tệp PNG bao gồm Chữ kí tệp (File signature) theo sau đó là một chuỗi các Chunks.
### Hình ảnh PNG hợp lệ phải chứa một đoạn IHDR, một hoặc nhiều đoạn IDAT và một đoạn IEND.
    
### 1.1. Chữ kí tệp (File signature)
	Tám byte đầu tiên của tệp PNG luôn luôn chứa những giá trị sau:
        (dec)       137  80  78  71  13  10  26  10
        (hex)        89  50  4e  47  0d  0a  1a  0a
        (ASCII)    \211   P   N   G  \r  \n \032 \n
 
- Chữ ký này vừa xác định tệp là tệp PNG vừa cung cấp để phát hiện ngay các sự cố truyền tệp phổ biến.
- Hai byte đầu tiên (89 50) phân biệt các tệp PNG trên các hệ thống nhằm xác định một loại tệp duy nhất.
- Byte đầu tiên (89) được chọn dưới dạng giá trị không phải ASCII để giảm - xác suất tệp văn bản có thể bị nhận dạng sai là tệp PNG.
- Các byte từ hai đến bốn (50 4e 47) là tên định dạng tệp (PNG).
        
###    1.2. Chunk IHDR Image header.
- IHDR là một phần quan trọng trong tệp PNG chứa header. Nó phải xuất hiện đầu tiên trong một hình ảnh PNG hợp lệ.
- Bắt đầu là tên của chunk IHDR: 49 48 44 52. Theo sau đó là 8 byte chứa thông tin về Chiều rộng (Width) và Chiều cao (Height) của hình ảnh. Đơn vị tính bằng pixel.
- []()   Ngoài ra còn có một số thông tin khác có thể tham khảo thêm: [IHDR](http://png.cybermirror.org/spec/1.2/PNG-Chunks.html#C.IHDR)
        
###    1.3. Chunk PLTE Palette.
	Đoạn PLTE chứa từ 1 đến 256 mục bảng màu, mỗi mục Một chuỗi ba byte có dạng:
		Red:   1 byte (0 = black, 255 = red)
		Green: 1 byte (0 = black, 255 = green)
		Blue:  1 byte (0 = black, 255 = blue)
- Số lượng mục được xác định từ độ dài khối. Một đoạn Độ dài không chia hết cho 3 là một lỗi.
    
###    1.4. IDAT Image data.
- Đoạn bắt đầu: 49 44 41 54
- Chứa dữ liệu hình ảnh.
- Có thể có nhiều khối IDAT. Nếu vậy, chúng phải xuất hiện liên tiếp mà không có khối can thiệp nào khác.
- Tệp PNG trong đó mỗi đoạn IDAT Chỉ chứa một byte dữ liệu hoặc thậm chí không chứa dữ liệu nào vẫn được xem là hợp lệ, mặc dù gây lãng phí đáng kể không gian lưu trữ.
		
###    1.5. IEND Image trailer.
- IEND phải xuất hiện cuối cùng đánh dấu sự kết thúc của Luồng dữ liệu PNG.
- Đoạn kết thúc của IEND: 49 45 4e 44 ae 42 60 82
    
