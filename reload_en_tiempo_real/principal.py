import importlib
import reload_en_tiempo_real.modulo as modulo
import time

modulo.saludo()
while True:
    time.sleep(2)  # Espera 2 segundos antes de recargar
    importlib.reload(modulo)
    print("\r", end="")  # Mueve el cursor al inicio de la línea
    modulo.saludo()