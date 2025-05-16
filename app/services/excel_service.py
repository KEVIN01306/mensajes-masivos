import pandas as pd
from io import BytesIO
import os
from werkzeug.utils import secure_filename
from datetime import datetime

def procesar_archivo_excel(file_storage):
    """Procesa el archivo Excel subido y retorna un mensaje de estado."""
    try:
        # Leer el archivo en memoria
        in_memory_file = BytesIO(file_storage.read())

        # Leer todas las hojas si quieres
        excel = pd.read_excel(in_memory_file, sheet_name=None)

        resumen = []
        for nombre_hoja, df in excel.items():
            resumen.append(f"Hoja '{nombre_hoja}' con {len(df)} filas y {len(df.columns)} columnas")

            # Aquí podrías hacer validaciones por hoja
            # validar_datos_hoja(df)  # función extra si lo deseas

        return "Archivo leído correctamente: " + " | ".join(resumen)

    except Exception as e:
        raise ValueError(f"Error leyendo Excel: {str(e)}")


UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploaded_excels')

def guardar_archivo_local(file_storage):
    """Guarda el archivo Excel en una carpeta local y devuelve su ruta."""
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    nombre_seguro = secure_filename(file_storage.filename)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_final = f"{timestamp}_{nombre_seguro}"

    ruta_completa = os.path.join(UPLOAD_FOLDER, nombre_final)
    file_storage.save(ruta_completa)

    return ruta_completa