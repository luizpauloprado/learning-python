class Camera:
    def __init__(self, modelo):
        self.ligado = False
        self.modelo = modelo

    def ligar(self):
        if not self.ligado:
            self.ligado = True
        print("Ligada")

    def delisgar(self):
        self.ligado = False
        print("Desligada")
