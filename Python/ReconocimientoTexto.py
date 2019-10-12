from PIL import Image
# Importamos Pytesseract
import pytesseract

# Abrimos la imagen
im = Image.open("Imagenes/Charlie.jpeg")


# Utilizamos el método "image_to_string"
# Le pasamos como argumento la imagen abierta con Pillow
texto = pytesseract.image_to_string(im)

# Mostramos el resultado
print(texto)