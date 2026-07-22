import ntptime
import time     


#Conectando no wifi
# conection.conectar_wifi()

# Atualiza horário pela internet
ntptime.settime()

# Pega o horário
hora = time.localtime()

hora = time.localtime(time.time() - 3*3600)

horario_formatado = "{:02d}:{:02d}:{:02d}".format(
    hora[3],
    hora[4],
    hora[5]
)

