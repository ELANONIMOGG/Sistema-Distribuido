from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from .forms import FileUploadForm

# Configuración del servidor FastAPI
FASTAPI_URL = "http://127.0.0.1:8000"
API_KEY = "devkey"

def index(request):
    """Vista principal con el formulario de subida"""
    form = FileUploadForm()
    return render(request, 'file_uploader/index.html', {'form': form})

def upload_file(request):
    """Vista para subir archivos al servidor FastAPI"""
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            
            try:
                # Preparar el archivo para enviar al servidor FastAPI
                files = {'file': (uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)}
                headers = {'X-API-KEY': API_KEY}
                
                # Enviar al servidor FastAPI
                response = requests.post(
                    f"{FASTAPI_URL}/upload",
                    files=files,
                    headers=headers
                )
                
                if response.status_code == 200:
                    messages.success(request, f'Archivo "{uploaded_file.name}" subido exitosamente.')
                else:
                    messages.error(request, f'Error al subir archivo: {response.text}')
                    
            except requests.exceptions.ConnectionError:
                messages.error(request, 'No se puede conectar al servidor. Asegúrate de que esté ejecutándose.')
            except Exception as e:
                messages.error(request, f'Error inesperado: {str(e)}')
        
        return redirect('file_uploader:index')
    
    return redirect('file_uploader:index')

def list_files(request):
    """Vista para listar archivos del servidor"""
    try:
        headers = {'X-API-KEY': API_KEY}
        response = requests.get(f"{FASTAPI_URL}/files", headers=headers)
        
        if response.status_code == 200:
            files_data = response.json()
            return render(request, 'file_uploader/file_list.html', {'files': files_data})
        else:
            messages.error(request, f'Error al obtener lista de archivos: {response.text}')
            
    except requests.exceptions.ConnectionError:
        messages.error(request, 'No se puede conectar al servidor.')
    except Exception as e:
        messages.error(request, f'Error inesperado: {str(e)}')
    
    return render(request, 'file_uploader/file_list.html', {'files': []})

def download_file(request, filename):
    """Vista para descargar archivos del servidor"""
    try:
        headers = {'X-API-KEY': API_KEY}
        response = requests.get(f"{FASTAPI_URL}/download/{filename}", headers=headers)
        
        if response.status_code == 200:
            # Crear respuesta HTTP con el archivo
            http_response = HttpResponse(
                response.content,
                content_type='application/octet-stream'
            )
            http_response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return http_response
        else:
            messages.error(request, f'Error al descargar archivo: {response.text}')
            
    except requests.exceptions.ConnectionError:
        messages.error(request, 'No se puede conectar al servidor.')
    except Exception as e:
        messages.error(request, f'Error inesperado: {str(e)}')
    
    return redirect('file_uploader:list_files')

def delete_file(request, filename):
    """Vista para eliminar archivos del servidor"""
    if request.method == 'POST':
        try:
            headers = {'X-API-KEY': API_KEY}
            response = requests.delete(f"{FASTAPI_URL}/delete/{filename}", headers=headers)
            
            if response.status_code == 200:
                messages.success(request, f'Archivo "{filename}" eliminado exitosamente.')
            else:
                messages.error(request, f'Error al eliminar archivo: {response.text}')
                
        except requests.exceptions.ConnectionError:
            messages.error(request, 'No se puede conectar al servidor.')
        except Exception as e:
            messages.error(request, f'Error inesperado: {str(e)}')
    
    return redirect('file_uploader:list_files')
