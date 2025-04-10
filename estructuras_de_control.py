#Estructura de un if
"""booleano1=True
if booleano1:
    print("Es True")
else:
    print("Es False")"""    

#Bucles
#Bucle for
"""for i in range(5):
    print(i)

#While
condicion=True
var_interrupcion=1
while(condicion):
    print('Es verdadero') 
    var_interrupcion+=1
    if(var_interrupcion>3):
        condicion=False"""   

#Sentencias de control de bucles
#Break
for i in range(5):
   print(i)
   if i>2:
       break
#Continue   
for i in range(10):
    if i==0:
      continue
    if i%2==0:
      print(i)     

