def temperatura():
    try:
        # Lee el archivo de temperatura (ajustar zone0 si es necesario)
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = int(f.read()) / 1000
            return temp
    except FileNotFoundError:
        return "Sensor no encontrado"