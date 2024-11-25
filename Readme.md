# ParMusic API Documentation

## Daftar Isi
- [Gambaran Umum](#gambaran-umum)
- [URL Dasar](#url-dasar)
- [Autentikasi](#autentikasi)
- [Endpoint yang Tersedia](#endpoint-yang-tersedia)
- [Penggunaan API Key](#penggunaan-api-key)
- [Panduan Pengujian](#panduan-pengujian)
- [Informasi Deployment](#informasi-deployment)
- [Penanganan Error](#penanganan-error)
- [Status API](#status-api)

## Gambaran Umum
ParMusic API menyediakan layanan akses ke fitur rekomendasi alat musik melalui antarmuka pemrograman aplikasi (API). API ini terbagi menjadi dua jenis endpoint: publik dan terproteksi, di mana endpoint terproteksi memerlukan autentikasi menggunakan API key.

## URL Dasar
```
https://simple-api-deployment-one.vercel.app
```

## Autentikasi
Endpoint terproteksi memerlukan API key yang harus disertakan dalam header permintaan.

**Nama Header:** `J-API-Key`  
**Format:** Sertakan API key dalam header permintaan
```
J-API-Key: e54d4431-5dab-474e-b71a-0db1fcb9e659
```

### Kode Response Autentikasi
- `200 OK`: Autentikasi berhasil
- `401 Unauthorized`: API key tidak ada atau tidak valid

## Endpoint yang Tersedia

### 1. Endpoint Root
```
GET https://simple-api-deployment-one.vercel.app/
```
Mengembalikan informasi dasar tentang ParMusic API.

#### Contoh Response
```json
{
    "message": "This is Simple API Deployment for ParMusic with Authentication by Josia 1822075"
}
```

### 2. Route Publik

#### Mengakses Route Publik
```
GET https://simple-api-deployment-one.vercel.app/api/v1/public/
```
Mengakses route publik yang tidak memerlukan autentikasi.

##### Contoh Response
```
"Public Route for ParMusic"
```

### 3. Route Terproteksi

#### Mendapatkan Informasi Pengguna
```
GET https://simple-api-deployment-one.vercel.app/api/v1/secure/
```
Mengembalikan informasi tentang pengguna yang terautentikasi.

##### Headers yang Diperlukan
```
J-API-Key: e54d4431-5dab-474e-b71a-0db1fcb9e659
```

##### Contoh Response Sukses
```json
{
    "name": "ParMusic",
    "message": "Semoga TST dapat A. A for Aminn"
}
```

##### Contoh Response Error (API Key Invalid)
```json
{
    "detail": "Missing or invalid API key"
}
```

## Penggunaan API Key
API menggunakan set API key yang telah ditentukan sebelumnya. Berikut adalah API key yang tersedia untuk pengujian:

```
API Key: e54d4431-5dab-474e-b71a-0db1fcb9e659
```

## Panduan Pengujian

### Menggunakan cURL

1. Uji Endpoint Root:
```bash
curl https://simple-api-deployment-one.vercel.app/
```

2. Uji Route Publik:
```bash
curl https://simple-api-deployment-one.vercel.app/api/v1/public/
```

3. Uji Route Terproteksi:
```bash
curl -H "J-API-Key: e54d4431-5dab-474e-b71a-0db1fcb9e659" https://simple-api-deployment-one.vercel.app/api/v1/secure/
```

### Menggunakan Python Requests

```python
import requests

# URL Dasar API
base_url = "https://simple-api-deployment-one.vercel.app"

# Headers untuk request terautentikasi
headers = {
    "J-API-Key": "e54d4431-5dab-474e-b71a-0db1fcb9e659"
}

# Uji endpoint root
response = requests.get(base_url)
print(response.json())

# Uji route publik
response = requests.get(f"{base_url}/api/v1/public/")
print(response.text)

# Uji route terproteksi
response = requests.get(f"{base_url}/api/v1/secure/", headers=headers)
print(response.json())
```

### Menggunakan JavaScript Fetch

```javascript
// URL Dasar API
const baseUrl = "https://simple-api-deployment-one.vercel.app";

// Headers untuk request terautentikasi
const headers = {
    "J-API-Key": "e54d4431-5dab-474e-b71a-0db1fcb9e659"
};

// Uji endpoint root
fetch(baseUrl)
    .then(response => response.json())
    .then(data => console.log(data));

// Uji route publik
fetch(`${baseUrl}/api/v1/public/`)
    .then(response => response.text())
    .then(data => console.log(data));

// Uji route terproteksi
fetch(`${baseUrl}/api/v1/secure/`, { headers })
    .then(response => response.json())
    .then(data => console.log(data));
```

## Informasi Deployment
- Platform: Vercel
- URL Produksi: https://simple-api-deployment-one.vercel.app
- Tipe Deployment: Serverless
- Auto-scaling: Dikelola oleh Vercel
- SSL: Aktif secara default


## Penanganan Error
API menggunakan kode status HTTP standar:
- 200: Sukses
- 401: Unauthorized (API key invalid atau tidak ada)
- 404: Tidak Ditemukan
- 500: Error Server Internal

## Status API
Anda dapat memeriksa status API dengan mengakses endpoint root:
```
GET https://simple-api-deployment-one.vercel.app/
```
