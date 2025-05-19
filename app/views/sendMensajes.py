from flask import Flask,Blueprint
import webbrowser
import pyautogui
import time

sendMensajes_bp = Blueprint('sendMensajes', __name__)

@sendMensajes_bp.route('/sendData/', methods=["POST"])
def prueba():
    webbrowser.open("https://web.whatsapp.com/send?phone=50230108703&text=Hola_kevin")
    
    time.sleep(7)
    
    pyautogui.press('enter')
    
    time.sleep(2)
    pyautogui.press('ctrl', 'w')
    
    
    
    return "listo"
    