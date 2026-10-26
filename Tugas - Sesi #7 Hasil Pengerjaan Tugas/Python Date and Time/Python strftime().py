from datetime import datetime


def demo_basic_strftime():
    print("=== 1. Basic Datetime to String (Example 1) ===")
    # Get current date and time
    now = datetime.now()

    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time_str = now.strftime("%H:%M:%S")
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    print("year:", year)
    print("month:", month)
    print("day:", day)
    print("time:", time_str)
    print("date and time:", date_time)
    print()


def demo_timestamp_formatting():
    print("=== 2. Creating String from Timestamp (Example 2) ===")
    timestamp = 1528797322
    date_time = datetime.fromtimestamp(timestamp)

    print("Date time object:", date_time)
    print("Output 2 (%m/%d/%Y, %H:%M:%S):", date_time.strftime("%m/%d/%Y, %H:%M:%S"))
    print("Output 3 (%d %b, %Y)         :", date_time.strftime("%d %b, %Y"))
    print("Output 4 (%d %B, %Y)         :", date_time.strftime("%d %B, %Y"))
    print("Output 5 (%I%p)              :", date_time.strftime("%I%p"))
    print()


def demo_locale_formatting():
    print("=== 3. Locale Appropriate Formats (Example 3) ===")
    timestamp = 1528797322
    date_time = datetime.fromtimestamp(timestamp)

    print("Output 1 (%c - Locale date and time):", date_time.strftime("%c"))
    print("Output 2 (%x - Locale date)         :", date_time.strftime("%x"))
    print("Output 3 (%X - Locale time)         :", date_time.strftime("%X"))
    print()


def demo_all_format_directives():
    print("=== 4. Full Directives Reference Demo ===")
    now = datetime.now()

    directives = [
        ("%a", "Abbreviated weekday name"),
        ("%A", "Full weekday name"),
        ("%w", "Weekday as decimal (0=Sunday)"),
        ("%d", "Day of month (zero-padded)"),
        ("%b", "Abbreviated month name"),
        ("%B", "Full month name"),
        ("%m", "Month (zero-padded)"),
        ("%y", "Year without century (00-99)"),
        ("%Y", "Year with century"),
        ("%H", "Hour (24-hour clock, zero-padded)"),
        ("%I", "Hour (12-hour clock, zero-padded)"),
        ("%p", "Locale's AM/PM"),
        ("%M", "Minute (zero-padded)"),
        ("%S", "Second (zero-padded)"),
        ("%f", "Microsecond (zero-padded)"),
        ("%j", "Day of the year (001-366)"),
        ("%U", "Week number of year (Sunday first day)"),
        ("%W", "Week number of year (Monday first day)"),
        ("%%", "A literal '%' character"),
    ]

    for code, desc in directives:
        formatted_val = now.strftime(code)
        print(f"{code:<5} | {desc:<42} | Output: {formatted_val}")

    # Platform-dependent non-padded directives (Unix/Linux/macOS)
    print("\n--- Non-padded directives (Platform Dependent) ---")
    try:
        print("%-d (Day without padding)   :", now.strftime("%-d"))
        print("%-m (Month without padding) :", now.strftime("%-m"))
        print("%-H (Hour 24h no padding)   :", now.strftime("%-H"))
    except ValueError:
        print("[Note] Format `%-d` dan kawan-kawan spesifik untuk sistem berbasis Unix/Linux/macOS.")
    print()


if __name__ == "__main__":
    # Execute all demonstration functions sequentially
    demo_basic_strftime()
    demo_timestamp_formatting()
    demo_locale_formatting()
    demo_all_format_directives()