from flask import Flask, render_template, request, send_file
import os
import shutil
from chocolate import procesar

app = Flask(__name__, static_folder='../', template_folder='../')

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'

# Crear las carpetas si no existen
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'folder' not in request.files:
        return "No se ha subido ninguna carpeta.", 400

    # Obtener la lista de archivos subidos
    files = request.files.getlist('folder')
    if not files or all(file.filename == '' for file in files):
        return "No se ha seleccionado ningún archivo.", 400

    # Crear una carpeta temporal para los archivos subidos
    temp_folder = os.path.join(UPLOAD_FOLDER, 'temp')
    os.makedirs(temp_folder, exist_ok=True)

    # Guardar los archivos subidos manteniendo la estructura de directorios
    for file in files:
        # Obtener la ruta relativa del archivo dentro de la carpeta
        file_path = os.path.join(temp_folder, file.filename)
        
        # Crear directorios necesarios
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Guardar el archivo
        file.save(file_path)
        print(f"Archivo guardado: {file_path}")  # Depuración

    # Procesar los archivos subidos
    output_md = os.path.join(OUTPUT_FOLDER, 'output.md')
    try:
        procesar(temp_folder, output_md)
    except FileNotFoundError as e:
        return f"Error: No se encontró el archivo {e.filename}.", 400
    except Exception as e:
        return f"Error al procesar la carpeta: {e}", 500

    # Enviar el archivo generado para descargar
    return send_file(output_md, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)