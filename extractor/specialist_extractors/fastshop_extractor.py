import re
from specialist_extractors.helpers import load_keys, get_html

HTML_DIRECTORY = './data/fastshop.html'
DESIRED_KEYS = []
DESIRED_KEYS = load_keys()
extracted_data = {}

def extract(html = None):
  if not html:
    html = get_html(HTML_DIRECTORY)
  table_body = html.find('blockquote')
  table_body = table_body.find_all('p')
  for row in table_body:
    if not row.find('b'):
      continue
    key = row.find('b').text
    value = row.text[len(key)::]
    if key in DESIRED_KEYS:
      extracted_data[key] = value
  return extracted_data