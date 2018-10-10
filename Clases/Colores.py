
class Colores():


    def __init__(self):
        self.Negro = (0, 0, 0)
        self.Blanco = (255, 255, 255)
        self.Gris = (200, 200, 200)
        self.Verdesungo = (125, 254, 29)
        self.Rojo = (250, 1, 0)
        self.Amarillo = (253, 253, 1)
        self.Rosa = (248, 67, 253)
        self.estado = 0
        self.color = self.Gris
        self.locura()
    def locura(self):

        if self.estado == 0:
            self.estado=1
            self.color = self.Blanco
        if self.estado == 1:
            self.estado=2
            return  self.Rojo
        if self.estado == 2:
            self.estado=3
            self.color =  self.Verdesungo
        if self.estado == 3:
            self.estado=4
            self.color =  self.Amarillo
        if self.estado == 4:
            self.estado=0
            self.color =  self.Rosa