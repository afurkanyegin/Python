print("Welcome to the Temperature Conversion App")
temp_in_f=float(input("What is the temperature in Fahrenheit: "))
temp_in_c=(temp_in_f - 32)/(1.8)
temp_in_k=(temp_in_f - 32)/(1.8) + 273.15
rounded_temp_in_c=round(temp_in_c,4)
rounded_temp_in_k=round(temp_in_k,4)
print(f"Temp in Fahrenheit is:\t {temp_in_f}")
print(f"Temp in Celcius is:\t {rounded_temp_in_c}")
print(f"Temp in Kelvin is:\t {rounded_temp_in_k}")
