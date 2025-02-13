import numpy as np
import matplotlib.pyplot as plt

def simulate_love(num_simulations=100000):
    success_count = 0
    results = []

    for _ in range(num_simulations):
        # ความน่าจะเป็นของปัจจัยต่าง ๆ ในความรัก (สมมุติ)
        chance_meeting = np.random.rand() < 0.7  # โอกาสได้เจอคนที่ถูกใจ 70%
        mutual_interest = np.random.rand() < 0.5  # โอกาสที่ชอบกันทั้งคู่ 50%
        timing_right = np.random.rand() < 0.6  # โอกาสที่จังหวะชีวิตลงตัว 60%

        # ถ้าทั้ง 3 เงื่อนไขเป็นจริง = ความรักสำเร็จ
        success = chance_meeting and mutual_interest and timing_right
        results.append(success)
        if success:
            success_count += 1

    prob_love = success_count / num_simulations
    return prob_love, results

# รันการจำลอง 100,000 ครั้ง
num_simulations = 100000
prob_love, results = simulate_love(num_simulations)

# แสดงผลลัพธ์
print(f"💖 โอกาสพบรักแท้จากการจำลอง Monte Carlo: {prob_love*100:.2f}%")

# แปลงข้อมูลเป็น int (0 = False, 1 = True)
results = [int(result) for result in results]

# สร้าง histogram
plt.hist(results, bins=2, edgecolor='black', alpha=0.7)
plt.title("โอกาสพบรักแท้")
plt.xlabel("ผลการจำลอง")
plt.ylabel("ความถี่")

# บันทึกกราฟเป็นไฟล์ .jpg
plt.savefig("love_simulation_result.jpg", format='jpg')

# ปิดการแสดงผลกราฟในโหมด interactive
plt.close()
