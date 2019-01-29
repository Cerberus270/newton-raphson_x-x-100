import math
import time
en=(input("Ingrese el primer numero para iniciar la iteracion=> "))
num=float(en)
datos=[]
r=0
datos.append(en)
i=0
x1=(int(100))
contador=0
#numerador=((num**num)-100)
#denominador=((num**num)*(1+math.log(num,math.e)))
#ecuacion=(num-((num**num)-100)/((num**num)*(1+math.log(num,math.e))))
#////////////////////////////////////#
while True:
    ingreso=float(datos[i])
    ecuacion=(ingreso-((ingreso**ingreso)-100)/((ingreso**ingreso)*(1+math.log(ingreso,math.e))))
    datos.append(ecuacion)
    r=int(ingreso**ingreso)
    print(ingreso)
    time.sleep(1)
    print(r)
    i+=1
    contador+=1
    if r==x1:
        ingreso1=str(ingreso)
        r1=str(r)
        con=str(contador)
        print("X^X=100 Se obtubo de la siguiente manera: "+ingreso1+"^"+ingreso1+" = "+r1)
        print("Se necesitaron "+con+" iteraciones")
        break