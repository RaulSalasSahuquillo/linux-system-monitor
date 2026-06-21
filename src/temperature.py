def get_temperature():
    try:
        # Read the temperature file (adjust zone0 if necessary)
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = int(f.read()) / 1000
            return temp
    except FileNotFoundError:
        return "Sensor not found"
