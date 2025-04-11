# PDP School API LMS

Bu FastAPI asosidagi API, maktab uchun ta'lim boshqaruv tizimi (LMS). Bu API, maktablar va o'quvchilarni boshqarish uchun nuqta nuqtalarini taqdim etadi, shu jumladan yangi yozuvlar yaratish va ismga asoslangan ma'lumotlarni olish.

## Xususiyatlar

# 🏫 PDP School API LMS

Bu loyiha FastAPI asosida yozilgan oddiy Learning Management System (LMS) API hisoblanadi. U maktablar va talabalar haqidagi ma'lumotlar bilan ishlashga mo'ljallangan.

## ⚙️ Texnologiyalar

- Python 3.10+
- FastAPI
- Uvicorn (dev server)



<img width="1697" alt="Screenshot 2025-04-11 at 10 01 15" src="https://github.com/user-attachments/assets/348a7991-4273-4f71-888d-fe1604c7fec4" />


## 📦 O'rnatish

Ushbu loyihani lokalda ishga tushirish uchun:

1. Repozitoriyani klonlash:
   ```bash
   git clone [https://github.com/abdusamadovv28/dae.git]
   cd school-api
   ```
2. Virtual muhit yaratish:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows uchun: `venv\Scripts\activate`
   ```
3. Bog'liqliklarni o'rnatish:
   ```bash
   pip install -r requirements.txt
   ```
4. Ilovani ishga tushirish:
   ```bash
   uvicorn main:app --reload
   ```
📚 API Endpoints
```bash
   GET /api/school – Barcha maktablar
   
   GET /api/school/{school_name} – Muayyan nomdagi maktab
   
   POST /api/school – Yangi maktab qo‘shish
   
   GET /api/student – Barcha talabalar
   
   GET /api/student/{student_name} – Muayyan nomdagi talaba
   
   POST /api/student – Yangi talaba qo‘shish
```

### Misol

Barcha o'quvchilarni olish uchun:
   ```bash
   GET http://127.0.0.1:8000/api/student
   ```
   Yangi o'quvchi yaratish:
   ```bash
   POST http://127.0.0.1:8000/api/student
   Content-Type: application/json

   {
     "name": "John Doe",
     "email": "john.doe@example.com",
     "room_id": 101,
     "since": "2022-01-01"
   }
   ```
## Litsenziya

Ushbu loyiha MIT litsenziyasi ostida litsenziyalanadi - tafsilotlar uchun LICENSE faylini ko'rib chiqing.
Bu `README.md` fayli sizning GitHub'dagi loyihangizni boshqalar uchun tushunarli qilishga yordam beradi.
