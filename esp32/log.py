import json
import hours

def registrar(temperatura,current_states,data,horas):
    with open('general_log.txt','a',encoding="utf-8") as arquivo:
        arquivo.write(f'data:{data},hrs:{horas},{temperatura}C,rele:{current_states}\n')

def mudanca_de_estado(estado_antigo,estado_atual,temperatura,data_hora):
    if estado_antigo != estado_atual:
        print('O estado mudou, registrando ....')
        registrar(temperatura,estado_atual,data_hora)
        estado_antigo = estado_atual
        return estado_antigo



def log_system(informacao):

    data_hora = f'{hours.pegar_data()} {hours.pegar_horas()}'
    
    informacao = f'{data_hora}, {informacao}'
    with open('log_system.txt', 'a', encoding='utf-8')  as arquivo:
        arquivo.write(f'{data_hora},{informacao}\n')




