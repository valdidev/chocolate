from flask import Flask, render_template, request, send_file
import os
import shutil
from chocolate import procesar

app = Flask(__name__, static_folder='../', template_folder='../')

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'folder' not in request.files:
        return "No se ha subido ninguna carpeta.", 400

    folder = request.files.getlist('folder')[0]
    if folder.filename == '':
        return "No se ha seleccionado ningún archivo.", 400

    # Guardar la carpeta subida
    folder_path = os.path.join(UPLOAD_FOLDER, folder.filename)
    folder.save(folder_path)

    # Extraer la carpeta si es un zip
    if folder.filename.endswith('.zip'):
        shutil.unpack_archive(folder_path, UPLOAD_FOLDER)
        folder_name = folder.filename[:-4]  # Eliminar la extensión .zip
    else:
        folder_name = folder.filename

    # Ruta completa de la carpeta
    full_folder_path = os.path.join(UPLOAD_FOLDER, folder_name)

    # Generar el archivo Markdown
    output_md = os.path.join(OUTPUT_FOLDER, 'output.md')
    procesar(full_folder_path, output_md)

    # Enviar el archivo generado para descargar
    return send_file(output_md, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)