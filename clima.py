import requests
import PySimpleGUI as sg

def temperaturas():
    try:
        key = '3d750123dbfeefcba851a398e9d81521'
        site = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}&lang=pt_br"

        requisicao = requests.get(site)
        requisicao_dicionario = requisicao.json()

        situacao = requisicao_dicionario['weather'][0]['description']
        temperatura = requisicao_dicionario['main']['temp'] - 273.15
        sensacao = requisicao_dicionario['main']['feels_like'] - 273.15    
    except:
        janela['mensagem'].update("""Houve um erro! 
Verifique se as informaçoes estão digitadas corretamente.""")    
    else:
        janela['mensagem'].update(f"""Situação: {situacao.upper()}
Temperatura: {temperatura:.1f}°C
Sensação térmica: {sensacao:.1f}°C""")


sg.theme("SystemDefault")
layout = [
    [sg.Text("Cidade")],
    [sg.Input(key="cidade", size=(30,1))],
    [sg.Button("Buscar")],
    [sg.Text(" ", key="mensagem")]
]

janela = sg.Window("CLIMA", layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break   
    elif eventos == "Buscar":
        cidade = valores['cidade']
        temperaturas()

janela.close()
