print("Enter the time duration to convert:")
timeDuration_str = input()
timeDuration = int(timeDuration_str) # Convert input string into integer
sec = timeDuration % 60
min = (timeDuration // 60) % 60
hr = timeDuration // (60 * 60)
print("It is", hr, ":", min, ":", sec)
