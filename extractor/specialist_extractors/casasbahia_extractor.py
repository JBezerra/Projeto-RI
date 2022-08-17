import re
from specialist_extractors.helpers import load_keys, get_html

HTML_DIRECTORY = './data/casasbahia.html'
DESIRED_KEYS = []
DESIRED_KEYS = load_keys()
extracted_data = {}

def extract(html = None):
  if not html:
    html = get_html(HTML_DIRECTORY)
  specs = html.find_all(id=re.compile('product-detail-list-'))
  for spec in specs:
    divs = spec.find_all('div')
    for row in divs:
      spans = row.find_all('span')
      key = spans[0].text
      value = spans[1].text
      if key in DESIRED_KEYS:
        extracted_data[key] = value
  return extracted_data