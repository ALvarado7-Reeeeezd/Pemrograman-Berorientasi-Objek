import time
from datetime import datetime


def demo_current_time_datetime():
    print("=== 1. Current Time Using datetime Module ===")
    # Mengambil datetime object saat ini
    now = datetime.now()

    # Memformat jam, menit, dan detik menjadi string
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    print()


def demo_current_time_time_module():
    print("=== 2. Current Time Using time Module ===")
    # Mengambil waktu lokal sebagai struct_time
    t = time.localtime()

    # Memformat waktu menggunakan time.strftime
    current_time = time.strftime("%H:%M:%S", t)
    print("Current Time =", current_time)
    print()


def demo_current_time_timezone():
    print("=== 3. Current Time of a Certain Timezone (pytz) ===")
    try:
        import pytz

        # Timezone New York
        tz_NY = pytz.timezone('America/New_York')
        datetime_NY = datetime.now(tz_NY)
        print("NY time:", datetime_NY.strftime("%H:%M:%S"))

        # Timezone London
        tz_London = pytz.timezone('Europe/London')
        datetime_London = datetime.now(tz_London)
        print("London time:", datetime_London.strftime("%H:%M:%S"))

    except ImportError:
        print("[Note] Modul 'pytz' belum di-install. Jalankan 'pip install pytz' di terminal kalau mau pakai fitur timezone.")
    print()


if __name__ == "__main__":
    # Eksekusi seluruh demonstrasi secara berurutan
    demo_current_time_datetime()
    demo_current_time_time_module()
    demo_current_time_timezone()