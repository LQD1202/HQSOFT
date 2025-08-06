# Ứng dụng Phát Hiện Đối Tượng với YOLOv8 + Streamlit

## 📦 Tính năng chính

- Tải ảnh từ máy và hiển thị trực tiếp
- Phát hiện đối tượng sử dụng mô hình YOLOv8 (`yolov8n.pt`)
- Hiển thị ảnh gốc và ảnh kết quả theo hàng ngang
- Giao diện đơn giản, thân thiện người dùng

---

## ⚙️ Hướng dẫn cài đặt và chạy ứng dụng

### 1. Clone hoặc tải mã nguồn

```bash
git clone https://github.com/your-username/yolov8-streamlit-app.git
cd HQSOFT
````


### 2. Tạo môi trường ảo (tuỳ chọn)

```bash
conda create -n od
```

### 3. Cài đặt thư viện phụ thuộc

```bash
pip install -r requirements.txt
```

### 4. Chạy ứng dụng

```bash
streamlit run app.py
```

Ứng dụng sẽ chạy tại địa chỉ: [http://localhost:8501](http://localhost:8501)

---

## 📁 Cấu trúc thư mục

```
HQSOFT/
├── app.py               # Mã nguồn chính
├── yolov8n.pt           # Trọng số YOLOv8 (nếu chưa có, sẽ tự tải)
├── requirements.txt     # Danh sách thư viện
└── README.md            # Hướng dẫn sử dụng
```

---

## 📷 Demo giao diện

![demo](demo/original.jpg)

---

## 📌 Ghi chú

* Trọng số YOLOv8 (`yolov8n.pt`) sẽ được tự động tải nếu chưa có.
* Có thể thay thế bằng mô hình khác như `yolov8s.pt`, `yolov8m.pt` nếu muốn độ chính xác cao hơn.

