from flask import Flask, Blueprint, request,jsonify
import webbrowser
import pyautogui
import time
import json
from urllib.parse import quote_plus
import threading

sendMensajes_bp = Blueprint('sendMensajes', __name__)


enviando = False  # Para controlar el envío
resultados = []   # Para almacenar filas con ✅ o ❌
lock = threading.Lock() 

@sendMensajes_bp.route('/stopSending/', methods=["POST"])
def stop_sending():
    global enviando
    with lock:
        enviando = False
    return {"status": "stopped", "resultados": resultados}

@sendMensajes_bp.route('/sendData/', methods=["POST"])
def prueba():
    global enviando, resultados
    with lock:
        enviando = True
        resultados = []

    if request.is_json:
        data = request.get_json()
        mensajes_recibidos, excel_data, columna_numeros, codigo_pais, tiempo_llegada, tiempo_envio = recepcion(data)

        mensaje_index = 0

        for row_data in excel_data:
            with lock:
                if not enviando:
                    print("❗ Envío detenido por el usuario.")
                    break

            resultado = row_data.copy()  # Creamos una copia por si queremos mantener original limpio

            try:
                phone_number = resultado.get(columna_numeros)

                if not phone_number:
                    resultado["estado"] = "❌"
                    resultados.append(resultado)
                    continue

                phone_number = str(phone_number)
                phone_number = codigo_pais + phone_number

                current_message = mensajes_recibidos[mensaje_index].replace('\n', "\n").strip()
                encoded_message = quote_plus(transformarSintaxis(resultado, current_message))

                whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_number}&text={encoded_message}"
                webbrowser.open(whatsapp_url)

                time.sleep(tiempo_llegada)
                pyautogui.press('enter')
                time.sleep(tiempo_envio)

                pyautogui.hotkey('ctrl', 'w')
                pyautogui.press('enter')

                resultado["estado"] = "✅"
                resultados.append(resultado)

                mensaje_index = (mensaje_index + 1) % len(mensajes_recibidos)

            except Exception as e:
                resultado["estado"] = "❌"
                resultados.append(resultado)
                print(f"Error procesando número: {e}")

        return jsonify(resultados)
    else:
        return "Error: La petición debe ser de tipo JSON", 400

    
    
def transformarSintaxis(row_data,current_message):
    for key, value in row_data.items():
        placeholder = f"<{{{{ {key} }}}}>"
        current_message = current_message.replace(placeholder, str(value))
    return current_message

def recepcion(data):
    mensajes_recibidos_str = data.get('mensajes', '[]')
    excel_data_str = data.get('data', '[]')
    columna_numeros = "numeros"
    codigo_pais = data.get('codigo')
    tiempo_llegada = int(data.get('Tllegada'))
    tiempo_envio = int(data.get('Tenvio'))

    try:
        mensajes_recibidos = json.loads(mensajes_recibidos_str)
        if not isinstance(mensajes_recibidos, list):
            print("Error: 'mensajes' no es una lista válida.")
            return "Error en el formato de los mensajes", 400

        excel_data = json.loads(excel_data_str)
        if isinstance(excel_data, dict):
            first_sheet_name = next(iter(excel_data))

            if isinstance(excel_data[first_sheet_name], list):
                excel_data = excel_data[first_sheet_name]
                print(f"Se ha procesado la primera hoja '{first_sheet_name}'.")
                print(excel_data)
            else:
                print(f"El contenido de la primera hoja '{first_sheet_name}' no es una lista.")
        else:
            print("Error: El formato de 'excel_data' no es el esperado o falta 'hoja1'.")
            return "Error en el formato de los datos de Excel", 400

    except json.JSONDecodeError as e:
        print(f"Error decodificando JSON (mensajes o excel_data): {e}")
        return "Error en el formato de los datos", 400

    print(f"Mensajes recibidos (como lista): {mensajes_recibidos}")
    print(f"Datos de Excel recibidos: {excel_data}")
    print(f"Columna de números seleccionada: {columna_numeros}")
    print(f"Codigo de pais : {codigo_pais}")
    print("Tiempos", tiempo_llegada, tiempo_envio)

    

    if not mensajes_recibidos:
        print("Error: No hay mensajes configurados para enviar.")
        return "Error: No hay mensajes configurados para enviar.", 400
    
    return mensajes_recibidos,excel_data,columna_numeros,codigo_pais,tiempo_llegada,tiempo_envio