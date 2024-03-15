def check_weather_and_water_status(temperature):
    if temperature > 30:
        print("it's hot")
    elif temperature < 10:
        print("it's cold")
    else:
        print("it's ok")

    if temperature >= 100:
        print("water would boil")
    elif temperature <= 0:
        print("water would freeze")

if __name__ == "__main__":
    temperature = int(input())

    check_weather_and_water_status(temperature)
