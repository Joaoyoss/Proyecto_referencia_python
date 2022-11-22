print("************************************************")
print("         Sistema de control vacacional Rappi    ")
print("************************************************")


var_nom_empleado=input("Por favor introduce el nombre del empleado: ")
var_clave_depart= int (input("Por favor introduce clave de departamento: "))
var_ant_empleado=float(input("Por favor introduce los años laborales del empleado: "))

if var_clave_depart==1:
    if var_ant_empleado==1 and var_ant_empleado<2:
        print("El empleado ", var_nom_empleado, " tiene derecho a 6 dìas de vacaciones.")
    elif var_ant_empleado>=2 and var_ant_empleado<=6:
        print("El empleado ", var_nom_empleado, " tiene derecho a 14 dìas de vacaciones.")
    elif var_ant_empleado>=7 :
        print("El empleado ", var_nom_empleado, " tiene derecho a 20 dìas de vacaciones.")
    else:
        print ("El empleado ", var_nom_empleado, " NO tiene derecho a dìas de vacaciones.")

elif var_clave_depart==2:
    if var_ant_empleado==1 and var_ant_empleado<2:
        print("El empleado ", var_nom_empleado, " tiene derecho a 7 dìas de vacaciones.")
    elif var_ant_empleado>=2 and var_ant_empleado<=6:
        print("El empleado ", var_nom_empleado, " tiene derecho a 15 dìas de vacaciones.")
    elif var_ant_empleado>=7 :
        print("El empleado ", var_nom_empleado, " tiene derecho a 22 dìas de vacaciones.")
    else:
        print ("El empleado ", var_nom_empleado, " aun NO tiene derecho a dìas de vacaciones.")

elif var_clave_depart==3:
    if var_ant_empleado==1 and var_ant_empleado<2:
        print("El empleado ", var_nom_empleado, " tiene derecho a 10 dìas de vacaciones.")
    elif var_ant_empleado>=2 and var_ant_empleado<=6:
        print("El empleado ", var_nom_empleado, " tiene derecho a 20 dìas de vacaciones.")
    elif var_ant_empleado>=7 :
        print("El empleado ", var_nom_empleado, " tiene derecho a 30 dìas de vacaciones.")
    else:
        print ("El empleado ", var_nom_empleado, " aun NO tiene derecho a dìas de vacaciones.")

else: 
    print("La clave de departemneto no existe; por favor vuelva a intentarlo con una clave de valor vàlido")

