import re
from specialist_extractors.helpers import load_keys, get_html

HTML_DIRECTORY = './data/colombo.html'
DESIRED_KEYS = []
DESIRED_KEYS = load_keys()
extracted_data = {}

def extract(html = None):
  if not html:
    html = get_html(HTML_DIRECTORY)
  prod_specs = html.find('div', { 'class': 'caracteristicas-produto'})
  specs = prod_specs.find_all('div', {'class':'caracteristicas-content caracteristicas-tecnicas'})
  divs = specs[1].find_all('div', { 'class': 'caracteristicas-row'})
  for row in divs:
    instance = row.find_all('div')
    key = instance[0].span.text
    value = instance[1].span.text
    key = re.sub('[^A-Za-z0-9]+ ', '', key)
    value = re.sub('[^A-Za-z0-9]+ ', '', value)
    if key in DESIRED_KEYS:
      key = key.replace(':', '')
      extracted_data[key.strip()] = value.replace('\u200e', '')
  return extracted_data
