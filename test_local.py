from flask import Flask, send_from_directory
import os

app = Flask(__name__, 
    static_folder='static',
    template_folder='templates'
)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_app(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.template_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)