#!/bin/bash
#SBATCH -p compute
#SBATCH -N 1
#SBATCH --ntasks=32
#SBATCH -t 01:00:00
#SBATCH -J love_prediction
#SBATCH -A ltxxxxxx (โปรเจคที่เรียกใช้)

# Load modules
module load Mamba/23.11.0-0

# เปิดใช้งาน virtual environment
source ~/love_prediction/love-montecarlo-env/bin/activate (แก้ตามที่อยู่ที่เราสร้าง python environment)

# รัน Python script
python3 love_simulation.py
