from machine import Pin 
import dht
import log

# Nome do Sensor
sensor = dht.DHT22(Pin(4))

# Pinagem do Relê
rele = Pin(27, Pin.OUT)

# Fara leitura da temperatura
def ler_temp():
    try:
        sensor.measure()
        temperatura = f'{sensor.temperature():.1f}'
        log.log_system(f'Sucess: Leitura de temperatura, {temperatura}°C')
        return temperatura

    except:
        log.log_system('Error: Falha na Leitura de temperatura ')
        return -99.0

estado_antigo = 'OFF'
rele.value(1)

def on_off(temp):
    log.log_system('Tomando decisao "ON/OFF"')
    if temp <= 21:
        rele.value(0)
        estado_antigo = 'ON'
        return 'ON'
    elif temp > 25:
        rele.value(1)
        estado_antigo = 'OFF'
        return 'OFF'
    else:
        return estado_antigo


