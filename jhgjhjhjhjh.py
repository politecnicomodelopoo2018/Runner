from Clases.DB import db

a = db.connect("select Nombre,Puntaje from Jugador order by Puntaje desc ")
y = []
for j in a :
    y.append(j)
print(y)