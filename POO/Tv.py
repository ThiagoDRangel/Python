class Tv:
    def __init__(self, tamanho: int) -> None:
        self.__volume = 50
        self.__canal = 1
        self.__tamanho = tamanho
        self.__ligada = False
    
    def aumentar_volume(self):
        if(self.volume > 0 and self.volume < 100):
            self.__volume += 1
        else:
            return "O volume deve estar entre 0 e 99"
        
    def diminuir_volume(self):
        if(self.volume > 0):
            self.__volume -= 1
        else:
            "O volume deve ser maior do que 0"

    def modificar_canal(self, canal: int):

        if(canal > 0 and canal < 100):
            self.__canal = canal
        else:
            raise ValueError("Canal indisponível")

    def ligar_desligar(self, ligada):
        self.__ligada = not self.__ligada