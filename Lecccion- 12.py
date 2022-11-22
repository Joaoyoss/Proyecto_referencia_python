print("**************************************")
print("    Challenger: Buscando nùmero par    ")
print("**************************************")

var_num_introducido=int(input("Introduce un nùmero entero: "))

#if type(var_num_introducido)!= "":

if type(var_num_introducido)==int:

    #print(var_num_introducido%2==0)

    if var_num_introducido>=0:

        if var_num_introducido%2==0:
            print("El nùmero: ",var_num_introducido," es un nùmero par.")
        else:
            print("El nùmero: ", var_num_introducido," es un nùmero impar.")

    else:
        print("El valor ",var_num_introducido, " No es un nùmero positivo")  
       
else:
    print("El valor ",var_num_introducido, " No es un nùmero entero")

#else:
    #print ("El nùmero ", var_num_introducido, " no es un dato valido de nùmero, es un string")