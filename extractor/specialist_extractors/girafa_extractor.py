import re
from specialist_extractors.helpers import load_keys, get_html

HTML_DIRECTORY = './data/girafa.html'
DESIRED_KEYS = []
DESIRED_KEYS = load_keys()
extracted_data = {}

def extract(html = None):
  if not html:
    html = get_html(HTML_DIRECTORY)
  table_body = html.find('table')
  table_body = table_body.find_all('tr')
  for row in table_body:
    isntance = row.find_all('td')
    key = isntance[0].text
    value = isntance[1].text
    key = re.sub('[^A-Za-z\u00C0-\u024F0-9]+ ', '', key).strip()
    value = re.sub('[^A-Za-z\u00C0-\u024F0-9]+ ', '', value).strip()
    if key in DESIRED_KEYS:
      extracted_data[key.strip()] = value.replace('\u200e', '')
  return extracted_data