import time


def demo_basic_sleep():
    print("=== 1. Basic sleep() Demo (2 Seconds) ===")
    print("Menunggu selama 2 detik...")
    # Menghentikan eksekusi program selama 2 detik
    time.sleep(2)
    print("Wait until 2 seconds.\n")


def demo_float_sleep():
    print("=== 2. Float Parameter sleep() Demo ===")
    print("Printed immediately.")
    # sleep() menerima nilai desimal (float)
    time.sleep(2.4)
    print("Printed after 2.4 seconds.\n")


def demo_digital_clock(max_ticks=5):
    print(f"=== 3. Digital Clock Demo (Running for {max_ticks} ticks) ===")
    print("Format waktu: 12-hour clock (hh:mm:ss AM/PM)")
    print("Tekan Ctrl+C untuk menghentikan program jika berjalan tanpa batas.\n")

    tick = 0
    try:
        # Loop untuk mensimulasikan pergerakan jam digital
        while tick < max_ticks:
            # Ambil waktu lokal saat ini sebagai struct_time
            current_time = time.localtime()

            # Format waktu ke format 12 jam dengan AM/PM (%I:%M:%S %p)
            formatted_time = time.strftime("%I:%M:%S %p", current_time)

            print(formatted_time, flush=True)

            # Jeda 1 detik sebelum iterasi berikutnya
            time.sleep(1)
            tick += 1
    except KeyboardInterrupt:
        print("\nDigital clock dihentikan oleh pengguna.")

    print()


if __name__ == "__main__":
    # Eksekusi seluruh fungsi demonstrasi secara berurutan
    demo_basic_sleep()
    demo_float_sleep()

    # Dijalankan 5 kali tick sebagai contoh biar gak mengunci terminal selamanya
    demo_digital_clock(max_ticks=5)