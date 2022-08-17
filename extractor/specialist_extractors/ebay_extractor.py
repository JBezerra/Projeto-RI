from specialist_extractors.helpers import load_keys, get_html

HTML_DIRECTORY = './data/ebay.html'
DESIRED_KEYS = []
DESIRED_KEYS = load_keys()
extracted_data = {}

def extract(html = None):
  if not html:
    html = get_html(HTML_DIRECTORY)
  specs = html.find('div', {'class': 'ux-layout-section ux-layout-section--features'})
  specs = specs.find_all('span',{'class': 'ux-textspans'})
  specs_len = len(specs)
  for index in range(0, specs_len, 2):
    key = specs[index].text
    value = specs[index+1].text
    if key in DESIRED_KEYS:
      key = key.replace(':', '')
      extracted_data[key] = value
  return extracted_data