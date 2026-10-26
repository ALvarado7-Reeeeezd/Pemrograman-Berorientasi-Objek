import datetime
from datetime import date, datetime as dt, time, timedelta

def demo_basic_now_and_today():
    print("=== 1. Current Date & Time ===")
    # Get current datetime
    now = datetime.datetime.now()
    print("Current DateTime:", now)

    # Get current date
    current_date = datetime.date.today()
    print("Current Date:", current_date)
    print()


def demo_module_attributes():
    print("=== 2. Attributes of datetime Module ===")
    # Print all attributes of datetime module
    print(dir(datetime))
    print()


def demo_date_class():
    print("=== 3. Python datetime.date Class ===")
    # Instantiating date object
    d = datetime.date(2022, 12, 25)
    print("Custom Date:", d)

    # Import and use date class directly
    d_direct = date(2022, 12, 25)
    print("Direct imported Date:", d_direct)

    # Get today's date
    todays_date = date.today()
    print("Today's date =", todays_date)

    # Date from UNIX timestamp
    timestamp_date = date.fromtimestamp(1326244364)
    print("Date from timestamp =", timestamp_date)

    # Access date attributes
    today = date.today()
    print(f"Current year: {today.year}")
    print(f"Current month: {today.month}")
    print(f"Current day: {today.day}")
    print()


def demo_time_class():
    print("=== 4. Python datetime.time Class ===")
    # Instantiate time objects
    a = time()
    b = time(11, 34, 56)
    c = time(hour=11, minute=34, second=56)
    d = time(11, 34, 56, 234566)

    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)

    # Time attributes
    print(f"Hour = {b.hour}")
    print(f"Minute = {b.minute}")
    print(f"Second = {b.second}")
    print(f"Microsecond = {b.microsecond}")
    print()


def demo_datetime_class():
    print("=== 5. The datetime.datetime Class ===")
    # Instantiate datetime objects
    a = dt(2022, 12, 28)
    b = dt(2022, 12, 28, 23, 55, 59, 342380)

    print("a =", a)
    print("b =", b)

    # Datetime attributes & timestamp
    print(f"Year = {b.year}")
    print(f"Month = {b.month}")
    print(f"Hour = {b.hour}")
    print(f"Minute = {b.minute}")
    print(f"Timestamp = {b.timestamp()}")
    print()


def demo_timedelta_class():
    print("=== 6. Python datetime.timedelta Class ===")
    # Difference between date objects
    t1 = date(year=2018, month=7, day=12)
    t2 = date(year=2017, month=12, day=23)
    t3 = t1 - t2
    print("t3 =", t3)

    # Difference between datetime objects
    t4 = dt(year=2018, month=7, day=12, hour=7, minute=9, second=33)
    t5 = dt(year=2019, month=6, day=10, hour=5, minute=55, second=13)
    t6 = t4 - t5
    print("t6 =", t6)

    print("Type of t3 =", type(t3))
    print("Type of t6 =", type(t6))

    # Difference between timedelta objects
    td1 = timedelta(weeks=2, days=5, hours=1, seconds=33)
    td2 = timedelta(days=4, hours=11, minutes=4, seconds=54)
    td3 = td1 - td2
    print("td3 =", td3)

    # Total seconds in timedelta
    t_duration = timedelta(days=5, hours=1, seconds=33, microseconds=233423)
    print("Total seconds =", t_duration.total_seconds())
    print()


def demo_strftime_and_strptime():
    print("=== 7. Formatting (strftime) and Parsing (strptime) ===")
    now = dt.now()

    # Formatting datetime to string
    t = now.strftime("%H:%M:%S")
    print("Time:", t)

    s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
    print("s1 (US format):", s1)

    s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
    print("s2 (UK format):", s2)

    # Parsing string back to datetime object
    date_string = "25 December, 2022"
    print("date_string =", date_string)
    date_object = dt.strptime(date_string, "%d %B, %Y")
    print("date_object =", date_object)
    print()


def demo_timezone():
    print("=== 8. Timezone Handling with pytz ===")
    try:
        import pytz

        local = dt.now()
        print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

        tz_NY = pytz.timezone('America/New_York')
        datetime_NY = dt.now(tz_NY)
        print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

        tz_London = pytz.timezone('Europe/London')
        datetime_London = dt.now(tz_London)
        print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))
    except ImportError:
        print("[Note] Module 'pytz' belum di-install. Jalankan 'pip install pytz' untuk fitur timezone.")
    print()


if __name__ == "__main__":
    # Executing all feature demonstrations
    demo_basic_now_and_today()
    demo_module_attributes()
    demo_date_class()
    demo_time_class()
    demo_datetime_class()
    demo_timedelta_class()
    demo_strftime_and_strptime()
    demo_timezone()