import os

# Define una función para encontrar todas las carpetas que contienen archivos .git
def find_git_directories(root_dir):
    git_dirs = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '.git' in dirnames:
            git_dirs.append(dirpath)
    return git_dirs

# Llama a la función para encontrar todas las carpetas que contienen archivos .git en el disco local C
git_dirs = find_git_directories("C:\\\\")

# Imprime las carpetas
for dir in git_dirs:
    print(dir)
