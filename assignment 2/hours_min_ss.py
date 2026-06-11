time_str = input("Enter time (HH:MM:SS): ")

hh, mm, ss = map(int, time_str.split(':'))

total_seconds = hh * 3600 + mm * 60 + ss

print("Total seconds:", total_seconds)