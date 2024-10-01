import datetime
#Playing with dates, python refresher.
#Also Happy Halloween!
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

today = datetime.date.today()
print("Today's date:", today)

specific_date = datetime.date(2024, 10, 1)
print("Specific date:", specific_date)

formatted_date = specific_date.strftime("%A, %B %d, %Y")
print("Formatted date:", formatted_date)

future_date = datetime.date(2025, 10, 1)
date_difference = future_date - today
print(f"Days until {future_date}: {date_difference.days} days")

one_week_later = today + datetime.timedelta(days=7)
print("One week from today:", one_week_later)

thirty_days_ago = today - datetime.timedelta(days=30)
print("30 days ago:", thirty_days_ago)
