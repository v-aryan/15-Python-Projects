def temperature_conversion(temp):
    f = float(temp)
    c = (f - 32) * 5/9
    return c

fahrenheit = int(input("Enter the temperature degree: "))
print(temperature_conversion(fahrenheit))