"""
Prime Number Finder
ค้นหาจำนวนเฉพาะในช่วงตัวเลขขนาดใหญ่
งานนี้ CPU-bound ล้วนๆ — ต้องใช้ multiple CPU cores
จึงได้ประโยชน์จาก multiprocessing (ไม่ใช่ threading)
"""

import multiprocessing
import time
import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def find_prime_number(args: tuple) -> list[int]:
    start, end = args
    return [n for n in range(start, end) if is_prime(n)]


def divide_work(start: int, end: int, num_workers: int) -> list[tuple]:
    size = (end - start) // num_workers
    return [
        (start + i * size, start + (i + 1) * size if i < num_workers - 1 else end)
        for i in range(num_workers)
    ]


def main():
    START, END = 2, 500_000
    NUM_WORKERS = min(multiprocessing.cpu_count(), 4)
    print(f"Find the prime numbers in range {START:,} to {END:,}")
    print(f"CPU have: {multiprocessing.cpu_count()} cores\n")

    # --- Single Process ---
    t0 = time.time()
    single_result = [n for n in range(START, END) if is_prime(n)]
    single_time = time.time() - t0
    print(f"Single:  found {len(single_result):,} in {single_time:.2f}s")

    # --- Multiprocessing Pool ---
    chunks = divide_work(START, END, NUM_WORKERS)
    t0 = time.time()
    with multiprocessing.Pool(processes=NUM_WORKERS) as pool:
        results = pool.map(find_prime_number, chunks)
    pool_result = sorted(n for chunk in results for n in chunk)
    pool_time = time.time() - t0
    print(f"Multiprocessing Pool:  found {len(pool_result):,} in {pool_time:.2f}s")

    print(f"\nSpeedup: {single_time / pool_time:.1f}x")
    print(f"Results match: {single_result == pool_result}")


if __name__ == "__main__":
    main()
