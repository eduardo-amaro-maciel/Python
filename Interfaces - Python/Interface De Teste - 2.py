import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        # Layout
        Layout = [
            [sg.Text ('NOME', size = (5, 0)), sg.Input (size = (20, 0), key = 'nome')],
            [sg.Text ('IDADE', size = (5, 0)), sg.Input (size = (5, 0), key = 'idade')],
            [sg.Text ('CPF', size = (5, 0)), sg.Input (size = (15, 0), key = 'cpf')],
            [sg.Text ('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox ('Gmail', key = 'gmail'), sg.Checkbox ('Outlook', key = 'outlook'), sg.Checkbox ('Yahoo', key = 'yahoo')],
            [sg.Text ('Aceita cartão')],
            [sg.Radio ('Sim', 'cartões', key = 'AceitaCartao'), sg.Radio ('Não', 'cartões', key = 'NaoAceitaCartao')],
            [sg.Slider (range = (0, 250), default_value = 0, orientation = 'h', size = (15, 20), key = 'SliderVelocidade')],
            [sg.Button ('ENVIAR DADOS')],
            [sg.Output (size = (30, 10))]
        ]
        # Janela
        self.Janela = sg.Window ("Dados do usuario").layout (Layout)


    def Iniciar(self):
        while True:
            # Extrair os dados da janela
            self.button, self.values = self.Janela.Read ()
            nome = self.values['nome']
            idade = self.values['idade']
            user_cpf = self.values['cpf']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['AceitaCartao']
            nao_aceita_cartao = self.values['NaoAceitaCartao']
            slider_velocidade = self.values['SliderVelocidade']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'cpf: {user_cpf}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita outlook: {aceita_outlook}')
            print(f'aceita yahoo: {aceita_yahoo}')
            print(f'aceita cartão: {aceita_cartao}')
            print(f'não aceita cartão: {nao_aceita_cartao}')
            print(f'velocidade do escript esta em: {slider_velocidade}')


# Programa principal
Tela = TelaPython()
Tela.Iniciar()