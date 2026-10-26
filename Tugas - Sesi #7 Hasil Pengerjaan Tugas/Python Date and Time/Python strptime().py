from datetime import datetime


def demo_basic_strptime():
    print("=== 1. String to Datetime Object (Example 1) ===")
    date_string = "21 June, 2018"
    print("date_string =", date_string)
    print("type of date_string =", type(date_string))

    # Convert string to datetime object using %d %B, %Y
    date_object = datetime.strptime(date_string, "%d %B, %Y")
    print("date_object =", date_object)
    print("type of date_object =", type(date_object))
    print()


def demo_date_format_interpretation():
    print("=== 2. Format Interpretation Differences (Example 2) ===")
    dt_string = "12/11/2018 09:15:32"

    # Considering date is in dd/mm/yyyy format
    dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
    print("dt_object1 (dd/mm/yyyy) =", dt_object1)

    # Considering date is in mm/dd/yyyy format
    dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
    print("dt_object2 (mm/dd/yyyy) =", dt_object2)
    print()


def demo_strptime_directives():
    print("=== 3. Format Directives Reference Demo ===")
    test_cases = [
        ("Sun Sep 30 07:06:05 2018", "%a %b %d %H:%M:%S %Y", "Abbreviated weekday & month"),
        ("Sunday 12 June 2018", "%A %d %B %Y", "Full weekday & month name"),
        ("12/06/18 09:55:22 AM", "%d/%m/%y %I:%M:%S %p", "12-hour format with AM/PM"),
        ("163", "%j", "Day of the year (001-366)"),
        ("24", "%U", "Week number (Sunday first day)"),
        ("24", "%W", "Week number (Monday first day)"),
        ("15/2022%", "%d/%Y%%", "Literal '%' sign parsing with year"),  # Disertai tahun agar bebas warning
    ]

    for raw_str, fmt_code, description in test_cases:
        parsed_dt = datetime.strptime(raw_str, fmt_code)
        print(f"Format: {fmt_code:<22} | Raw: {raw_str:<25} | Output: {parsed_dt}")
    print()

def demo_value_error_handling():
    print("=== 4. Handling ValueError in strptime() ===")
    date_string = "12/11/2018"
    invalid_format = "%d %m %Y"  # Spasi digunakan, padahal string pakai slash '/'

    print(f"Attempting to parse '{date_string}' with format '{invalid_format}'...")

    try:
        date_object = datetime.strptime(date_string, invalid_format)
        print("date_object =", date_object)
    except ValueError as error:
        print(f"[Caught Expected Error] ValueError: {error}")
        print("Solusi: Pastikan delimiter (seperti `/` atau `-`) dan urutan spesifier sama persis dengan string asal.")
    print()


if __name__ == "__main__":
    # Execute all demonstration functions sequentially
    demo_basic_strptime()
    demo_date_format_interpretation()
    demo_strptime_directives()
    demo_value_error_handling()