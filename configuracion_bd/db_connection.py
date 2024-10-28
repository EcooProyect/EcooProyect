import psycopg2

def connect_db():
    try:
        connection = psycopg2.connect(
            dbname="energy_saver_db",
            user="postgres",
            password="12345",
            host="localhost",
            port="5432"
        )
        print("Conexión exitosa a la base de datos")
        return connection
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

# Conectar y probar
conn = connect_db()
if conn:
    conn.close()
