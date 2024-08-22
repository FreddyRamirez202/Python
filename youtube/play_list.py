import ffmpeg
import os

def convertir_mp4_a_mkv(input_file, output_file):
    try:
        (
            ffmpeg
            .input(input_file)
            .output(output_file, **{'c:v': 'copy', 'c:a': 'copy'})
            .run(overwrite_output=True)
        )
        print(f"Conversión exitosa: {input_file} a {output_file}")
    except ffmpeg.Error as e:
        print(f"Error al convertir el archivo: {e}")

# Ruta de la carpeta donde están los videos
ruta_videos = r'C:\Users\ADM19\Desktop\videos'

# Lista de nombres de los videos
videos = [
    'El agujero negro mágico',
    'Super Bebés',
    'El Show de Pocoyó Circo Espacial',
    'Pocoyó y La Liga De Los Súper Amigos'
]

# Convertir cada video de .mp4 a .mkv
for video in videos:
    input_file = os.path.join(ruta_videos, f'{video}.mp4')
    output_file = os.path.join(ruta_videos, f'{video}.mkv')
    convertir_mp4_a_mkv(input_file, output_file)
