print("Welcome to the MPH to MPS Conversion App")
speed_in_miles=float(input("What is your speed in miles:"))
speed_in_meters=speed_in_miles * 0.4474
rounded_speed_in_meters=round(speed_in_meters,2)
print(f"Your speed in MPS is: {rounded_speed_in_meters}")
