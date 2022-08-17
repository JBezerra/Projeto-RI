from helpers import load_keys, get_html

HTML_DIRECTORY = '../data/americanas.html'
DESIRED_KEYS = []
extracted_data = {}

def extract():
  html = get_html(HTML_DIRECTORY)
  table_body = html.find('table').tbody

  for row in table_body.children:
    instances = row.find_all('td')
    key = instances[0].text
    if key in DESIRED_KEYS:
      value = instances[1].text
      extracted_data[key] = value


DESIRED_KEYS = load_keys()
extract()
print(extracted_data)