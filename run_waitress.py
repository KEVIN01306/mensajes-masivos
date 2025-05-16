from app.run import app
from waitress import serve

if __name__ == '__main__':
    print("Intentando iniciar el servidor Waitress...")
    try:
        print("Servidor Waitress iniciado en http://0.0.0.0:5001")
        serve(app, host='0.0.0.0', port=5001)
    except Exception as e:
        print(f"Ocurrió un error al iniciar el servidor: {e}")