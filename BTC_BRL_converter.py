import PySimpleGUI as sg
import requests
import json

#requisição API
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_btc = float(cotacoes["BTCBRL"]["bid"])

class TelaConversor:
    #construtor
    def __init__(self):
        sg.change_look_and_feel('LightGrey1')
        #layout
        layout = [
            [sg.Text('Digite o valor em Real para converter em Bitcoin:',size=(45,0)),sg.Input(0.0,size=(25,0),key='real')],
            [sg.Text('Digite o valor em Bitcoin para converter em Real:',size=(45,0)),sg.Input(0.0,size=(25,0),key='bitcoin')],  
            [sg.Button('Converter')],
            [sg.Output(size=(80,5))]        
        ]
        #janela
        self.janela = sg.Window("Conversor BTC/BRL").layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            real = float(self.values['real'])
            bitcoin = float(self.values['bitcoin'])
    
            print('{} em Real convertido para Bitcoin equivale a BTC {:.2f}'.format(real, (real/cotacao_btc)))
            print('{} em Bitcoin convertido para Real equivale a BRL {:.2f}'.format(bitcoin, (bitcoin*cotacao_btc)))


conversor = TelaConversor()
conversor.Iniciar()            