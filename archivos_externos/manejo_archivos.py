from io import open

archivo_texto = open("archivo.txt", "w")

frase = "Estupendo dia para estidia python \n el lunes"

archivo_texto.write(frase)

archivo_texto.close()
