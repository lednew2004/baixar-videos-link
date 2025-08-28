from flask import Flask, request, send_file, render_template
import yt_dlp
import tempfile
import os
import uuid
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    filename = None
    error = None
    loading_img = None

    # Busca imagens disponíveis na pasta static/imgs/
    img_folder = os.path.join(app.static_folder, 'imgs')
    img_files = [
        f for f in os.listdir(img_folder)
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
    ]
    if img_files:
        loading_img = f"imgs/{random.choice(img_files)}"  # Caminho relativo à pasta static/

    if request.method == 'POST':
        url = request.form['url']
        temp_dir = tempfile.gettempdir()
        safe_name = f"{uuid.uuid4().hex}.mp4"
        full_path = os.path.join(temp_dir, safe_name)

        ydl_opts = {
            'outtmpl': full_path,
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'quiet': True,
            'cookiefile': 'cookies.txt',  # Suporte a vídeos privados/login
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                filename = os.path.basename(full_path)
        except Exception as e:
            error = str(e)

    return render_template('index.html', filename=filename, error=error, loading_img=loading_img)

@app.route('/download/<filename>')
def download(filename):
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return "❌ Arquivo não encontrado", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
