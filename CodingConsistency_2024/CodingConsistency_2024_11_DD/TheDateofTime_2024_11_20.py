from datetime import datetime
#Finds Current time
current_time = datetime.now()

formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

print(f"The current date and time is: {formatted_time}")
