from Clases.DB import db
class scores(object):

    def __init__(self):
        self.nombre = None
        self.puntaje = None


    def cargar(self,pos):
        a = db.connect("select Nombre,Puntaje from Jugador order by Puntaje desc ")
        y = []
        for j in a:
            y.append(j)
        self.nombre = y[pos]['Nombre']
        self.puntaje = y[pos]['Puntaje']