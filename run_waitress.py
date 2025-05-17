from app.run import app
from waitress import serve

if __name__ == '__main__':
    print("Iniciando el servidor de desarrollo de Flask con modo debug activado...")
    app.run(debug=True, port=5001)

#if __name__ == '__main__':
#    print("Intentando iniciar el servidor Waitress...")
#    try:
#        print("Servidor Waitress iniciado en http://localhost:5001")
#        serve(app, port=5001)
#    except Exception as e:
#        print(f"Ocurrió un error al iniciar el servidor: {e}")