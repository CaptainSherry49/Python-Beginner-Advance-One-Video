# Celcius to Farenheit
# (0°C × 9/5) + 32 = 32°F

def Converting_Temperature():
    user = int(input("Enter the Temperature to Convert it into Farenheit from Celcius:\n"))
    Farenheit = (user*(9/5))+32
    print(f"The Given {user} Celcius temperature is Converted into Farenheit temperature {Farenheit}")

Converting_Temperature()