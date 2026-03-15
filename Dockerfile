# ใช้ Python Image แบบ lightweight
FROM python:3.11-slim

# ตั้งค่า Working Directory
WORKDIR /app

# คัดลอกไฟล์ requirements และติดตั้ง
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกโค้ดทั้งหมดเข้า Container
COPY . .

# สั่งรันแอปพลิเคชัน
CMD ["python", "main.py"]