texto = "Python es un lenguaje de programación increíble para ciencia de datos"
palabras = texto.split()
num_palabras = len(palabras)

palabra_mas_larga = ""

for palabra in palabras:

    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra
contador_a=texto.count("a")
contador_e=texto.count("e")
contador_i=texto.count("i")
contador_o=texto.count("o")
contador_u=texto.count("u")

print(f"El número de palabras en la frase es {num_palabras}")
print(f"La palabra más larga es {palabra_mas_larga}")
print(f"contadores de vocales: a {contador_a} ,e {contador_e} ,i {contador_i} ,o {contador_o} ,u {contador_u} ,")
palabras_ordenadas=sorted(palabras,key=len,reverse=True)
print(palabras_ordenadas[:3])