# Dokumentasi API ParMusic

Selamat datang di **API ParMusic**! API ini memungkinkan Anda untuk berinteraksi dengan platform ParMusic, yang mencakup autentikasi, endpoint publik, dan akses aman ke data spesifik pengguna.

## URL Dasar

URL dasar untuk API yang sudah dideploy adalah:

```
https://simple-api-deployment-one.vercel.app
```

Anda dapat mengakses dokumentasi API interaktif menggunakan Swagger UI di:

```
https://simple-api-deployment-one.vercel.app/docs
```

## Autentikasi

API ParMusic menggunakan **API Key Authentication** dan **OAuth2 Bearer Tokens** untuk mengamankan endpoint. Berikut adalah ringkasan mekanisme autentikasi:

### API Key Authentication
- Kirimkan API Key di header request menggunakan nama header `J-API-Key`.
- Contoh:
  ```
  J-API-Key: e54d4431-5dab-474e-b71a-0db1fcb9e659
  ```

### OAuth2 Bearer Tokens
- Dapatkan token melalui endpoint `/api/v1/auth/login`.
- Sertakan token dalam header `Authorization`:
  ```
  Authorization: Bearer <token>
  ```

## Endpoint

### 1. Endpoint Publik
Endpoint publik dapat diakses tanpa autentikasi.

#### GET `/api/v1/public/`
- **Deskripsi**: Mengembalikan pesan publik.
- **Respons**:
  ```json
  "Public Route for ParMusic"
  ```

#### GET `/api/v1/public/google-login`
- **Deskripsi**: Memulai proses login menggunakan Google (implementasi sedang dikembangkan).
- **Respons**:
  ```json
  {
    "message": "Login with Google initiated"
  }
  ```

### 2. Endpoint Autentikasi
Endpoint untuk login dan registrasi pengguna.

#### POST `/api/v1/auth/login`
- **Deskripsi**: Login pengguna dan menyediakan token autentikasi.
- **Body Permintaan**:
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Respons**:
  ```json
  {
    "message": "Login successful",
    "user": {
      "name": "string",
      "email": "string",
      "password": "string"
    }
  }
  ```

#### POST `/api/v1/auth/register`
- **Deskripsi**: Registrasi pengguna baru.
- **Body Permintaan**:
  ```json
  {
    "name": "string",
    "email": "string",
    "password": "string"
  }
  ```
- **Respons**:
  ```json
  {
    "message": "User registered successfully",
    "user": {
      "name": "string",
      "email": "string",
      "password": "string"
    }
  }
  ```

### 3. Endpoint Aman
Endpoint ini memerlukan autentikasi yang valid.

#### GET `/api/v1/secure/`
- **Deskripsi**: Mengembalikan detail pengguna yang sudah diautentikasi.
- **Headers**:
  ```
  J-API-Key: <api-key>
  ```
- **Respons**:
  ```json
  {
    "name": "string",
    "message": "string",
    "email": "string",
    "password": "string"
  }
  ```

#### GET `/api/v1/secure/userid`
- **Deskripsi**: Mengembalikan ID pengguna yang sudah diautentikasi.
- **Headers**:
  ```
  J-API-Key: <api-key>
  ```
- **Respons**:
  ```json
  {
    "user_id": "string"
  }
  ```

## Contoh Permintaan

### 1. Login
**Permintaan**:
```http
POST /api/v1/auth/login HTTP/1.1
Host: simple-api-deployment-one.vercel.app
Content-Type: application/json

{
  "email": "parmusic@example.com",
  "password": "securepassword"
}
```
**Respons**:
```json
{
  "message": "Login successful",
  "user": {
    "name": "ParMusic",
    "email": "parmusic@example.com",
    "password": "$2b$12$..."
  }
}
```

### 2. Akses Endpoint Aman
**Permintaan**:
```http
GET /api/v1/secure/userid HTTP/1.1
Host: simple-api-deployment-one.vercel.app
J-API-Key: e54d4431-5dab-474e-b71a-0db1fcb9e659
```
**Respons**:
```json
{
  "user_id": "ParMusic"
}
```

## Kode Error
| Kode Status | Deskripsi                         |
|-------------|-----------------------------------|
| 401         | API key/token tidak valid        |
| 400         | Permintaan tidak valid (contoh: email sudah terdaftar) |
| 500         | Kesalahan server internal        |

## Catatan
- Ini adalah versi awal dari API. Fitur tambahan seperti Google Login sedang dalam pengembangan.

