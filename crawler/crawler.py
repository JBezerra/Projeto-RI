
"""Crawler exemplo usando webfones. O mesmo código rodou os outros sites do dominio:
samsung: https://colab.research.google.com/drive/16firwqulY0agOPWaIWvCmjHh5aMt1J2e?usp=sharing
webfones: https://colab.research.google.com/drive/1tQw749cDXcLszikVbEaYPXDrGyFyfefD?usp=sharing
girafas: https://colab.research.google.com/drive/1po12r9GzpfcUGWXtjZUXdaNTHwdBf6ZC?usp=sharing
imperio k7 (em manutenção): https://colab.research.google.com/drive/1NbjUov0SWUC_nCCW6ezHL9Ii5Jy0yJHR?usp=sharing
colombo: https://colab.research.google.com/drive/11-tfVot5tKrvUOvuqzSVF5HrwcpWLoln?usp=sharing
trocafone: https://colab.research.google.com/drive/1IdKwL_Lj4VAXQuYnyPFg5sma5m-bkn11?usp=sharing
UOL: https://colab.research.google.com/drive/1xH2zw3MIjIuUHpZWpJ2eUG14NnIraPSy#scrollTo=hrlPbYwkVgsv
magalu: https://colab.research.google.com/drive/1Sv4pG_BVBP1PR7At9XMpxv6Z3f84mrnx#scrollTo=hrlPbYwkVgsv
motorola: https://colab.research.google.com/drive/1SXvnRWZX38xZ5mNE5RPdetJoOIP-E1WU#scrollTo=hrlPbYwkVgsv
fastshop: https://colab.research.google.com/drive/1EY46fh8kIm8lTDbPh1kAN68hwEDkSEew#scrollTo=_Z3QsHuWFsA2
big: https://colab.research.google.com/drive/1YY0lQs8N_J5J2F22JP8jkZZIkpo2w8lq?usp=sharing
ferreira costa: https://colab.research.google.com/drive/1EY46fh8kIm8lTDbPh1kAN68hwEDkSEew?usp=sharing
"""

#print("CRAWLING BACK TO YOU\n\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n&&&&&&&&&&&&&&&&&&&&P!#&@?^&&&PP&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&PP&&#:?@&#!P&&&&&&&&&&&&&&&&&&&&\n&&&&&&&&&&&&&&&G~B&&! P@&^ B@#.:&&&B&&&&&&&&&&&&&&&&&&&&&&&&&&&&B&&&:.#@B ~&@P !&&B~G&&&&&&&&&&&&&&&\n&&&&&&&&&&&G#&@? Y@&^:J@#^.P@G::B@G Y@&&@&&&&&&&&&&&&&&&&&&@&&@Y.G@G::G@P.^#@J:^&@Y ?@&#G&&&&&&&&&&&\n&&&&&&@&&&P ?@&~^7@B^77@B^~Y@Y!~5@J.!&&#Y#&&&&&&&&&&&&&&&&#Y#&&!.J@5~!Y@Y~^B@77^B@7^~&@? P&&&@&&&&&&\n&&@&&&?Y&@?^~&#^?~@G^Y!@G~7?@??7J@!?^#@? J@&&&&&&&&&&&&&&@? ?@#^?!@J7??@?7~G@~Y^G@~?^&&~^?@&Y?&&&@&&\n&5Y&@P.:#&~Y^#B^5^&5~P^@5!Y!@!Y??&^P^B&~?~&&B~7&&B~7&#~7&#^J^&B^P^&?JY!@!Y~5&^P~5&^5^B#^Y~&#:.P@&Y5&\nP^^P@7?~P#^B^GG^B^#Y7B^&Y75~&~PY!#:B^G#^G^#@7J!Y@?7~PY~^BG^B^#P^B:#!YP~&~57Y&^B!Y#^B^GG^B^#P~?7@P^^P\n^PJ7@^G?JG^&!55~&^B??#:#??G^#^G5~G^&!5G^&^G#:#P^&!5Y~^G!5J7&^G5!&^G~PG^#^G??#:#??B^&~55!&^G??G^@7J5^\n?&G^P^&5!Y!@?JJ7@^P7Y&^B7YB^B^#G~5~@7JY!@!YY!@&^P^G&PG@??~5@!5J?@~5^G#^B^BY7B^&Y7P^@7Y??@!Y!5&^P^B&?\n&&&J~5@B^~J@Y!7J@!Y~5&^G~5#^P^#B^?7@Y7??@5^^P&@J^^#&@&@5.^#@??!Y@7?^B#^P^#5~G^&5~Y!@J7!Y@J~^B@5~J&&&\n&&&&&&&&~ G@P^~5@7?~G@~5^G&^J~&#^~J@P^^5@&YP&&&&YP&&&&&&YG&@5^^G@J~^#&~J^&G~5~@G~?7@5~^G@G ~&&&&&&&&\n&&&&&&&&G5&&#:.B@Y~^B@!?^B&~!!&&^.P@#::#&&@&&&&&@&&&&&&&@&&&#::#@P.^&&!!~&B^?!@B^~Y@B.:#&&5G&&&&&&&&\n&&&&&&&&&@&&&!^&@P.^&@?~^#@7 ?@&~ B&&GG&&&&&&&&&&&&&&&&&&&&&&GG&&B ~&@? 7@#^~?@&^.P@&^!&&&@&&&&&&&&&\n&&&&&&&&&&&&&##&&B !&@5 ~&@J Y@&Y7&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&!Y&@Y J@&~ 5@&! #&&##&&&&&&&&&&&&&\n&&&&&&&&&&&&&&&&&&PG&&B.J@&G~B&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B~G&@J.B&&GP&&&&&&&&&&&&&&&&&&\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

