import sqlite3

def crear_base_datos(conn):
    cursor = conn.cursor()

    try:
        # Crear la tabla clientes si no existe
        cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                        id INTEGER PRIMARY KEY,
                        nombre TEXT NOT NULL,
                        apellido TEXT NOT NULL,
                        email TEXT NOT NULL)''')

        # Guardar los cambios
        conn.commit()

        print("Base de datos y tabla creadas correctamente.")
    except sqlite3.Error as e:
        print("Error al crear la base de datos y la tabla:", e)
    finally:
        cursor.close()

def insertar_cliente(conn, nombre, apellido, email):
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO clientes (nombre, apellido, email) VALUES (?, ?, ?)', (nombre, apellido, email))
        conn.commit()
        print("Cliente insertado correctamente.")
    except sqlite3.Error as e:
        print("Error al insertar cliente:", e)
    finally:
        cursor.close()

def mostrar_clientes(conn):
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM clientes')
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print("Error al mostrar clientes:", e)
        return []
    finally:
        cursor.close()

# Sección principal del código
try:
    # Conexión a la base de datos (se creará si no existe)
    conn = sqlite3.connect('base_de_datos.db')

    # Crear la base de datos y la tabla si no existen
    crear_base_datos(conn)

    # Insertar algunos datos de ejemplo
    insertar_cliente(conn, 'Juan', 'Perez', 'juan@example.com')
    insertar_cliente(conn, 'María', 'González', 'maria@example.com')

    # Mostrar los clientes
    clientes = mostrar_clientes(conn)
    if clientes:
        print("Clientes:")
        for cliente in clientes:
            print(cliente)
    else:
        print("No se pudieron mostrar los clientes.")
except Exception as e:
    print("Error en la sección principal del código:", e)
finally:
    conn.close()
