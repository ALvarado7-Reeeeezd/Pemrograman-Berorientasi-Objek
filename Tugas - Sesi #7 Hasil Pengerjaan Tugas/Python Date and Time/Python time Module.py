import time


def demo_time_and_ctime():
    print("=== 1. time.time() & time.ctime() ===")
    # 1. time.time() - Mengambil detik sejak epoch (1 Jan 1970 UTC)
    seconds = time.time()
    print("Seconds since epoch =", seconds)

    # 2. time.ctime() - Mengonversi detik epoch ke string waktu lokal
    sample_seconds = 1672215379.5045543
    local_time = time.ctime(sample_seconds)
    print("Local time (from ctime) =", local_time)
    print()


def demo_sleep():
    print("=== 2. time.sleep() ===")
    print("Printed immediately.")
    # Menunda eksekusi thread selama 2.4 detik
    time.sleep(2.4)
    print("Printed after 2.4 seconds.")
    print()


def demo_localtime_and_gmtime():
    print("=== 3. time.localtime() & time.gmtime() ===")
    sample_seconds = 1672214933

    # 1. time.localtime() - Mengembalikan struct_time dalam waktu lokal
    local_res = time.localtime(sample_seconds)
    print("localtime result :", local_res)
    print(f"year: {local_res.tm_year}, tm_hour: {local_res.tm_hour}")

    # 2. time.gmtime() - Mengembalikan struct_time dalam UTC
    utc_res = time.gmtime(sample_seconds)
    print("gmtime result    :", utc_res)
    print(f"year: {utc_res.tm_year}, tm_hour: {utc_res.tm_hour}")

    # Jika dipanggil tanpa argumen, menggunakan nilai time.time() saat ini
    current_local = time.localtime()
    print("Current local hour:", current_local.tm_hour)
    print()


def demo_mktime_and_asctime():
    print("=== 4. time.mktime() & time.asctime() ===")
    # Format tuple 9 elemen: (year, month, day, hour, minute, second, weekday, day_of_year, daylight_saving)
    # Catatan: 28 Des 2022 adalah hari Rabu (weekday = 2)
    time_tuple = (2022, 12, 28, 8, 44, 4, 2, 362, 0)

    # 1. time.mktime() - Mengonversi struct_time / tuple ke detik epoch lokal
    seconds = time.mktime(time_tuple)
    print("Seconds from mktime =", seconds)

    # 2. time.asctime() - Mengonversi struct_time / tuple ke string readable
    asc_result = time.asctime(time_tuple)
    print("Result from asctime  =", asc_result)
    print()


def demo_strftime_and_strptime():
    print("=== 5. time.strftime() & time.strptime() ===")
    # 1. time.strftime() - Formatting struct_time menjadi string
    named_tuple = time.localtime()
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    print("Formatted time string (strftime) =", time_string)

    # 2. time.strptime() - Parsing string waktu menjadi struct_time
    input_str = "14 July, 2023"
    parsed_struct = time.strptime(input_str, "%d %B, %Y")
    print("Parsed struct_time (strptime)   =", parsed_struct)
    print(f"Parsed year: {parsed_struct.tm_year}, month: {parsed_struct.tm_mon}, day: {parsed_struct.tm_mday}")
    print()


if __name__ == "__main__":
    # Eksekusi seluruh demonstrasi fungsi secara berurutan
    demo_time_and_ctime()
    demo_sleep()
    demo_localtime_and_gmtime()
    demo_mktime_and_asctime()
    demo_strftime_and_strptime()