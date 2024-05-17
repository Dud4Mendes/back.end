class Celular():
    bateria = 'infinita'
    tela = '4x3'
    tem_camera = True
    tem_botao = True
    tem_antena = True
    cor = 'Cinza'
    modelo = 'tijolão'

    def ligacao():
        print('ligando...')

    def mensagem():
        print('enviando menagem...')

    def jogo_cobrinha():
        print('jogo criado')

print(Celular.bateria)
print(Celular.jogo_cobrinha())                