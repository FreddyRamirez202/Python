import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Cargar la imagen de Mario
mario_image = Image.open('C:/Users/theal/OneDrive/Escritorio/Python_FromScratch\Python_Advanced/mario_pic.png')

# Convertir la imagen a escala de grises
mario_gray = mario_image.convert('L')

# Pixelar la imagen reduciendo su tamaño y luego aumentándolo de nuevo
size = (32, 32)  # Tamaño para la pixelación
mario_small = mario_gray.resize(size, resample=Image.BILINEAR)
mario_pixelated = mario_small.resize(mario_gray.size, Image.NEAREST)

# Mostrar la imagen pixelada en escala de grises
plt.imshow(mario_pixelated, cmap='gray')
plt.axis('off')  # Ocultar los ejes
plt.show()

# Guardar la imagen pixelada en escala de grises
mario_pixelated.save('mario_pixelated_gray.png')

# import numpy as np
# import matplotlib.pyplot as plt

# # Definir la matriz de intensidad de píxeles para una versión simplificada de Mario
# matriz_mario = np.array([
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 50, 50, 100, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 50, 0],
#     [0, 50, 100, 150, 200, 255, 255, 255, 255, 255, 255, 255, 255, 200, 100, 0],
#     [0, 100, 150, 200, 200, 255, 255, 255, 255, 255, 255, 255, 200, 150, 100, 0],
#     [0, 100, 150, 200, 200, 200, 255, 255, 255, 255, 255, 200, 200, 150, 100, 0],
#     [0, 0, 100, 150, 200, 200, 200, 255, 255, 255, 200, 200, 150, 100, 0, 0],
#     [0, 0, 100, 150, 200, 200, 255, 255, 255, 255, 255, 200, 150, 100, 0, 0],
#     [0, 0, 0, 100, 150, 200, 255, 255, 255, 255, 200, 150, 100, 0, 0, 0],
#     [0, 0, 0, 0, 0, 100, 200, 255, 255, 255, 200, 100, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 100, 255, 255, 100, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 100, 100, 100, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 100, 100, 100, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ])

# # Mostrar la matriz como una imagen
# plt.imshow(matriz_mario, cmap='gray')
# plt.show()
