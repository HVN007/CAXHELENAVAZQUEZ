x=int(input("Escribe la calificación de tu primer trimestre: "))
y=int(input("Escribe la calificacion de tu segundo trimestre: "))
z=int(input("Escribe la calificacion de tu tercer trimestre: "))

r=(x+y+z)
p=(r/3)
print("Tu promedio del año es ",p)

if (p>=6):
  print("Aprobaste, muy bien!")
if (p==10):
  print("Wow! Mereces una medalla")
if (p<6):
  print("Ups, Creo que repetirás año")
