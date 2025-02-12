# Documentador de código en Markdown

Este script en Python genera un archivo Markdown (`*.md`) que documenta la estructura de un proyecto, incluyendo la jerarquía de directorios, los docstrings/comentarios iniciales de los archivos y el código fuente.

## Características

- **Estructura de Directorios**: Genera una lista jerárquica de carpetas y archivos en formato Markdown.
- **Docstrings/Comentarios**: Extrae y añade los docstrings o comentarios iniciales de los archivos soportados (`.py`, `.js`, `.php`, `.css`, `.html`).
- **Código Fuente**: Incluye el contenido de los archivos dentro de bloques de código en Markdown.
- **Interfaz Gráfica**: Utiliza una interfaz gráfica (GUI) para seleccionar la carpeta de origen y el archivo de salida.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `tkinter`
  - `ttkbootstrap`

## Uso

1. Ejecuta el script `generador_markdown.py`.
2. Selecciona la carpeta del proyecto que deseas documentar.
3. Especifica la ruta y nombre del archivo Markdown de salida.
4. Haz clic en "Iniciar Proceso" para generar el documento.

## Ejemplo de Salida

El archivo generado incluirá:

- **Estructura del Proyecto**: Lista de carpetas y archivos.
- **Documentación de Archivos**: Docstrings o comentarios extraídos.
- **Código de Archivos**: Contenido de los archivos en bloques de código.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes alguna mejora, no dudes en abrir un issue o enviar un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.