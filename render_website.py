import json
from jinja2 import Environment, FileSystemLoader, select_autoescape


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)
template = env.get_template('index.html')
with open('filejson.json') as json_file:
    book_collection = json.load(json_file)

rendered_page = template.render(books=book_collection)
with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)