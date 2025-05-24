from flask import Flask, render_template, request, send_file, flash
import os
from rsa_utils import generate_keys, save_keys, load_keys, sign_file, verify_signature

app = Flask(__name__)
app.secret_key = 'secret_key'
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Sinh khóa nếu chưa có
if not os.path.exists("private_key.pem") or not os.path.exists("public_key.pem"):
    priv, pub = generate_keys()
    save_keys(priv, pub)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        file_path = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(file_path)

        with open(file_path, "rb") as file:
            file_data = file.read()

        private_key, _ = load_keys()
        signature = sign_file(private_key, file_data)

        # Lưu chữ ký
        signature_path = os.path.join(UPLOAD_FOLDER, f.filename + ".sig")
        with open(signature_path, "wb") as sig_file:
            sig_file.write(signature)

        flash("File đã được ký số thành công!", "success")
        return render_template('index.html', filename=f.filename)

    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    file = request.files['file']
    sig = request.files['signature']
    file_data = file.read()
    signature = sig.read()

    _, public_key = load_keys()
    valid = verify_signature(public_key, file_data, signature)

    if valid:
        flash("✅ Chữ ký hợp lệ!", "success")
    else:
        flash("❌ Chữ ký không hợp lệ!", "danger")
    return render_template('index.html')

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
