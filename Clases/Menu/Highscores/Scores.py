from Clases.DB import db
class scores(object):

    def __init__(self):
        self.nombre = None
        self.puntaje = None

    @staticmethod
    def cargar():
        a = db.connect("select Nombre,Puntaje from Jugador order by Puntaje desc ")
        y = []
        for j in a:
            y.append(j)
        lista=[]
        for z in range(4):
            a = scores()
            a.nombre=y[z]['Nombre']
            a.puntaje=y[z]['Puntaje']
            lista.append(a)
        return lista