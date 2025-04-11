# PDP School API LMS

Bu FastAPI asosidagi API, maktab uchun ta'lim boshqaruv tizimi (LMS). Bu API, maktablar va o'quvchilarni boshqarish uchun nuqta nuqtalarini taqdim etadi, shu jumladan yangi yozuvlar yaratish va ismga asoslangan ma'lumotlarni olish.

## Xususiyatlar

# 🏫 PDP School API LMS

Bu loyiha FastAPI asosida yozilgan oddiy Learning Management System (LMS) API hisoblanadi. U maktablar va talabalar haqidagi ma'lumotlar bilan ishlashga mo'ljallangan.

## ⚙️ Texnologiyalar

- Python 3.10+
- FastAPI
- Uvicorn (dev server)

## 📦 O'rnatish

1. Repository'ni clone qiling:

```bash
git clone [https://github.com/your-username/pdp-school-api.git](https://github.com/abdusamadovv28/dae.git)
cd pdp-school-api


<img width="1697" alt="Screenshot 2025-04-11 at 10 01 15" src="https://github.com/user-attachments/assets/348a7991-4273-4f71-888d-fe1604c7fec4" />


## O'rnatish

Ushbu loyihani lokalda ishga tushirish uchun:

1. Repozitoriyani klonlash:
   ```bash
   git clone https://github.com/PDPSchoolTeam/FastApi-model.git
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
## API Endpoints

### Maktablar
   ```bash
   GET /api/school: Barcha maktablarni olish.
   POST /api/school: Yangi maktab yaratish.
   GET /api/school/{school_name}: Maktabni nomi bo'yicha olish.
   ```
### O'quvchilar
   ```bash
   GET /api/student: Barcha o'quvchilarni olish.
   POST /api/student: Yangi o'quvchi yaratish.
   GET /api/student/{student_name}: O'quvchini nomi bo'yicha olish.
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
