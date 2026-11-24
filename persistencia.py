import json
import os


def guardar_json(ruta_archivo, datos):
    carpeta = os.path.dirname(ruta_archivo)
    if carpeta:
        os.makedirs(carpeta, exist_ok=True)
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def cargar_json(ruta_archivo, por_defecto=None):
    if por_defecto is None:
        por_defecto = []
    if not os.path.exists(ruta_archivo):
        return por_defecto
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, OSError):
        return por_defecto