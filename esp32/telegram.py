import requests
import json


BOT_TOKEN = 'TOKEN DO GRUPO QUE FOI CRIADO '
CHAT_ID = 'ID DA CONVERSA SUA COM O BOOT'


def bot_telegram(temperatura,lampada,data_horario):

    url_telegram = "https://api.telegram.org/bot{}/sendMessage".format(BOT_TOKEN)

    if lampada == 'ON':
        lampada = 'ON (*)'
    else:
        lampada = 'OFF ( )'


    dados = f'Terrarium Hub !!!\nEsp 32 C3 SMini \n===================\nHorario:              {data_horario} \nTemperatura:     {temperatura}°C \nLampada:          {lampada} \n '

    mensagem = {
        "chat_id": CHAT_ID,
        "text": dados ,
    }

    try:
        
        print('Chatid', CHAT_ID)
        resposta = requests.post(url_telegram, json=mensagem)

        print("Resposta:", resposta.text)

        resposta.close()

    except Exception as e:
        print("Erro:", e)


################################################################################

def mensagem_telegram(mensagem):
    
    url_telegram = "https://api.telegram.org/bot{}/sendMessage".format(BOT_TOKEN)

    mensagem = {
        "chat_id": CHAT_ID,
        "text": mensagem ,
    }
    
    try:
        resposta = requests.post(url_telegram, json=mensagem)

        print("Resposta:", resposta.text)

        resposta.close()

    except Exception as e:
        print("Erro:", e)
