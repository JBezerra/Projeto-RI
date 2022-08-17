from specialist_extractors.helpers import load_keys, get_html

HTML_DIRECTORY = './data/americanas.html'
DESIRED_KEYS = []
DESIRED_KEYS = load_keys()
extracted_data = {}

def extract(html = None):
  if not html:
    html = get_html(HTML_DIRECTORY)
  table_body = html.find('table').tbody

  for row in table_body.children:
    instances = row.find_all('td')
    key = instances[0].text
    if key in DESIRED_KEYS:
      value = instances[1].text
      extracted_data[key] = value
  return extracted_data