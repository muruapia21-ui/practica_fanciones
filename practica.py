print ("hola mundo") #que hace esta funcion


nombre= input("como te llamas?") #imput permite la entrada de datos por teclado
print("hola",nombre)


palabra=input("escribi un texto")
print("cantidad de letras:",len(palabra)) #imprime el mensaje y te devuelce el resultado contando los espacios 


numero=input("ingresa un numero:")
numero= int(numero)
print("el doble es:",numero*2)#imprime el numero y despues a ese resultado hace el doble y a ese numero lo multiplica


numero=float(input("ingresa un numero decimal:"))
print("redondeado:", round(numero))#esto tiene varias funciones en esto, y hace mas corta las lineas y que de el mismo resultado linea de codigo nos pide un numero decimal, y entonces despues lo redondea y hace el numero mas chico o mas grande dependiendo los los numeros
#innova la funcion argumenta los comandos, y concatenamos a lineas

#crear un programa que:pida un nombre y la edad en desimal muestre cuantos caracteres tiene el nombre y muestre la edad redondeada

nombre=input("ingresa tu nombre:")
edad=float(input("ingresa tu edad:"))#pide q ingreses tu edad 
print("cantidad de caracteres en el nombre:", len(nombre))#cuenta cuantos caracteres tiene tu nombre y lo imprime
print("edad redondeada:", round(edad))#redondea la edad y la imprime