import requests
import re

roots = []
roots.append("http://www.webfones.com.br")

rootNames = ["webfones"]


frontier = []
downloaded = []
crawled = []
exceptions = []

concat = ""
nArquivos = 0
exceptions = []



def robots(self):
    try:
        r = requests.get(self + "/robots.txt")
        html = r.text.encode("utf8")
        string = str(html)
        string = string.split("User-agent: *\\n")
        string = string[1]    
        string = string.replace("\\n", "")
        string = string.replace("*", "")
        string = string.split("Disallow: ")
        for item in string:
            if item is not '':
                exceptions.append(item)
        print("robot success")

    except:
        print("robot error")


class Node:                                                                     #nó da árvore
    def __init__(self, link, html):
        self.link = link
        self.html = html
        self.children = []
        self.fronteira = []


def insert(self, children):                                                     #insert criança
    try:
        r = requests.get(children)
        html = r.text.encode("utf8")
        self.children.append(Node(children, html))
        
    except:
        print("insert except")


def seek(self, link):                                                           #procurar um link na árvore pra visitar fazer o crawling a partir dele
    if self.link == link:
        return self
    else:
        for children in self.children:
            return seek(children, children.link)

nodeList = []
for item in roots:                                                              #cria uma árvore por root
    print(item)
    r = requests.get(item)                                                      #baixa html de cada root
    html = r.text.encode("utf8")
    nodeList.append(Node(item, html))                                           #cria e salva nó (uma árvore por root)
    f = open("root.txt",'w')
    f.write(html.decode("utf8"))
    f.close()



def crawl(self):                                                                #pega o link e html do nó, procura todos links na página e adiciona na fronteira e árvore
    crawled.append(self.link)
    root = self.link
    html = self.html
    print("now crawling:", root)

    try:
      search1 = re.findall(r'href=[\'"?](http[://\w\-._]+)', html.decode("utf8"))
      for link in search1:
          if link not in exceptions:
              for item in rootNames:
                  if len(frontier) < 1000:
                      if item in link and link not in downloaded and link not in crawled:
                          if not any(excecao in link for excecao in exceptions):
                              if link not in frontier:
                                  print(link)
                                  frontier.append(link)
                                  insert(self, link)                                      #inserir como filho (vai baixar MUITOS html)
                                  downloaded.append(link)

    except:
      pass
    try:
      search2 = re.findall(r'src=[\'"?](http[://\w\-._]+)', html.decode("utf8"))
      for link in search2:
          if link not in exceptions:
              for item in rootNames:
                  if len(frontier) < 1000:
                      if item in link and link not in downloaded and link not in crawled:
                          if not any(excecao in link for excecao in exceptions):
                              if link not in frontier:
                                  print(link)
                                  frontier.append(link)
                                  insert(self, link)                                      #inserir como filho (vai baixar MUITOS html)
                                  downloaded.append(link)

    except:
      pass



def rec(self):
    crawl(self)
    for item in self.children:
        crawl(item)

for item in nodeList:
    frontier = []

    exceptions = ["whatsapp", "facebook", "instagram", "jpg", "png", "jpeg", "youtube", "img"]
    robots(item.link)
    crawl(item)
    for it in item.children:
        rec(it)

    concat = ''
    for item in frontier:
        concat = concat + "\n" + item
    f = open("concat.txt", "w")
    f.write(concat)
    f.close()

    print("Fim do", item, " e todos seus filhos. Tamanho da fronteira: ", len(frontier))


