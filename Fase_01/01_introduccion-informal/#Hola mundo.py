#Hola mundo
print("Hola Mundo")
print('Hola Mundo')
#"esta 'palabra se encuentra escrita entre comillas simples'"
#"esta \"palabra\" se encuentra escrita entre comillas dobles'"
#"esta 'palabra' se encuentra escrita entre comillas dobles'

#La funcion Print()
#--Es una funcion que permite mostrar el valor de una cadena u otros valores ,
#  variables en pantalla
#ejempl: "Una cadena"
#ejempl: 'otra cadena'
#ejempl: 'otra cadena mas'

print("Una cadena")
print('otra cadena')
print('otra cadena mas')

#Acepta caracteres especiales , como tabulaciones/t o saltos de linea \n}
print("un texto\tuna tabulacion")
print("un texto\nuna nueva linea")

#Para evitar los caracteres especiales se debe indicar que una cadena es cruda
#(raw)
#forma incorecta
print("C:\nombre\Directorio\temporales")
#Forma correcta con formato raw representado con r
print(r"C:\nombre\temporal")

##  Es posible utilizar la triple comilla para cadenas multiples
print("""una linea
otra linea
otra linea\tuna tabulacion""")

##Tambien podemos asignar cadenas a variables
#--La forma correcta de mostrarles es con la instruccion print().

c = ("Esto es una cadena\nCon dos lineas")
print (c)

##Operaciones
#Una de las operaciones de las cadenas es la concatenacion(o suma de cadenas)
c+c
print(c+c)

s="Una cadena" "compuesta de dos cadenas"
print(s)

c1 = "Una cadena"
c2 = "Otra cadena"
print("Una cadena" + c2)

##Tambien es posible utilizar la multiplicacion de cadenas
diez_espacios=" " * 10
print(diez_espacios+ "Un texto a diez espacios")

##Indices en las cadenas
#-Los indices nos permiten posicionarnos en un caracter especifico
#de una cadena
#Represe un numero (indice), que empezando por el 0 indica el caracter
#de la primera posicion , y asi susecivamente 
palabra = "Python"
palabra[0] #Caracter en la posicion 0
print(palabra)

palabra1 = "Python"
palabra1[3] #Caracter en la posicion 3
print(palabra)
