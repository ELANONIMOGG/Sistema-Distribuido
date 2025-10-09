from fastapi import FastAPI, UploadFile, File, HTTPException, Header
from fastapi.responses import FileResponse
import os, sqlite3, time
from typing import Optional

STORAGE_DIR = os.path.join(os.path.dirname(__file__), "server_storage")
DB_PATH = os.path.join(os.path.dirname(__file__), "files.db")
API_KEY = "devkey"

app = FastAPI(title="Mini Distributed File Server")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS files ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "filename TEXT UNIQUE,"
        "uploaded_at REAL"
        ")"
    )
    conn.commit()
    conn.close()

def require_key(x_api_key: Optional[str]):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

@app.on_event("startup")
def startup():
    os.makedirs(STORAGE_DIR, exist_ok=True)
    init_db()

@app.post("/upload")
async def upload(file: UploadFile = File(...), x_api_key: Optional[str] = Header(None)):
    require_key(x_api_key)
    dest_path = os.path.join(STORAGE_DIR, file.filename)
    # write file
    with open(dest_path, "wb") as f:
        content = await file.read()
        f.write(content)
    # update db
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO files (filename, uploaded_at) VALUES (?, ?)",
                (file.filename, time.time()))
    conn.commit()
    conn.close()
    return {"filename": file.filename, "size": len(content)}

@app.get("/files")
def list_files(x_api_key: Optional[str] = Header(None)):
    require_key(x_api_key)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT filename, uploaded_at FROM files ORDER BY uploaded_at DESC")
    rows = cur.fetchall()
    conn.close()
    return [{"filename": r[0], "uploaded_at": r[1]} for r in rows]

@app.get("/download/{filename}")
def download(filename: str, x_api_key: Optional[str] = Header(None)):
    require_key(x_api_key)
    path = os.path.join(STORAGE_DIR, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(path, filename=filename)

@app.delete("/delete/{filename}")
def delete_file(filename: str, x_api_key: Optional[str] = Header(None)):
    require_key(x_api_key)
    path = os.path.join(STORAGE_DIR, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")
    os.remove(path)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM files WHERE filename = ?", (filename,))
    conn.commit()
    conn.close()
    return {"deleted": filename}

@app.get("/health")
def health():
    return {"status": "ok"}

