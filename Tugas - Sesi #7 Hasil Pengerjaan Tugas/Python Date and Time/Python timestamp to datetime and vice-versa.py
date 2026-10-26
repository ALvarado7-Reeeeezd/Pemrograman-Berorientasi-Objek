from datetime import datetime


def demo_timestamp_to_datetime():
    print("=== 1. Python Timestamp to Datetime Object ===")
    # UNIX timestamp (jumlah detik sejak 1 Januari 1970 UTC)
    timestamp = 1545730073

    # Mengubah timestamp ke datetime object dalam zona waktu lokal
    dt_object = datetime.fromtimestamp(timestamp)

    # Cetak hasil dan tipe datanya
    print("dt_object =", dt_object)
    print("type(dt_object) =", type(dt_object))
    print()


def demo_datetime_to_timestamp():
    print("=== 2. Python Datetime Object to Timestamp ===")
    # Ambil tanggal dan waktu lokal saat ini
    now = datetime.now()

    # Mengubah dari datetime object ke UNIX timestamp
    ts = datetime.timestamp(now)

    print("Current datetime =", now)
    print("Timestamp =", ts)
    print("type(ts) =", type(ts))
    print()


def demo_timestamp_to_formatted_string():
    print("=== 3. Timestamp -> Datetime Object -> Formatted String ===")
    timestamp = 1545730073
    dt_object = datetime.fromtimestamp(timestamp)

    # Mengubah datetime object hasil konversi menjadi string yang rapi
    formatted_str = dt_object.strftime("%d %B %Y, %H:%M:%S")
    print("Formatted String =", formatted_str)
    print()


if __name__ == "__main__":
    # Eksekusi seluruh fungsi demonstrasi secara berurutan
    demo_timestamp_to_datetime()
    demo_datetime_to_timestamp()
    demo_timestamp_to_formatted_string()