import os

def handler(request, response):
    path = request.path
    
    # Serve arquivos estáticos (CSS, JS, imagens)
    if path.startswith('/static/'):
        file_path = path[8:]  # Remove '/static/'
        static_file = f'../static/{file_path}'
        
        try:
            with open(static_file, 'rb') as f:
                file_content = f.read()
            
            # Define o tipo de conteúdo
            content_type = 'text/css' if path.endswith('.css') else \
                          'application/javascript' if path.endswith('.js') else \
                          'image/jpeg' if path.endswith('.jpg') else \
                          'image/png' if path.endswith('.png') else \
                          'text/html'
            
            return response(file_content, 200, {'Content-Type': content_type})
        except FileNotFoundError:
            return response('File not found', 404)
        except Exception as e:
            return response(f'Error: {str(e)}', 500)
    
    # Serve a página principal
    else:
        try:
            with open('../templates/index.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            return response(html_content, 200, {'Content-Type': 'text/html'})
        except Exception as e:
            return response(f'Error loading page: {str(e)}', 500)