![Banner](https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=1400&auto=format&fit=crop&ixlib=rb-4.0.3&s=8a0f2a0e7d2ab0b7b5a0f8b5c6d6e4a7)

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

## Arquitectura (visión rápida)

El flujo es simple:

1. El cliente envía peticiones HTTP al servidor (lista, sube, descarga, elimina).
2. El servidor guarda los ficheros en `server_storage/` y devuelve metadatos JSON.

```mermaid
flowchart LR
  Cliente[Cliente CLI]
  Servidor[Servidor FastAPI]
  Storage[server_storage]
  Cliente -->|HTTP (upload/list/download/sync)| Servidor
  Servidor -->|lectura/escritura| Storage
```

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
pip install fastapi uvicorn requests python-multipart
```

En macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install fastapi uvicorn requests python-multipart
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

Gracias por revisar este mini-proyecto. Es perfecto para experimentar con conceptos distribuidos y gestión básica de archivos en red.

# Mini Distributed File System (Python)

This repository contains a simple distributed file-sharing system implemented in Python.

## Components
- `server.py`: FastAPI server that accepts file uploads, lists files, serves downloads, and deletes files. Uses a simple API key header `X-API-KEY` for auth.
- `client.py`: CLI client (uses `requests`) to interact with the server. Commands: `list`, `upload`, `download`, `sync`.
- `server_storage/`: Where server stores uploaded files.
- `client_storage/`: Example local folder for client operations.

## Quick start (local)
1. Create a virtual environment:
   ```bash
  <!--- Proyecto: Mini Distributed File System (Python) --->

  # Sistema de Archivos Distribuido — Mini proyecto (Python)

  [![Estado](https://img.shields.io/badge/status-experimental-yellow.svg)](https://github.com)
  [![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org)
  [![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

  Una implementación mínima y educativa de un sistema de intercambio de archivos distribuido. Es ideal para aprender conceptos básicos: servidor HTTP con FastAPI, cliente CLI, y sincronización simple de archivos.

  ## Contenido del repositorio

  - `server.py` — servidor FastAPI que acepta subidas, lista archivos, sirve descargas y permite borrado. Usa un encabezado `X-API-KEY` simple para autenticación.
  - `client.py` — cliente CLI (usa `requests`) para interactuar con el servidor. Comandos: `list`, `upload`, `download`, `sync`.
  - `server_storage/` — carpeta donde el servidor guarda los archivos subidos.
  - `client_storage/` — ejemplo de carpeta local usada por el cliente.

  ---

  ## Arquitectura (visión rápida)

  El flujo es simple:

  1. El cliente envía peticiones HTTP al servidor (lista, sube, descarga, elimina).
  2. El servidor guarda los ficheros en `server_storage/` y devuelve metadatos JSON.

  ```mermaid 
  flowchart LR
    Cliente[Cliente CLI]
    Servidor[Servidor FastAPI]
    Storage[server_storage]
    Cliente -->|HTTP (upload/list/download/sync)| Servidor
    Servidor -->|lectura/escritura| Storage
  ```

  ---

  ## Requisitos

  - Python 3.8 o superior
  - Dependencias en `requirements.txt` (FastAPI, uvicorn, requests, etc.)

  Si no existe `requirements.txt`, instala las dependencias mínimas:

  ```powershell
  # Crear y activar virtualenv (PowerShell)
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  pip install --upgrade pip
  pip install -r requirements.txt
  
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

  ## Arquitectura (visión rápida)

  ```mermaid
  flowchart LR
    Cliente[Cliente CLI]
    Servidor[Servidor FastAPI]
    Storage[server_storage]
    Cliente -->|HTTP (upload/list/download/sync)| Servidor
    Servidor -->|lectura/escritura| Storage
  ```

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
  pip install fastapi uvicorn requests python-multipart
  ```

  En macOS/Linux:

  ```bash
  python -m venv .venv
  source .venv/bin/activate
  pip install --upgrade pip
  pip install fastapi uvicorn requests python-multipart
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

  Gracias por revisar este mini-proyecto. Es perfecto para experimentar con conceptos distribuidos y gestión básica de archivos en red.

  Los endpoints dependen de la implementación en `server.py`. Tipo de endpoints típicos:

  - GET /files — lista archivos
  - POST /upload — sube un archivo (multipart/form-data)
  - GET /download/{filename} — descarga
  - DELETE /files/{filename} — elimina

  Ejemplo con PowerShell (descarga con header API key):

  ```powershell
  Invoke-RestMethod -Uri "http://localhost:8000/files" -Headers @{"X-API-KEY"="devkey"}
  # o para descargar: Invoke-WebRequest -Uri "http://localhost:8000/download/archivo.pdf" -OutFile .\client_storage\archivo.pdf -Headers @{"X-API-KEY"="devkey"}
  ```

  ---

  ## Buenas prácticas y seguridad

  - No uses la API key incrustada `devkey` en producción. Sustituye por secretos gestionados o JWT.
  - Expon el servidor solo sobre HTTPS (añade un reverse proxy o usa ALB/Cloud provider).
  - Implementa control de acceso, límites de tamaño de subida, escaneo antivirus y registro (auditoría).

  ---

  ## Desarrollo y pruebas

  - Para desarrollar, activa el virtualenv y arranca `uvicorn` con `--reload`.
  - Añade tests unitarios y casos de integración para las operaciones críticas (upload/download/sync).

  Ejemplo rápido para comprobar que el servidor responde:

  ```powershell
  $r = Invoke-RestMethod -Uri "http://localhost:8000/health" -Method GET -Headers @{"X-API-KEY"="devkey"}
  Write-Host $r
  ```

  Si no existe `/health`, prueba `GET /files` como sanidad básica.

  ---

  ## Contribuir

  1. Haz fork del repositorio.
  2. Crea una rama con una descripción clara: `feature/mi-cambio`.
  3. Añade tests cuando sea posible.
  4. Abre un Pull Request con la explicación del cambio y capturas/ejemplos.

  ---

  ## Ideas de mejora

  - Integrar autenticación por usuario (JWT) y roles.
  - Añadir versionado de archivos y resolución de conflictos en sincronización.
  - Persistencia en base de datos para metadatos y uso de S3/Object Storage para ficheros.
  - Interfaz web o Dashboard para administración.

  ---

  ## Licencia

  Este proyecto usa la licencia MIT — revisa `LICENSE` para más detalles.

  ---

  ## Contacto

  Si tienes dudas o quieres colaborar, abre un issue o contacta al mantenedor del repositorio.

  Gracias por revisar este mini-proyecto — ideal para experimentar con conceptos distribuidos y gestionar archivos en redes.

