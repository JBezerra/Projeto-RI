import re
from helpers import load_keys, get_html

HTML_DIRECTORY = '../data/amazon.html'
DESIRED_KEYS = []
extracted_data = {}

def extract():
  html = get_html(HTML_DIRECTORY)
  table_body = html.find('table', id='productDetails_techSpec_section_1').tbody
  table_body = table_body.find_all('tr')
  for row in table_body:
    key = row.find('th').text
    value = row.find('td').text
    key = re.sub('[^A-Za-z0-9]+ ', '', key)
    value = re.sub('[^A-Za-z0-9]+ ', '', value)
    if key in DESIRED_KEYS:
      extracted_data[key.strip()] = value.replace('\u200e', '')



DESIRED_KEYS = load_keys()
extract()
print(extracted_data)