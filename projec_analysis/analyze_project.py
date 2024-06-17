import os

def es_directorio_de_git_o_virtual(directorio):
    """
    Función para determinar si un directorio pertenece a Git o es un entorno virtual de Python.
    """
    git_folders = ['.git']
    git_subfolders = ['.git/hooks', '.git/info', '.git/logs', '.git/objects', '.git/refs']
    virtual_folders = ['.venv', 'venv', '.env', 'env']

    # Comprobar si el directorio actual pertenece a Git
    if any(folder.lower() in directorio.lower() for folder in git_folders):
        return True

    # Comprobar si el directorio es una subcarpeta de un directorio de Git
    for subfolder in git_subfolders:
        if directorio.lower().startswith(os.path.normcase(subfolder.lower())):
            return True

    # Comprobar si el directorio actual es un entorno virtual de Python
    if any(folder.lower() in directorio.lower() for folder in virtual_folders):
        return True

    return False

def analizar_directorio(directorio):
    for root, dirs, files in os.walk(directorio):
        if es_directorio_de_git_o_virtual(root):
            continue  # Saltar directorios que pertenecen a Git o son entornos virtuales

        carpeta_rel = os.path.relpath(root, directorio)
        if carpeta_rel == ".":
            carpeta_rel = os.path.basename(directorio)

        # Verificar si la carpeta es una carpeta especial
        mostrar_archivos = True
        for carpeta_especial in ["static", "templates"]:
            if carpeta_especial.lower() in carpeta_rel.lower():
                mostrar_archivos = False
                break

        print(f"{carpeta_rel}:")

        if mostrar_archivos:
            for archivo in files:
                print(f"    {archivo}")
        else:
            print("    (archivos omitidos)")

if __name__ == "__main__":
    # Obtener el directorio actual
    directorio_actual = os.getcwd()
    analizar_directorio(directorio_actual)