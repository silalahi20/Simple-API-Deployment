import secrets

# Buat API key aman dengan panjang 32 karakter
api_key = secrets.token_urlsafe(32)
print(f"API key Anda:{api_key}")
