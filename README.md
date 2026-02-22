# จัดทำโดย
ชื่อ: นายพลกฤต บัวลอย  
รหัสนักศึกษา: 6810110223

---

## โครงสร้างโปรเจกต์
```
code/
  ├── threading_example.py
  ├── asyncio_example.py
  ├── process_pool_example.py
  └── README.md
```

---

## วิธีรัน
```bash
python threading_example.py
python asyncio_example.py
python process_pool_example.py
```

---

## Threading (`threading_example.py`)
### จำลองร้านอาหาร 5 โต๊ะ สั่งอาหารพร้อมกัน แต่ละโต๊ะต้องรอครัวทำอาหาร
### การทำงาน
- แต่ละโต๊ะ = 1 Thread
- ทุก Thread เริ่มพร้อมกันด้วย `thread.start()`
- รอให้ครบทุกโต๊ะด้วย `thread.join()`

### ผลลัพธ์
```
Restaurant is open! 5 tables ordering food simultaneously.
Table 1 ordered [Fried Rice] — Wait 1.3 Seconds
Table 2 ordered [Noodle] — Wait 2.1 Seconds
...
[SUCCESS] Table 1 received [Fried Rice]!
...
All tables have been served! Total time taken: 2.31 seconds.
```

### ทำไมถึงเร็วขึ้น
ถ้าทำทีละโต๊ะจะใช้เวลารวมกัน ~8 วินาที  
แต่ Threading ทำพร้อมกัน ใช้เวลาแค่โต๊ะที่นานที่สุด ~2 วินาที

---

## Asyncio (`asyncio_example.py`)
### ดึงข้อมูล Number Trivia ของตัวเลข 6 ตัวพร้อมกัน โดยจำลอง network delay
### การทำงาน
- แต่ละตัวเลข = 1 Coroutine
- `await asyncio.sleep()` จำลองการรอ network — ระหว่างรอ Event Loop ไปทำตัวอื่นก่อน
- `asyncio.gather()` เริ่มทุก Coroutine พร้อมกัน

### ผลลัพธ์
```
Pulling number    1 ... (wait 0.8s)
Pulling number    2 ... (wait 1.5s)
...
Complete in 1.97 seconds

[1] 1 is not a prime number
[2] 2 is the only even prime number
...
```

### ความแตกต่างจาก Threading
| | Threading | Asyncio |
|---|---|---|
| การสลับงาน | OS จัดการ | โปรแกรมจัดการเอง (สลับตรง `await`) |
| Overhead | มี context switch | แทบไม่มี |
| เหมาะกับ | I/O-bound ทั่วไป | I/O-bound ที่ต้องการ concurrent สูง |

---

## Multiprocessing Pool (`process_pool_example.py`)
### ค้นหาจำนวนเฉพาะตั้งแต่ 2 ถึง 500,000 โดยใช้หลาย CPU cores
### การทำงาน
- แบ่งช่วงตัวเลขออกเป็น chunks ตามจำนวน CPU
- `Pool.map()` กระจาย chunks ไปยังแต่ละ process
- แต่ละ process ทำงานบน CPU core ของตัวเองจริงๆ

### ผลลัพธ์
```
Find the prime numbers in range 2 to 500,000
CPU have: 4 cores

Single:             found 41,538 in 2.84s
Multiprocessing Pool: found 41,538 in 0.92s

Speedup: 3.1x
Results match: True
```

### ทำไมต้องใช้ Multiprocessing ไม่ใช่ Threading
Python มี GIL ทำให้ Threading รันได้ทีละ thread  
สำหรับงานคำนวณหนัก (CPU-bound) จะไม่เร็วขึ้น  
Multiprocessing สร้าง process แยกกัน แต่ละอันมี GIL ของตัวเอง ทำให้รันพร้อมกันได้

---

## สรุป

```
ถ้างานต้องรอเยอะ 
├── Asyncio
└── Threading
ถ้าต้องการคำนวณหนัก
└── Multiprocessing
```
