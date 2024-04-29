class Celulares:
    def __init__(self, marca, ano, modelo, bateria):
        self.marca = marca
        self.ano = ano
        self.modelo = modelo
        self.bateria = bateria
    def ligar(self):
        return 'ligando o celular'
    def carregar(self):
        if self.marca == 'xiamomi':
            return '30 minutos'
        else:
            return'60 minutos'
    def despertar(self):
        return 'padrão'

celular1 = Celulares('xiaomi', 2021, 'pocoX3', 30)
print(celular1.carregar())               