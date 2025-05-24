# 🔐 RSA File Signer Web App

Ứng dụng web đơn giản dùng Flask để **ký số và xác minh chữ ký số** của file sử dụng **RSA**.

## 🚀 Chức năng

- Upload file và ký bằng RSA private key
- Tải file đã ký và chữ ký
- Upload file + chữ ký để xác minh tính hợp lệ
- Giao diện web HTML đơn giản, dễ dùng

## 🛠 Công nghệ sử dụng

- Python 3
- Flask
- cryptography (mã hóa RSA)

## 📁 Cấu trúc thư mục

├── app.py # Flask app chính
├── rsa_utils.py # Hàm sinh khóa, ký và xác minh chữ ký
├── private_key.pem # Private key RSA (không nên commit)
├── public_key.pem # Public key RSA
├── index.html # Giao diện người dùng
└── uploads/ # Nơi lưu trữ file và chữ ký

## ⚙️ Cách chạy

1. Cài thư viện:
   ```bash
pip install flask cryptography
python app.py
http://127.0.0.1:5000/

---

### ✅ **2. File `.gitignore` (để tránh đẩy private key và file upload)**

Tạo file `.gitignore` với nội dung:

```gitignore
__pycache__/
*.pyc
uploads/
private_key.pem
