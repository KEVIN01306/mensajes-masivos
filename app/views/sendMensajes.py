from flask import Flask, Blueprint, request
import webbrowser
import pyautogui
import time
import json
from urllib.parse import quote_plus

sendMensajes_bp = Blueprint('sendMensajes', __name__)

@sendMensajes_bp.route('/sendData/', methods=["POST"])
def prueba():
    if request.is_json:
        data = request.get_json()
        
        
        mensajes_recibidos,excel_data,columna_numeros,codigo_pais,tiempo_llegada,tiempo_envio = recepcion(data)
        
        mensaje_index = 0

        for row_data in excel_data:
            try:
                phone_number = row_data.get(columna_numeros) 

                if phone_number is None:
                    print(f"Saltando fila: No se encontró número en la columna '{columna_numeros}' para: {row_data}")
                    continue 
                phone_number = str(phone_number)
                    
                phone_number = codigo_pais + phone_number 

                current_message = mensajes_recibidos[mensaje_index].replace('\n', """
""").strip()

                    
                encoded_message = quote_plus(transformarSintaxis(row_data,current_message)) 
                

                whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_number}&text={encoded_message}"
                
                print(f"Abriendo WhatsApp para: {phone_number} con mensaje: {current_message[:30]}...") 
                webbrowser.open(whatsapp_url)
                
                time.sleep(tiempo_llegada) 
                
                pyautogui.press('enter') 
                time.sleep(tiempo_envio) 
                
                pyautogui.hotkey('ctrl', 'w')
                pyautogui.press('enter') 
                

                mensaje_index = (mensaje_index + 1) % len(mensajes_recibidos)
                

            except Exception as e:
                print(f"Error procesando el número {phone_number if 'phone_number' in locals() else 'desconocido'}: {e}")

        return "Mensajes procesados y enviados."
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
        if isinstance(excel_data, dict) and 'hoja1' in excel_data and isinstance(excel_data['hoja1'], list):
            excel_data = excel_data['hoja1']
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