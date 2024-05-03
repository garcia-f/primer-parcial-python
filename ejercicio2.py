

#  funcion capitalizar_palabra
def capitalizar_palabra( palabra ):

    #  si palabra es igual a un str que capitalize la palabra
    if type(palabra) == str:
        palabra_capitalizada = palabra.capitalize() # capitalize() metodo para capitalizar la palabra
        return palabra_capitalizada
    else:
        return 'Debes ingresar una estring'   


print(capitalizar_palabra('prueba'))
print(capitalizar_palabra('PRUEBA'))
print(capitalizar_palabra('Prueba'))