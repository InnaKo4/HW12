import json
from json import JSONDecodeError


def load_posts():
    """Загружает данные из Json в Python"""
    try:
        with open("posts.json", "r") as file:
            file_json = file.read()
            all_posts = json.loads(file_json)
            return all_posts
    except FileNotFoundError:
        return "Файл не найден"
    except JSONDecodeError:
        return "Файл не удается преобразовать"
def get_post_by_word(word):
    posts = load_posts()
    all_posts = []
    for post in posts:
        if word in post['content']:
            all_posts.append(post)
    return all_posts

def change_posts(json_file):
    raw_json = json.dumps(json_file, ensure_ascii=False)
    with open("posts.json", "w") as file:
       file.write(raw_json)



