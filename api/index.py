from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

# Configuração do app
app = FastAPI(title="Meu Portfólio")

# Configura templates e arquivos estáticos
templates = Jinja2Templates(directory="templates")

# Serve arquivos estáticos (CSS, JS, Images)
@app.get("/static/{file_path:path}")
async def serve_static(file_path: str):
    static_file = os.path.join("static", file_path)
    if os.path.exists(static_file):
        return FileResponse(static_file)
    return {"error": "File not found"}

# Página principal
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Rotas para SPA (Single Page Application)
@app.get("/sobre", response_class=HTMLResponse)
async def sobre(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/projetos", response_class=HTMLResponse)
async def projetos(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/contato", response_class=HTMLResponse)
async def contato(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Handler para Vercel
async def handler(request, response):
    try:
        path = request.path
        method = request.method
        
        # Serve a página principal para todas as rotas
        if method == "GET":
            if path.startswith("/static/"):
                # Serve arquivos estáticos
                file_path = path.replace("/static/", "")
                static_file = os.path.join("static", file_path)
                if os.path.exists(static_file):
                    with open(static_file, 'rb') as f:
                        content = f.read()
                    return response(content, 200)
                else:
                    return response("Not found", 404)
            else:
                # Serve HTML principal
                with open("templates/index.html", "r", encoding="utf-8") as f:
                    html_content = f.read()
                return response(html_content, 200, {"Content-Type": "text/html"})
        
        return response("Method not allowed", 405)
    
    except Exception as e:
        return response(f"Error: {str(e)}", 500)