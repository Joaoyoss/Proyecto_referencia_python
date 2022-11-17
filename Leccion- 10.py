print ("Sistema de calculo de promedio de calificaciònes y definiciòn de aprobado")

#OjO!!!Todo lo que entra de teclado por input entra como texto y el tipo de dato de numero es necesario para las operaciones aritmèticas llevarlo a entero.

nombre = input ("Para comenzar, Introduzca su nombre: ")

cal_matematicas = float(input("Introduce tus calificaciones de matemàticas "+nombre+": "))
cal_espanol = float(input("Introduce tus calificaciones de español "+nombre+": "))
cal_fisica = float (input("Introduce tus calificaciones de fìsica "+nombre+": "))

cal_promedio = (cal_matematicas + cal_espanol + cal_fisica)/3

if cal_promedio>=60:
    print("Felicidades "+nombre+" APROBASTE con un promèdio de: "+ str(cal_promedio))
    print("Felicidades "+nombre+" APROBASTE con un promèdio de: "+ str(round(cal_promedio, 2)))
    
else:
    print("Desapronaste el curso CLIAO con un    promèdio  de: "+ str(cal_promedio))
    print("Desapronaste el curso CLIAO con un promèdio de: "+ str(round(cal_promedio, 1)))

print("Fin a la wea, y eeeraa!!")
