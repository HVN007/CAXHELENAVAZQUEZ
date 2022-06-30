import datetime 
dia= datetime.date.today()
print(dia)
w=dia.weekday()+1

print(w)

if(w==0):
  print("Feliz domingo")
elif(w==1):
  print("Disfruta el Lunes")
elif(w==2):
  print("Que te vaya bien este martes!")
elif(w==3):
  print("Buen Miercoles!")
elif(w==4):
  print("Juevess!")
elif(w==5):
  print("Por fin Viernes!")
else:
  print("Yoho, es sabado!")