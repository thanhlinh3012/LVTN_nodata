# LVTN_TRUY VẤN ẢNH TRONG TẬP DỮ LIỆU ẢNH DỰA TRÊN ĐẶC TRƯNG RIÊNG
# Chuẩn bị: Cài đặt python3, pip, OpenCV; tải tập dữ liệu ảnh Oxford-5K
## Cài đặt python

Mở command line để kiểm tra phiên bản python. Phiên bản đang sử dụng là Python 3.7.3  

Truy cập [Python.org](https://www.python.org/downloads/) để tải và cài đặt Python

Kiểm tra việc cài đặt thành công Python bằng cách mở command line và gõ lệnh sau:

 ```
  python --version
 ```
 
 ## Cài đặt pip
 Với phiên bản python hiện tại, bạn có thể bỏ qua bước này vì

Từ phiên bản python 3.4 trở đi, PIP đã được cài sẵn trong python
Kiểm tra pip đã được cài đặt thành công bằng cách gõ lệnh

 ```
  pip --version
 ```
 
 ## Cài đặt thư viện OpenCV
 
Cài đặt OpenCV thông qua lệnh

 ```
  pip install opencv-python
 ```
 
 Kiểm tra phiên bản OpenCV thông qua gói imutils được cài đặt qua lệnh
 
 ```
  pip install imutils
 ```
 ## Tải tập dữ liệu ảnh Oxford-5K
 Tải tập dữ liệu ảnh Oxford-5K ở [Link](https://www.robots.ox.ac.uk/~vgg/data/oxbuildings/) này.
 
 # Cài đặt project
 ## Clone repository theo lệnh sau
  ```
  git clone https://github.com/thanhlinh3012/LVTN_nodata
 ```
## Tạo thư mục ảnh dữ liệu
Tạo thư mục **dataset** chứa toàn bộ tập ảnh dữ liệu ảnh Oxford-5K vừa tải ở trên.

## Tạo thư mục ảnh truy vấn
Tạo thư mục **queries** chứa các ảnh cần truy vấn.

## Chạy dự án thực hiện các lệnh sau
Sử dụng lệnh bên dưới để trích xuất các vector đặc trưng của ảnh dữ liệu và lưu chúng vào file *index.csv*:

 ```
 python index.py --dataset dataset --index index.csv
 ```
 Sử dụng lệnh bên dưới để thực hiện truy vấn ảnh:
  ```
  python search.py --index index.csv --query queries/q4.jpg --result-path dataset
 ```




