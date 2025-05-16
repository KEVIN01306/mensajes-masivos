from flask import Blueprint, request, flash ,jsonify
from ..services.excel_service import procesar_archivo_excel
import pandas as pd
import numpy as np

excel_bp = Blueprint('excel_bp', __name__)

@excel_bp.route("/excel/", methods=["POST"])
def subir_excel():
    archivo = request.files.get('archivo-excel')

    if not archivo or archivo.filename == "":
        flash("El archivo debe ser .xlsx","danger")
        return jsonify({"error": "No se envió ningún archivo"}), 400

    if not archivo.filename.endswith(".xlsx"):
        flash("El archivo debe ser .xlsx","danger")
        return jsonify({"error": "El archivo debe ser .xlsx"}), 400

    try:
        archivo.seek(0) 

        mensaje = procesar_archivo_excel(archivo)

        archivo.seek(0) 
        dataframes = pd.read_excel(archivo, sheet_name=None)

        data_json = {
            sheet: df.replace({np.nan: None}).to_dict(orient="records")
            for sheet, df in dataframes.items()
        }
        flash("✅ data cargada","success")
        flash(f"📄 {mensaje}", "info")
        return jsonify({
            "mensaje": mensaje,
            "datos": data_json
        })

    except Exception as e:
        return jsonify({"error": f"Error al procesar archivo: {str(e)}"}), 500