class Carro:
    ano_atual = 2022
    def __init__(self, cor_do_carro, ano_do_veiculo, marca):
        self.cor_do_carro = cor_do_carro
        self.ano_do_veiculo = ano_do_veiculo
        self.marca = marca

    def tempo_de_uso(self):
        print(f'Seu carro tem {self.ano_atual - self.ano_do_veiculo} anos')
    
    def marca_do_veiculo(self):
        print(f'Seu carro é da marca {self.marca}')
    
    def informacoes(self):
        print(self.cor_do_carro, self.ano_do_veiculo, self.marca)

carro1 = Carro('Azul', 2004, 'FIAT')
carro1.tempo_de_uso()
carro1.marca_do_veiculo()
carro1.informacoes()