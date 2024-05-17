class Aimal():
    quantidade_patas = 4
    tem_rabo = False
    tem_pelo = True
    especie = ''
    sexo = 'femia'

class Cachorro(Aimal):
    tem_rabo = True
    especie = 'Canis lupus famiiaris'
    raca = 'shitzu'
    nome = 'meg'
    porte = 'pequeno'

    def latir():
        return 'AUAUAUAUAUAU'

    def comer():
        return 'sons de cachorro comendo'  

    def dormir():
        return 'ZZZZZZZ'      
