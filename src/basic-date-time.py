from datetime import date, datetime

today = date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())

now = datetime.now()

print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# Formatting

print(now.strftime("%Y-%m-%d"))  # 2026-11-15
print(now.strftime("%d.%m.%Y"))  # 15.11.2026
print(now.strftime("%H:%M:%S"))  # 21:30:45
print(now.strftime("%Y%m%d_%H%M%S"))  # 20261115_213045
print(now.strftime("%A, %d %B %Y"))  # Sunday, 15 November 2026
print(now.strftime("%I:%M %p"))  # 09:30 PM

# ISO format

iso_timestamp = now.isoformat()

print(f"ISO format date time: {iso_timestamp}")

# From ISO format

date_string = "2026-11-15T14:30:00+01:00"

parsed = datetime.fromisoformat(date_string)

print(parsed)
