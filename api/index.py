from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI(title="Meu Portfólio")

templates = Jinja2Templates(directory="../templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/static/{file_path:path}")
async def serve_static(file_path: str):
    static_path = f"../static/{file_path}"
    if os.path.exists(static_path):
        return FileResponse(static_path)
    return {"error": "File not found"}, 404

def handler(request, response):
    import asyncio
    
    async def handle_request():
        path = request.path
        method = request.method
        
        if path.startswith("/static/"):
            file_path = path.replace("/static/", "")
            static_file = f"../static/{file_path}"
            if os.path.exists(static_file):
                with open(static_file, 'rb') as f:
                    content = f.read()
                return response(content, 200, {'Content-Type': 'text/css' if path.endswith('.css') else 'text/javascript' if path.endswith('.js') else 'image/jpeg'})
            else:
                return response("File not found", 404)
        
        else:
            try:
                with open("../templates/index.html", "r", encoding="utf-8") as f:
                    html_content = f.read()
                return response(html_content, 200, {'Content-Type': 'text/html'})
            except Exception as e:
                return response(f"Error: {str(e)}", 500)
    
    return asyncio.run(handle_request())