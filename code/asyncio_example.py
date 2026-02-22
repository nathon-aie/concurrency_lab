"""
Number Trivia Fetcher
จำลองการดึงข้อมูลสนุกๆ เกี่ยวกับตัวเลข โดยไม่ต้องรอทีละตัว ดึงพร้อมกันทุกตัวเลข
ใช้ asyncio.sleep แทน HTTP จริง เพื่อให้รันได้โดยไม่ต้องติดตั้ง library เพิ่ม
"""

import asyncio
import random
import time

TRIVIA_DB = {
    1: "1 is not a prime number",
    2: "2 is the only even prime number",
    3: "3 is the smallest odd prime number",
    7: "7 is the smallest number that cannot be represented as the sum of three squares",
    42: "42 is the answer to life, the universe, and everything in Douglas Adams 'The Hitchhiker's Guide to the Galaxy'",
    404: "404 is a common HTTP error code indicating a page not found",
}


async def pulling(number: int) -> str:
    delay = random.uniform(0.5, 2.0)
    print(f"Pulling number {number:4} ... (wait {delay:.1f}s)")
    await asyncio.sleep(delay)  # จำลอง network
    return TRIVIA_DB.get(number, f"{number} NO DATA")


async def main():
    numbers = [1, 2, 3, 7, 42, 404]
    start = time.time()
    # เริ่มดึงทุกตัวพร้อมกัน
    results = await asyncio.gather(
        pulling(1),
        pulling(2),
        pulling(3),
        pulling(7),
        pulling(42),
        pulling(404),
    )
    print(f"\nComplete in {time.time() - start:.2f} seconds\n")
    for number, trivia in zip(numbers, results):
        print(f"[{number}] {trivia}")


asyncio.run(main())
