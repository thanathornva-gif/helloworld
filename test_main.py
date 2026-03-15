from fastapi.testclient import TestClient
from main import app

# สร้าง client เพื่อใช้ทดสอบ
client = TestClient(app)

def test_read_root():
    """ทดสอบ Endpoint / ว่าส่งข้อความถูกต้องไหม"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World from FastAPI!", "status": "online"}

def test_health_check():
    """ทดสอบ Endpoint /health"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}