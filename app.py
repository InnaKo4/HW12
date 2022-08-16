from flask import Flask, request, render_template, send_from_directory
from functions import load_posts, get_post_by_word, change_posts
from main.views import main_blueprint
from loader.views import loader_blueprint
import logging
logging.basicConfig(filename="info.log", level=logging.INFO)
logging.basicConfig(filename="error.log", level=logging.ERROR)
POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.register_blueprint(main_blueprint)
logging.info("Главная страница загружена")
app.register_blueprint(loader_blueprint)
logging.info("Страница для загрузки поста загружена")

@app.route("/search")
def search_page():
    s = request.args['s']
    posts = get_post_by_word(s)
    return render_template('post_list.html', posts=posts, word=s)

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

@app.route("/upload", methods=["GET", "POST"])
def page_post_form():
    allowed_extensions = {'png', 'jpg', 'jpeg'}
    content = request.form["content"]
    picture = request.files.get("picture")
    filename = picture.filename
    extension = filename.split(".")[-1]
    picture.save(f"./uploads/images/{filename}")
    try:
        if extension not in allowed_extensions:
            logging.error(f"Тип файлов {extension} не поддерживается")
            return f"Тип файлов {extension} не поддерживается"
        else:
            logging.info("Файл загружен")
            return render_template("post_uploaded.html", filename=filename, content=content)
    except FileNotFoundError:
        logging.error("Ошибка при выгрузке файла")
        return "Ошибка при выгрузке файла"

@app.route("/upload", methods=["POST"])
def page_post_upload():
    pass

app.run(host='127.0.0.1', port=9000)
