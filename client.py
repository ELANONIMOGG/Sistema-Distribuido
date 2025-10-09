#!/usr/bin/env python3
import requests, os, argparse, sys, time
import subprocess

API_KEY = "devkey"
DEFAULT_BASE = "http://localhost:8000"

def list_files(base):
    r = requests.get(f"{base}/files", headers={"X-API-KEY": API_KEY})
    r.raise_for_status()
    for f in r.json():
        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(f["uploaded_at"]))
        print(f"{f['filename']}\t{ts}")

def upload_file(base, path):
    fname = os.path.basename(path)
    with open(path, "rb") as fh:
        files = {"file": (fname, fh)}
        r = requests.post(f"{base}/upload", files=files, headers={"X-API-KEY": API_KEY})
    r.raise_for_status()
    print("Uploaded:", r.json())

def download_file(base, filename, dest_dir):
    r = requests.get(f"{base}/download/{filename}", headers={"X-API-KEY": API_KEY}, stream=True)
    if r.status_code == 404:
        print("Not found on server")
        return
    r.raise_for_status()
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, filename)
    with open(dest, "wb") as fh:
        for chunk in r.iter_content(4096):
            fh.write(chunk)
    print("Downloaded:", dest)

def sync(base, local_dir):
    r = requests.get(f"{base}/files", headers={"X-API-KEY": API_KEY})
    r.raise_for_status()
    server_files = {f["filename"] for f in r.json()}
    local_files = {f for f in os.listdir(local_dir) if os.path.isfile(os.path.join(local_dir, f))}
    to_upload = local_files - server_files
    to_download = server_files - local_files 
    for f in to_upload:
        print("Uploading", f)
        upload_file(base, os.path.join(local_dir, f))
    for f in to_download:
        print("Downloading", f)
        download_file(base, f, local_dir)
    print("Sync complete.")

def delete_file(base, filename):
    r = requests.delete(f"{base}/delete/{filename}", headers={"X-API-KEY": API_KEY})
    if r.status_code == 404:
        print("File not found on server")
        return
    elif r.status_code == 401:
        print("Unauthorized: Invalid API key")
        return
    elif r.status_code == 200:
        print("File deleted on server")
        return
    r.raise_for_status()
    print("Deleted:", filename)

def main():
    parser = argparse.ArgumentParser(description="Client for Mini Distributed File Server")
    parser.add_argument("command", choices=["list","upload","download","sync","delete"])
    parser.add_argument("--base", default=DEFAULT_BASE, help="Server base URL")
    parser.add_argument("--path", help="Path for upload or local directory for sync/download")
    parser.add_argument("--filename", help="Filename for download")
    args = parser.parse_args()
    if args.command == "list":
        list_files(args.base)
    elif args.command == "upload":
        if not args.path:
            print("Missing --path for upload")
            sys.exit(1)
        upload_file(args.base, args.path)
    elif args.command == "download":
        if not args.filename or not args.path:
            print("Need --filename and --path (dest dir)")
            sys.exit(1)
        download_file(args.base, args.filename, args.path)
    elif args.command == "sync":
        if not args.path:
            print("Need --path (local dir to sync)")
            sys.exit(1)
        sync(args.base, args.path)
    elif args.command == "delete":
        if not args.filename:
            print("Need --filename to delete")
            sys.exit(1)
        delete_file(args.base, args.filename)


if __name__ == "__main__":
    main()
