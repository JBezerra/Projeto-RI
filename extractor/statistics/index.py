from specialist_extractors.amazon_extractor import extract as amazon_extractor
from specialist_extractors.americanas_extractor import extract as americanas_extractor
from specialist_extractors.casasbahia_extractor import extract as casasbahia_extractor
from specialist_extractors.colombo_extractor import extract as colombo_extractor
from specialist_extractors.ebay_extractor import extract as ebay_extractor
from specialist_extractors.fastshop_extractor import extract as fastshop_extractor
from specialist_extractors.girafa_extractor import extract as girafa_extractor
from specialist_extractors.magazineluiza_extractor import extract as magazineluiza_extractor
from specialist_extractors.submarino_extractor import extract as submarino_extractor
from specialist_extractors.webfone_extractor import extract as webfone_extractor

from domain_specific_extractor import extract
from domain_specific_extractor.helpers import get_html

HTML_DIRECTORIES = {
  'SUBMARINO': './data/submarino.html',
  'AMERICANAS': './data/americanas.html',
  'MAGAZINELUIZA': './data/magazineluiza.html',
  'AMAZON': './data/amazon.html',
  'CASASBAHIA': './data/casasbahia.html',
  'EBAY': './data/ebay.html',
  'FASTSHOP': './data/fastshop.html',
  'WEBFONE': './data/webfone.html',
  'COLOMBO': './data/colombo.html',
  'GIRAFA': './data/girafa.html',
}

def evaluate_extractors_result(domain_extractor_result, specific_extractor_result):
  keys_to_compare = []
  if len(domain_extractor_result) <= len(specific_extractor_result):
    keys_to_compare = domain_extractor_result.keys()
  else:
    keys_to_compare = specific_extractor_result.keys()
  score_count = 0
  for key in keys_to_compare:
    if (key in domain_extractor_result and key in specific_extractor_result)\
    and domain_extractor_result[key] == specific_extractor_result[key]:
      score_count += 1

  accuracy_pct = int(score_count)/len(keys_to_compare)
  data_diff = abs(len(domain_extractor_result) - len(specific_extractor_result))
  print(f'-----  Acurácia de {accuracy_pct*100}%')
  print(f'-----  Diferença de qtd. dados capturados: {data_diff}\n\n')

def evaluate_americanas():
  html = get_html(HTML_DIRECTORIES['AMERICANAS'])
  domain_extractor_result = extract(html)
  specific_extractor_result = americanas_extractor()
  print('-- AMERICANAS --')
  evaluate_extractors_result(domain_extractor_result, specific_extractor_result)

def evaluate_submarino():
  html = get_html(HTML_DIRECTORIES['SUBMARINO'])
  domain_extractor_result = extract(html)
  specific_extractor_result = submarino_extractor()
  print('-- SUBMARINO --')
  evaluate_extractors_result(domain_extractor_result, specific_extractor_result)

def evaluate_magazineluiza():
  html = get_html(HTML_DIRECTORIES['MAGAZINELUIZA'])
  domain_extractor_result = extract(html)
  specific_extractor_result = magazineluiza_extractor()
  print('-- MAGAZINE LUIZA --')
  evaluate_extractors_result(domain_extractor_result, specific_extractor_result)

def evaluate_amazon():
  html = get_html(HTML_DIRECTORIES['AMAZON'])
  domain_extractor_result = extract(html)
  specific_extractor_result = amazon_extractor()
  print('-- AMAZON --')
  evaluate_extractors_result(domain_extractor_result, specific_extractor_result)

def evaluate_casasbahia():
  html = get_html(HTML_DIRECTORIES['CASASBAHIA'])
  domain_extractor_result = extract(html)
  specific_extractor_result = casasbahia_extractor()
  print('-- CASAS BAHIA --')
  evaluate_extractors_result(domain_extractor_result, specific_extractor_result)

def evaluate_ebay():
  html = get_html(HTML_DIRECTORIES['EBAY'])
  domain_extractor_result = extract(html)
  specific_extractor_result = ebay_extractor()
  print('-- EBAY --')
  evaluate_extractors_result(domain_extractor_result, specific_extractor_result)

def evaluate_webfone():
  html = get_html(HTML_DIRECTORIES['WEBFONE'])
  domain_extractor_result = extract(html)
  specific_extractor_result = webfone_extractor()
  print('-- WEBFONE --')
  evaluate_extractors_result(domain_extractor_result, specific_extractor_result)

def evaluate_fastshop():
  html = get_html(HTML_DIRECTORIES['FASTSHOP'])
  domain_extractor_result = extract(html)
  specific_extractor_result = fastshop_extractor()
  print('-- FASTSHOP --')
  evaluate_extractors_result(domain_extractor_result, specific_extractor_result)

def evaluate_colombo():
  html = get_html(HTML_DIRECTORIES['COLOMBO'])
  domain_extractor_result = extract(html)
  specific_extractor_result = colombo_extractor()
  print('-- COLOMBO --')
  evaluate_extractors_result(domain_extractor_result, specific_extractor_result)

def evaluate_girafa():
  html = get_html(HTML_DIRECTORIES['GIRAFA'])
  domain_extractor_result = extract(html)
  specific_extractor_result = girafa_extractor()
  print('-- GIRAFA --')
  evaluate_extractors_result(domain_extractor_result, specific_extractor_result)

evaluate_americanas()
evaluate_submarino()
evaluate_magazineluiza()
evaluate_amazon()
evaluate_casasbahia()
evaluate_ebay()
evaluate_webfone()
evaluate_fastshop()
evaluate_colombo()
evaluate_girafa()
