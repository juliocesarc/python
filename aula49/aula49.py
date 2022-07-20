class Pessoa:
    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, *comida):
        if self.comendo:
            print(f'{self.nome} já está comendo!')
            return

        print(f'{self.nome} está comendo')
        self.comendo = True

    def falar(self, *assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar pois está comendo')
            return
        elif self.falando:
            print(f'{self.nome} já está falando!')
            return
        
        print(f'{self.nome} agora está falando sobre {assunto[0]}!')
        self.falando = True

    def parar_de_comer(self, *comida):
        if self.comendo:
            print(f'{self.nome} agora parou de comer!')
            self.comendo = False
            return
        print(f'{self.nome} já parou de comer!')

