# Love_Prediction: Using HPC and Monte Carlo Simulation

**Love_Prediction** เป็นโปรเจกต์ที่ใช้เทคนิค Monte Carlo Simulation ในการทำนายความรักผ่านการจำลองแบบทางคณิตศาสตร์ โดยใช้เครื่อง **LANTA** ในการประมวลผล

### ขั้นตอนการติดตั้งและการใช้งาน

1. **เข้าสู่ระบบ LANTA**:
   - ก่อนอื่นให้เข้าสู่ระบบของเครื่อง LANTA ให้เรียบร้อย

2. **สร้างโฟลเดอร์สำหรับเก็บไฟล์**:
   ```bash
   mkdir ~/love_prediction
3. **สร้าง python environment เพื่อรองรับการทำงาน**:
   ```bash
   module load Mamba/23.11.0-0
   ```
    ```bash
   python3 -m venv ~/love_prediction/love-montecarlo-env
   ```
    ติดตั้ง Libralies ที่จำเป็น
   ```bash
   pip install numpy scipy matplotlib
   ```
5. **เรียกใช้งาน Python Environment ที่เราสร้างขึ้น***:
   ```bash
   source ~/love_prediction/love-montecarlo-env/bin/activate (ตัวอย่าง Path เรียก)
   ```
7. **นำโค้ด love_simulation.py ไปเขียนในโฟลเดอร์**:
8. **สร้าง SLURM scipt สำหรับส่งงานไปรัน จาก submit_love_prediction.sh**:
9. **ส่งงานไปรัน**:
    ```bash
    sbatch submit_love_prediction.sh
    ```
    เช็คสถานะ
   ```bash
   myqueue
   ```
   
