import urequests
import log

url_medicao = "http://<IP_DO_SERV_API>:8000/medicao"
url_logs = "http://<IP_DO_SERV_API>:8000/log"

def enviar_dados(dados):
    log.log_system('Enviando dados para API')
    try:
        urequests.post(url_medicao, json=dados,timeout=10)
        log.log_system('Sucess: Dados enviados')
    except:
        log.log_system('Error: Falha ao enviar dados')

def enviar_log(data_hora):

    with open("log_system.txt", "r") as arquivo:
        linhas = [linha.strip() for linha in arquivo]
    dados = {
        "data": data_hora,
        "log": linhas
    }

    log.log_system('Enviando LOG para API')

    
