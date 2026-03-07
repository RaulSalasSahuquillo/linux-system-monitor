import psutil

def cpu():
    # 1. Obtener el uso de CPU en porcentaje
    # Intervalo de 1 segundo
    cpu_usage = psutil.cpu_percent(interval=1)

    # 2. Obtener el número de núcleos lógicos
    cpu_count = psutil.cpu_count()

    # 3. Frecuencia de la CPU (actual, mínima, máxima)
    cpu_freq = psutil.cpu_freq()
    return (f"Uso de la CPU: {cpu_usage}%\nNúcleos lógicos: {cpu_count}\nFrecuencia actual: {cpu_freq.current} Mhz")
