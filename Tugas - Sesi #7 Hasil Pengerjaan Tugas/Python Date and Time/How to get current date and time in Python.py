from datetime import date, datetime


def demo_get_todays_date():
    print("=== 1. Get Today's Date ===")
    # Menggunakan date class untuk mengambil tanggal lokal saat ini
    today = date.today()
    print("Today's date:", today)
    print()


def demo_date_formatting():
    print("=== 2. Current Date in Different Formats ===")
    today = date.today()

    # Format dd/mm/YYYY (contoh: 27/12/2022)
    d1 = today.strftime("%d/%m/%Y")
    print("d1 =", d1)

    # Format Textual month, day and year (contoh: December 27, 2022)
    d2 = today.strftime("%B %d, %Y")
    print("d2 =", d2)

    # Format mm/dd/yy (contoh: 12/27/22)
    d3 = today.strftime("%m/%d/%y")
    print("d3 =", d3)

    # Format Month abbreviation, day and year (contoh: Dec-27-2022)
    d4 = today.strftime("%b-%d-%Y")
    print("d4 =", d4)
    print()


def demo_get_current_datetime():
    print("=== 3. Get Current Date and Time ===")
    # Menggunakan datetime class untuk mengambil tanggal sekaligus waktu saat ini
    now = datetime.now()
    print("now =", now)

    # Format dd/mm/YYYY H:M:S (contoh: 27/12/2022 10:09:20)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    print()


if __name__ == "__main__":
    # Eksekusi seluruh fungsi demonstrasi secara berurutan
    demo_get_todays_date()
    demo_date_formatting()
    demo_get_current_datetime()