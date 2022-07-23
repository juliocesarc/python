from log import LogMixin

class Eletronico:
    def __init__(self, nome):
        self.nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            print('Já está ligado!')
            return
        print('Ligado...')
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            print('Já está desligado!')
            return
        print('Desligado...')
        self._ligado = False

class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self.conect_wifi = False

    def conectar(self):
        if not self._ligado or self.conect_wifi:
            erro = 'Seu Smartphone se encontra desligado ou já está conectado...'
            self.log_error(erro)
            return

        info = 'Smartphone conectado!'
        self.log_info(info)
        self.conect_wifi = True

    def desconectar(self):
        if not self.conect_wifi or not self._ligado:
            erro = 'Smartphone já se encontra desconectado ou está desligado...'
            self.log_error(erro)
            return

        info = 'Smartphone desconectado!'
        self.log_info(info)
        self.conect_wifi = False

