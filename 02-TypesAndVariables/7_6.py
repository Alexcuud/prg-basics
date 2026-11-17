speed = int(input("Enter the speed in km/h: "))
speed_ok = speed >= 40 and speed <= 140
print(f'Speed is within the allowed range (40-140 km/h): {speed_ok}')