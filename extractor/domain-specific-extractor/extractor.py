import re
from codecs import open as open_using_codecs
from bs4 import BeautifulSoup, Tag
import urllib.request
from helpers import load_keys

HTML_DIRECTORIES = {
  'SUBMARINO': '../data/submarino.html',
  'AMERICANAS': '../data/americanas.html',
  'MAGAZINELUIZA': '../data/magazineluiza.html',
  'AMAZON': '../data/amazon.html',
  'CASASBAHIA': '../data/casasbahia.html',
  'EBAY': '../data/ebay.html',
  'FASTSHOP': '../data/fastshop.html',
  'WEBFONE': '../data/webfone.html',
  'COLOMBO': '../data/colombo.html',
  'GIRAFA': '../data/girafa.html',
}
DESIRED_KEYS = []
EXTRACTION = {}

def get_html(directory):
  file = open_using_codecs(directory, 'r', 'utf-8')
  html = BeautifulSoup(file.read(), features="html.parser")
  return html

def extract():
  html = get_html(HTML_DIRECTORIES['FASTSHOP'])
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
          desired_key = re.sub('[^A-Za-z\u00C0-\u024F0-9 ,.]+', '', desired_key).strip()
          sibling_text = re.sub('[^A-Za-z\u00C0-\u024F0-9 ,.]+[ ]+', '', sibling.text).strip()
          sibling_text = sibling_text.replace('\u200e', '')
          EXTRACTION[desired_key] = sibling_text

DESIRED_KEYS = load_keys()
extract()
print(EXTRACTION)