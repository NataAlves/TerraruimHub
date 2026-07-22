import network
from time import sleep
import log

SSID = 'NMMUV 2G'
SENHA = '104156127'


wifi = network.WLAN(network.STA_IF)

def conectar_wifi():
    
    try:
        # Refente ao Wifi
        wifi = network.WLAN(network.STA_IF)
        wifi.active(True)
        
        while not wifi.isconnected():
        # Dados da rede, usuário e senha
            wifi.connect(SSID,SENHA)
            print('Conectando...')

        # Mostra o IP do ESP32
        config_off = wifi.ifconfig()
        my_ip = 'IPv4:',config_off[0] 
        print('Conectado!!')
        log.log_system(f)
        log.log_system(f'Sucess: Conectado ao WIfi IPv4:{my_ip}')
        return True
    except: 
        print('Falha ao conectar no wifi')
        log.log_system('Error: Conectar ao Wifi')

def desligar_wifi():
    log.log_system('Sucess: Desligando WIfi')
    wifi.disconnect()
    wifi.active(False)




    

