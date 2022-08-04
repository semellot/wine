from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

import datetime
import pandas
from pprint import pprint
import collections

def get_year():
    today = datetime.datetime.now()
    year = today.year - 1920
    if year % 10 == 1 and year != 11 and year % 100 != 11:
        text_year = "год"
    elif 1 < year % 10 <= 4 and year != 12 and year != 13 and year != 14:
        text_year = "года"
    else:
        text_year = "лет"
    return f'{year} {text_year}'

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

excel_data_df = pandas.read_excel('wine3.xlsx', sheet_name='Лист1', na_values=['N/A', 'NA'], keep_default_na=False)
wines = excel_data_df.to_dict(orient='records')
wines_by_category = collections.defaultdict(list)
for wine in wines:
    category = wine['Категория']
    wines_by_category[category].append(wine)

rendered_page = template.render(
    year=get_year(),
    wines_by_category=wines_by_category
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
