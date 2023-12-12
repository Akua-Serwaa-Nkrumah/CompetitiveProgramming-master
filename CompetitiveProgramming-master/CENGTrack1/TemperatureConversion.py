class Solution:
    def convertTemperature(self, celsius):
        if(0 <= celsius <= 1000):
            kelvin = celsius + 273.15
            fahrenheit = celsius*1.80 + 32.00
            ans = [kelvin, fahrenheit]
        else:
            print("Temperature in celsius should between 0 and 1000")
        return ans