# 📦 Market Backend API

## Deskripsi

Ini adalah API untuk Market Backend yang mencakup berbagai fitur seperti pengelolaan produk, transaksi, dan pengguna. API ini dibuat dengan Flask dan menggunakan SQLAlchemy untuk ORM.

## 🛠️ Instalasi

1. Clone Repository

```bash
git clone https://github.com/andikazulprisa/market-backend.git
cd market-backend
```

2. Install Dependensi

- Pastikan kamu sudah menginstal Python 3.7+ dan virtualenv. Jika belum:

```bash
pip install virtualenv
```

- Buat environment dan aktifkan:

```bash
# macOS/Linux
virtualenv venv
source venv/bin/activate

# Windows
virtualenv venv
venv\Scripts\activate
```

- Install semua dependensi:

```bash
pip install -r requirements.txt
```

3. Setup Database

- Pastikan SQLite sudah terpasang (atau sesuaikan config database di .env). Jalankan perintah migrasi:

```bash
flask db init
flask db migrate
flask db upgrade
```

4. Menjalankan Aplikasi

```bash
flask run
```

- Aplikasi akan berjalan di: http://127.0.0.1:5000

## Fitur

- User Management: Register, login, update, delete user.

- Product Management: Create, read (all & by id), update, delete products.

- Transaction Management: (Jika sudah selesai implementasi)

## 🧱 ERD (Entity Relationship Diagram)

Di bawah ini adalah diagram relasi antara entitas yang ada pada aplikasi ini:

![ERD](assets/erd.png)

- Users: Menyimpan data pengguna seperti `name`, `email`, dan `password`.
- Products: Menyimpan data produk seperti `name`, `description`, `price`, dan `stock`.
- Transactions: Menyimpan data transaksi yang terjadi antara pengguna dan produk.

## 🗃️ Database Schema

Struktur database terdiri dari 3 tabel utama: `users`, `products`, dan `transactions`.

### SQL Schema

File schema ada di `app/migrations/schema.sql`.

```sql
-- contoh isi file schema.sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    ...
);
```

## 🔗 API Endpoints

Dokumentasi lengkap dan uji coba endpoint tersedia di: 👉
[Postman Collection Link](https://.postman.co/workspace/My-Workspace~ffdbc94a-c6f9-407c-85d4-3894c4baac29/collection/43110416-9206d3ba-5c64-4c20-a350-c2609632fd03?action=share&creator=43110416)

1. 🧑 User Routes

- ✅ POST /register
  - Mendaftarkan pengguna baru.

```json
{
  "name": "User Name",
  "email": "user@example.com",
  "password": "password123"
}
```

Response:

```json
{
  "message": "User berhasil didaftarkan"
}
```

- 🔐 POST /login
  - Login pengguna untuk mendapatkan JWT token.

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

Response:

```
{
  "token": "jwt_token_here"
}
```

🔍 GET /users

- Mendapatkan semua pengguna.

🔍 GET /users/{user_id}

- Mendapatkan pengguna berdasarkan ID.

✏️ PUT /users/{user_id}

- Update data pengguna berdasarkan ID.

❌ DELETE /users/{user_id}

- Menghapus pengguna berdasarkan ID.

2. 📦 Product Routes

- ✅ POST /products

Menambahkan produk baru.

```
{
  "name": "Product Name",
  "description": "Product Description",
  "price": 100.0,
  "stock": 10
}
```

Response:

```
{
  "message": "Produk berhasil ditambahkan"
}
```

🔍 GET /products

Mendapatkan semua produk.

Response:

```
[
  {
    "id": 1,
    "name": "Product Name",
    "description": "Product Description",
    "price": 100.0,
    "stock": 10
  },
]
```

🔍 GET /products/{product_id}

- Mendapatkan produk berdasarkan ID.

Response:

```
{
  "id": 1,
  "name": "Product Name",
  "description": "Product Description",
  "price": 100.0,
  "stock": 10
}
```

✏️ PUT /products/{product_id}

- Mengupdate produk berdasarkan ID.

❌ DELETE /products/{product_id}

- Menghapus produk berdasarkan ID.

3. 💸 Transaction Routes

- ✅ POST /transactions

Membuat transaksi baru.

```
{
  "user_id": 1,
  "product_id": 1,
  "quantity": 2
}
```

Response:

```
{
  "message": "Transaksi berhasil"
}
```

📬 Penggunaan di Postman

Gunakan token JWT pada header Authorization:

```
Authorization: Bearer <token>
```

Buat collection Postman dan import endpoint di atas untuk mencoba semua fitur API dengan mudah.

🧪 Debugging & Log

Jika terjadi error, periksa terminal Flask:

```
# Contoh log
127.0.0.1 - - [DATE] "METHOD /endpoint HTTP/1.1" STATUS_CODE -
```

---

# ✍️ Author

Andika Zulprisa Adha

Individual Test Brief

- Generate by AI (Chat GPT)
