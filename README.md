# Proyek Manajemen

Proyek ini adalah aplikasi manajemen berbasis Django.

## Persyaratan

- Python 3.8+
- Django 3.2+
- Dependensi lainnya (lihat `requirements.txt`)

## Instalasi

1. Clone repositori ini:
   ```
   git clone https://github.com/username/nama-proyek.git
   cd nama-proyek
   ```

2. Buat dan aktifkan virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # Untuk Unix atau MacOS
   venv\Scripts\activate  # Untuk Windows
   ```

3. Instal dependensi:
   ```
   pip install -r requirements.txt
   ```

4. Lakukan migrasi database:
   ```
   python manage.py migrate
   ```

5. Buat superuser:
   ```
   python manage.py createsuperuser
   ```

6. Jalankan server pengembangan:
   ```
   python manage.py runserver
   ```

7. Buka browser dan akses `http://localhost:8000`


