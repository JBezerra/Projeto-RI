import re
from codecs import open as open_using_codecs
from bs4 import BeautifulSoup, Tag
import urllib.request

HTML_DIRECTORIES = {
  # 'BANGGOOD': './data/bangood.html',
  # 'KABUM': './data/kabum.html',
  'SUBMARINO': './data/submarino.html',
  'AMERICANAS': './data/americanas.html',
  'MAGAZINELUIZA': './data/magazineluiza.html',
  'AMAZON': './data/amazon.html',
  'CASASBAHIA': './data/casasbahia.html',
  'EBAY': './data/ebay.html',
  'ALIBABA': './data/alibaba.html',
  'FASTSHOP': './data/fastshop.html',
}

DESIRED_KEYS = []
def load_keys():
  with open('hot-words.txt','r') as file:
      for line in file:
          for word in line.split():
              DESIRED_KEYS.append(word)

def get_html(directory):
  file = open_using_codecs(directory, 'r', 'utf-8')
  html = BeautifulSoup(file.read(), features="html.parser")
  return html

load_keys()
html = get_html(HTML_DIRECTORIES['AMERICANAS'])

extracted_data = {}
for desired_key in DESIRED_KEYS:
  key_tags = html.find_all(text=desired_key)

  for key_tag in key_tags:
    if not (key_tag):
      continue

    key_tag = key_tag.parent
    while not(key_tag.next_sibling):
      key_tag = key_tag.parent

    sibling_exists = bool(key_tag.next_sibling)
    if sibling_exists:
      sibling = key_tag.next_sibling
      while not(isinstance(sibling, Tag) and sibling.text) and sibling.next_sibling:
        sibling = sibling.next_sibling

      if(sibling.text):
        extracted_data[desired_key.strip()] = (sibling.text).strip()
        print(desired_key.strip(), (sibling.text).strip())
