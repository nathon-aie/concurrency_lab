"""
Restaurant Order Simulation
จำลองร้านอาหารที่มีหลายโต๊ะสั่งอาหารพร้อมกัน
แต่ละโต๊ะ = 1 thread ครัวทำอาหารทุกโต๊ะพร้อมกัน
"""

import threading
import time
import random


def cook_order(table_id: int, dish: str, cook_time: float):
    # จำลองการทำอาหาร (I/O-bound: รอครัวทำ)
    print(f"Table {table_id} ordered [{dish}] — Wait {cook_time:.1f} Seconds")
    time.sleep(cook_time)  # จำลองเวลาทำอาหาร
    print(f"[SUCCESS] Table {table_id} received [{dish}]!")


def run_restaurant():
    tables = [
        (1, "Fried Rice"),
        (2, "Noodle"),
        (3, "Pad Kra Pao"),
        (4, "Omelete"),
        (5, "Steak"),
    ]
    print("/" * 58)
    print("Restaurant is open! 5 tables ordering food simultaneously.")
    print("\\" * 58)
    start = time.time()
    # สร้าง thread สำหรับแต่ละโต๊ะ
    threads = []
    for table_id, dish in tables:
        cook_time = random.uniform(1.0, 2.5)
        t = threading.Thread(
            target=cook_order,
            args=(table_id, dish, cook_time),
            name=f"Table-{table_id}",
        )
        threads.append(t)
    # เริ่มทุก thread พร้อมกัน
    for t in threads:
        t.start()
    print("+" * 50)
    # รอให้ทุก thread เสร็จ
    for t in threads:
        t.join()
    elapsed = time.time() - start
    print("=" * 60)
    print(f"All tables have been served! Total time taken: {elapsed:.2f} seconds.")
    print("=" * 60)


if __name__ == "__main__":
    run_restaurant()
