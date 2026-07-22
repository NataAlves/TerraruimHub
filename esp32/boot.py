from connection import conectar_wifi
import ntptime
import time
from temperature import ler_temp,on_off
from hours import pegar_data, pegar_horas
from log import mudanca_de_estado, log_system
from api import enviar_dados, enviar_log
import gc
from machine import WDT

log_system('ESP ligado')
time.sleep(2)
try:
    #Conectando no wifi
    conectar_wifi()
    time.sleep(1)
    #  Atualizo o NTP
    ntptime.settime()
    print('Sincronizado NTP')
    time.sleep(1)

except:
    log_system('Falha ao conectar ao WIFI ou ao Atualizar o NTP')  
finally:
    #desligar_wifi()
    print('finalizado excessão do primiro boot')
    time.sleep(1)


# Tempo para reiniciar caso o programa pare de responder
wdt = WDT(timeout=60000)  # 60 segundos
enviar_api = time.ticks_ms()
ultima_leitura = time.ticks_ms()
ultima_ntp = time.ticks_ms()

estado_antigo = 'DESCONHECIDO'
temperatura = ler_temp()
estado_atual = on_off(estado_antigo, temperatura)
time.sleep(1)
while True:

    time_atual = time.ticks_ms()

    # Checando data e hora
    data_hora = f'{pegar_data()} {pegar_horas()}'
    time.sleep(1)
    
    # definindo tempo de 5 segundos entre cada leitura
    if time.ticks_diff(time_atual,ultima_leitura) >= 5000:
        # Checando temperatura 
        temperatura = ler_temp() 

        # Checando se a lampada esta ligada ou desligada
        estado_atual = on_off(estado_antigo, temperatura)
        ultima_leitura = time_atual

    dados={
        'temperatura':temperatura,
        'lampada': estado_atual,
        'horario': data_hora,
       }
    print(f'{5*"#"}\n{data_hora}\nTemperatura:{temperatura}\nLampada:{estado_atual}\nEstado Antigo: {estado_antigo}°C')
    print(10 * '==')
    time.sleep(5)
    # mudança de estado
    mudanca_de_estado(estado_antigo,estado_atual,temperatura,data_hora)
    time.sleep(1)
    estado_antigo = estado_atual
    time.sleep(1)
    wdt.feed()
    # definindo 5 minutos para cada envio de log
    if time.ticks_diff(time_atual, enviar_api) >= 600000:    
        try:
            wdt.feed()
            conectar_wifi()

            wdt.feed()
            # Envia dados para API
            enviar_dados(dados)

            wdt.feed()
            # Enviando log para API
            enviar_log(data_hora)
        except Exception as e:
            log_system(f"Erro API: {e}")
        finally:
            #desligar_wifi()
            print('finalizado excessão do primiro boot')
            enviar_api = time_atual
    
        if time.ticks_diff(time_atual, ultima_ntp) >= 43200000:
            try:
                conectar_wifi()
                ntptime.settime()
                ultima_ntp = time_atual
            finally:
                #desligar_wifi()
                print('finalizado excessão do primiro boot')


    # Limpa Memoria
    gc.collect()
    print('Cheguei no final do looping, limpei memoria')
    time.sleep_ms(10)
    

    


    


