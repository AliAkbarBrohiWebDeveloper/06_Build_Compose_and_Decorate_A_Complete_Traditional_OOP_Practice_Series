# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class Temprature_Converter():
    @staticmethod
    def celcuius_to_farenhiet(c):
        return (c*9/5)+32
    
temp_c=25
temp_f=Temprature_Converter.celcuius_to_farenhiet(temp_c)
print(f"{temp_c}°C is equal to {temp_f}°F")
