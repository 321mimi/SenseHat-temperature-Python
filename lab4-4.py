# SenseHat temperature
# By Michelle Cantin

from sense_hat import SenseHat

sense = SenseHat()
temp = sense.get_temperature()

# The function
def convertTemperature(temp):
    result = str(int((temp * (9/5)) + 32))
    return result

# Calls the function and prints it
print(convertTemperature(temp))
