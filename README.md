# Sistema de Archivos Distribuido — Mini proyecto (Python)

[![Estado](https://img.shields.io/badge/status-experimental-yellow.svg)](https://github.com)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

Una implementación mínima y educativa de un sistema de intercambio de archivos distribuido. Ideal para aprender los conceptos básicos: servidor HTTP con FastAPI, cliente CLI y sincronización simple de archivos.

## Contenido del repositorio

- `server.py` — Servidor FastAPI que acepta subidas, lista archivos, sirve descargas y permite borrado. Usa el header `X-API-KEY` para autenticación básica.
- `client.py` — Cliente CLI (usa `requests`) para interactuar con el servidor. Comandos comunes: `list`, `upload`, `download`, `sync`.
- `server_storage/` — Carpeta donde el servidor guarda los archivos subidos.
- `client_storage/` — Ejemplo de carpeta local usada por el cliente.

---


## Requisitos

- Python 3.8 o superior
- Paquetes: FastAPI, uvicorn, requests, python-multipart (para subidas multipart)

Si existe `requirements.txt`, instálalo; si no, las dependencias mínimas pueden instalarse así (PowerShell):

```powershell

# Crear y activar virtualenv (PowerShell)

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt

```

En macOS/Linux:

```bash

python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

```

---

## Uso rápido (PowerShell)

1) Arrancar el servidor en modo desarrollo:

```powershell
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

2) Ejemplos de uso del cliente:

- Listar archivos en el servidor:

```powershell
python client.py list --base http://localhost:8000
```

- Subir un archivo:

```powershell
python client.py upload --path .\client_storage\archivo_ejemplo.pdf --base http://localhost:8000
```

- Descargar un archivo:

```powershell
python client.py download --filename archivo_ejemplo.pdf --path .\client_storage --base http://localhost:8000
```

- Sincronizar una carpeta local con el servidor:

```powershell
python client.py sync --path .\client_storage --base http://localhost:8000
```

Si el cliente acepta `--api-key`, añade `--api-key devkey` (si tu servidor usa `devkey` como clave de desarrollo).

---

## Endpoints comunes (referencia)

Los endpoints dependen de la implementación en `server.py`; típicamente:

- GET /files — lista archivos
- POST /upload — sube un archivo (multipart/form-data)
- GET /download/{filename} — descarga de archivo
- DELETE /files/{filename} — elimina archivo

Ejemplo PowerShell para listar archivos con header de API key:

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/files" -Headers @{"X-API-KEY"="devkey"}
```

Para descargar un archivo:

```powershell
Invoke-WebRequest -Uri "http://localhost:8000/download/archivo.pdf" -OutFile .\client_storage\archivo.pdf -Headers @{"X-API-KEY"="devkey"}
```

---

## Buenas prácticas y seguridad

- No uses la clave `devkey` en producción. Gestiona secretos (Azure Key Vault, AWS Secrets Manager, HashiCorp Vault, etc.).
- Usa HTTPS (TLS) para todas las comunicaciones.
- Limita el tamaño máximo de archivos y aplica políticas de validación de tipos.
- Escanea los ficheros subidos con un antivirus antes de servirlos a otros usuarios.
- Añade control de acceso y registro/auditoría (quién sube/descarga/borra).

---

## Desarrollo y pruebas

- Ejecuta el servidor con `uvicorn` y usa `--reload` para desarrollo.
- Añade tests unitarios e integración para upload/download/sync.

Chequeo rápido de salud (PowerShell):

```powershell
$r = Invoke-RestMethod -Uri "http://localhost:8000/files" -Method GET -Headers @{"X-API-KEY"="devkey"}
Write-Host $r
```

Si `GET /files` no está disponible, adapta la ruta según tu `server.py`.

---

## Contribuir

1. Haz fork del repositorio.
2. Crea una rama: `feature/descripcion` o `fix/descripcion`.
3. Añade tests y documentación.
4. Abre un Pull Request con una descripción clara.

Muchas gracias por contribuir — incluso pequeños parches son bienvenidos.

---

## Ideas de mejora

- Autenticación por usuario (JWT) y control de roles.
- Versionado de archivos y resolución de conflictos en sincronización.
- Persistencia de metadatos en base de datos y ficheros en S3 u object storage.
- Interfaz web o dashboard para administración y visualización.

---

## Licencia

Proyecto bajo licencia MIT. Consulta `LICENSE` para detalles.

---

## Contacto

Abre un issue o contacta al mantenedor del repositorio para dudas o propuestas.

---
