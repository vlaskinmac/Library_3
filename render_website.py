import json
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked


def rebuild():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('pages/index.html')
    with open('filejson.json') as json_file:
        book_collection = json.load(json_file)
    pages = list(chunked(book_collection, 10))
    os.makedirs('pages', exist_ok=True)
    for number, page in enumerate(pages, 1):
        books_divided = list(chunked(page, 2))
        rendered_page = template.render(
            books_divided=books_divided,
            current_page=number,
            last_page=len(pages),
        )
        with open(f'pages/index{number}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)

