from specialist_extractors.helpers import load_keys, get_html

HTML_DIRECTORY = './data/webfone.html'
DESIRED_KEYS = []
DESIRED_KEYS = load_keys()
extracted_data = {}

def extract(html = None):
  if not html:
    html = get_html(HTML_DIRECTORY)
  table_body = html.find('table')
  table_body = table_body.find_all('tr')
  for row in table_body:
    key = row.find('th').text
    value = row.find('td').text
    if key in DESIRED_KEYS:
      extracted_data[key] = value
  return extracted_data