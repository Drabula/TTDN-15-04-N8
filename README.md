# Quản Lý Khách Hàng

## 1. Giới thiệu

Dự án **Quản Lý Khách Hàng** cung cấp các chức năng chính nhằm hỗ trợ doanh nghiệp trong việc quản lý và chăm sóc khách hàng hiệu quả. Hệ thống giúp theo dõi thông tin khách hàng, hỗ trợ khách hàng, thống kê hiệu suất làm việc của nhân viên và bảng xếp hạng khách hàng mua hàng. Ngoài ra, người dùng còn có thể thêm sản phẩm và đơn hàng của khách hàng.

## 2. Chức năng chính

- **Xem thông tin khách hàng**  
- **Hỗ trợ khách hàng**  
- **Thống kê hỗ trợ của nhân viên**  
- **Bảng xếp hạng khách hàng mua hàng**  

### Chức năng phụ

- **Thêm sản phẩm**  
- **Thêm đơn hàng sản phẩm của khách hàng**  

## 3. Công nghệ sử dụng

![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

## 4. Cài đặt môi trường

### 4.1. Clone dự án
```sh
git clone https://gitlab.com/Drabula/TTDN-15-04-N8.git
cd TTDN-15-04-N8
```

### 4.2. Cài đặt các thư viện cần thiết
Chạy lệnh sau để cài đặt các thư viện bắt buộc:
```sh
sudo apt-get install libxml2-dev libxslt-dev libldap2-dev libsasl2-dev \
libssl-dev python3.10-distutils python3.10-dev build-essential libffi-dev \
zlib1g-dev python3.10-venv libpq-dev
```

### 4.3. Khởi tạo môi trường ảo
```sh
python3.10 -m venv ./venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## 5. Cấu hình Database
Hệ thống sử dụng PostgreSQL chạy trên Docker. Để khởi tạo database, thực hiện:
```sh
sudo apt install docker-compose
sudo docker-compose up -d
```

## 6. Cấu hình hệ thống

### 6.1. Tạo tệp `odoo.conf`
Tạo tệp `odoo.conf` với nội dung sau:
```ini
[options]
addons_path = addons
db_host = localhost
db_password = odoo
db_user = odoo
db_port = 5434
xmlrpc_port = 8069
```

## 7. Chạy hệ thống

Chạy lệnh sau để khởi động hệ thống:
```sh
python3 odoo-bin.py -c odoo.conf -u all
```
Sau khi chạy xong, truy cập [http://localhost:8069/](http://localhost:8069/) để đăng nhập vào hệ thống.

## 8. Hình ảnh minh họa 📸

### **Trang quản lý khách hàng**

![img.png](img.png)
trang quản lý thông tin khách hàng
![img_1.png](img_1.png)
trang quản lý hỗ trợ khách hàng
![img_2.png](img_2.png)
trang thống kê hỗ trợ khách hàng
![img_3.png](img_3.png)
trang xếp hạng khách hàng
![img_4.png](img_4.png)
trang quản lý email và gửi
![img_5.png](img_5.png)
trang chi tiết đơn hàng
![img_6.png](img_6.png)
trang chi tiết sản phẩm

---
**Hoàn tất cài đặt!** 🚀