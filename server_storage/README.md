
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
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Run server:
   ```bash
   uvicorn server:app --reload --host 0.0.0.0 --port 8000
   ```

3. Use client:
   - List files:
     ```bash
     python client.py list --base http://localhost:8000
     ```
   - Upload a file:
     ```bash
     python client.py upload --path ./client_storage/example.pdf --base http://localhost:8000
     ```
   - Download a file:
     ```bash
     python client.py download --filename example.pdf --path ./client_storage --base http://localhost:8000
     ```
   - Sync local folder with server:
     ```bash
     python client.py sync --path ./client_storage --base http://localhost:8000
     ```

## Security notes
- This example uses a fixed API key `devkey` for simplicity. For any real deployment, replace it with a secure secret and use HTTPS.
- Consider adding authentication, access control, rate-limiting, and virus scanning in production.

## Next steps / extensions
- Add user accounts and per-user directories.
- Add file versioning and conflict resolution.
- Replace API key with JWT-based auth.
- Use object storage (S3) and a more robust metadata database.

