from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

import datetime
import pandas
import collections
import argparse


def get_age():
    today = datetime.datetime.now()
    foundation_year = 1920
    number_years = today.year - foundation_year
    if number_years % 10 == 1 and number_years % 100 != 11 and number_years != 11:
        year_word = "год"
    elif 1 < number_years % 10 <= 4 and number_years not in [12,13,14]:
        year_word = "года"
    else:
        year_word = "лет"
    return f'{number_years} {year_word}'

if __name__ == '__main__':
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default='wine.xlsx')
    parser.add_argument('--sheet', default='Лист1')
    args = parser.parse_args()
    excel_data_df = pandas.read_excel(args.file, sheet_name=args.sheet, na_values=['N/A', 'NA'], keep_default_na=False)

    wines = excel_data_df.to_dict(orient='records')
    wines_by_category = collections.defaultdict(list)
    for wine in wines:
        category = wine['Категория']
        wines_by_category[category].append(wine)

    rendered_page = template.render(
        year=get_age(),
        wines_by_category=wines_by_category
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
