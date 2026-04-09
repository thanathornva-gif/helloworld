# FastAPI Security Playground (Hello World)

โปรเจกต์นี้เป็นแอปพลิเคชันตัวอย่างที่พัฒนาด้วย **FastAPI** ซึ่งออกแบบมาเพื่อใช้ในการศึกษาด้านความปลอดภัยของเว็บแอปพลิเคชัน โดยภายในโค้ดจะมีการใส่ช่องโหว่ความปลอดภัยแบบตั้งใจ (Intentional Vulnerabilities) เพื่อใช้สำหรับการทดสอบและเรียนรู้

> โปรเจกต์นี้มีช่องโหว่ร้ายแรง (เช่น SQL Injection, Command Injection)

## ฟีเจอร์หลัก
- แสดงข้อความ Hello World พื้นฐาน
- ระบบตรวจสอบสถานะ (Health Check)
- หน้าดึงข้อมูลผู้ใช้จากฐานข้อมูล SQLite
- ฟังก์ชัน Ping และคำนวณเลข
- การสุ่ม Token

## ช่องโหว่ความปลอดภัยที่พบในโปรเจกต์ (เพื่อการศึกษา)
1. **SQL Injection**: ที่เอนด์พอยต์ `/user` เนื่องจากการใช้ string formatting ในการสร้าง SQL query
2. **Command Injection**: ที่เอนด์พอยต์ `/ping` เนื่องจากการรับ input จากผู้ใช้ไปรันคำสั่ง system โดยตรง
3. **Dangerous Eval**: ที่เอนด์พอยต์ `/calculate` เนื่องจากการใช้ฟังก์ชัน `eval()` กับ input จากผู้ใช้
4. **Hardcoded Secret**: มีการฝัง API Secret ไว้ในโค้ดโดยตรง
5. **Debug Mode Enabled**: เปิดโหมด Debug ค้างไว้ใน production logic
6. **Weak Random**: ใช้การสุ่มที่คาดเดาได้ง่ายสำหรับ Token