# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pYi18JH0Hxg0XTvFXSG6sZ_GfGAXhGwt
"""

#print("CRAWLING BACK TO YOU\n\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n&&&&&&&&&&&&&&&&&&&&P!#&@?^&&&PP&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&PP&&#:?@&#!P&&&&&&&&&&&&&&&&&&&&\n&&&&&&&&&&&&&&&G~B&&! P@&^ B@#.:&&&B&&&&&&&&&&&&&&&&&&&&&&&&&&&&B&&&:.#@B ~&@P !&&B~G&&&&&&&&&&&&&&&\n&&&&&&&&&&&G#&@? Y@&^:J@#^.P@G::B@G Y@&&@&&&&&&&&&&&&&&&&&&@&&@Y.G@G::G@P.^#@J:^&@Y ?@&#G&&&&&&&&&&&\n&&&&&&@&&&P ?@&~^7@B^77@B^~Y@Y!~5@J.!&&#Y#&&&&&&&&&&&&&&&&#Y#&&!.J@5~!Y@Y~^B@77^B@7^~&@? P&&&@&&&&&&\n&&@&&&?Y&@?^~&#^?~@G^Y!@G~7?@??7J@!?^#@? J@&&&&&&&&&&&&&&@? ?@#^?!@J7??@?7~G@~Y^G@~?^&&~^?@&Y?&&&@&&\n&5Y&@P.:#&~Y^#B^5^&5~P^@5!Y!@!Y??&^P^B&~?~&&B~7&&B~7&#~7&#^J^&B^P^&?JY!@!Y~5&^P~5&^5^B#^Y~&#:.P@&Y5&\nP^^P@7?~P#^B^GG^B^#Y7B^&Y75~&~PY!#:B^G#^G^#@7J!Y@?7~PY~^BG^B^#P^B:#!YP~&~57Y&^B!Y#^B^GG^B^#P~?7@P^^P\n^PJ7@^G?JG^&!55~&^B??#:#??G^#^G5~G^&!5G^&^G#:#P^&!5Y~^G!5J7&^G5!&^G~PG^#^G??#:#??B^&~55!&^G??G^@7J5^\n?&G^P^&5!Y!@?JJ7@^P7Y&^B7YB^B^#G~5~@7JY!@!YY!@&^P^G&PG@??~5@!5J?@~5^G#^B^BY7B^&Y7P^@7Y??@!Y!5&^P^B&?\n&&&J~5@B^~J@Y!7J@!Y~5&^G~5#^P^#B^?7@Y7??@5^^P&@J^^#&@&@5.^#@??!Y@7?^B#^P^#5~G^&5~Y!@J7!Y@J~^B@5~J&&&\n&&&&&&&&~ G@P^~5@7?~G@~5^G&^J~&#^~J@P^^5@&YP&&&&YP&&&&&&YG&@5^^G@J~^#&~J^&G~5~@G~?7@5~^G@G ~&&&&&&&&\n&&&&&&&&G5&&#:.B@Y~^B@!?^B&~!!&&^.P@#::#&&@&&&&&@&&&&&&&@&&&#::#@P.^&&!!~&B^?!@B^~Y@B.:#&&5G&&&&&&&&\n&&&&&&&&&@&&&!^&@P.^&@?~^#@7 ?@&~ B&&GG&&&&&&&&&&&&&&&&&&&&&&GG&&B ~&@? 7@#^~?@&^.P@&^!&&&@&&&&&&&&&\n&&&&&&&&&&&&&##&&B !&@5 ~&@J Y@&Y7&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&!Y&@Y J@&~ 5@&! #&&##&&&&&&&&&&&&&\n&&&&&&&&&&&&&&&&&&PG&&B.J@&G~B&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B~G&@J.B&&GP&&&&&&&&&&&&&&&&&&\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

import requests
import re

roots = []
#roots.append("http://www.americanas.com.br") #nao baixou
#roots.append("http://www.submarino.com.br") #nao baixou
#roots.append("http://www.casasbahia.com.br") #nao baixou
roots.append("http://www.fastshop.com.br")
#roots.append("http://www.carrefour.com.br") #nao achou links
#roots.append("http://www.banggood.com") #nao achou links
#roots.append("http://www.kabum.com.br") #nao achou links
roots.append("http://www.amazon.com.br")
#roots.append("http://www.ebay.com.br") #loopou depois de alguns links
roots.append("http://www.alibaba.com.br")
roots.append("http://www.magazineluiza.com.br")
roots.append("http://www.efacil.com.br")
roots.append("http://girafa.com.br")
roots.append("http://www.onofreagora.com.br")
roots.append("http://www.bemol.com.br")
roots.append("http://www.webfones.com.br")
roots.append("http://www.meupositivo.com.br")


rootNames = ["americanas", "submarino", "casasbahia", "fastshop", "carrefour", "banggod", "kabum", "amazon", "ebay", "alibaba", "magazineluiza", "efacil", "girafa", "onofre", "agora", "bemol", "webfones", "extra", "positivo"]

frontier = []
downloaded = []
crawled = []
exceptions = []

exceptions = ["https://listadecasamento.efacil.com.br/ListaPresentes.aspx"]     #links que deram erro e n??o consegui resolver ainda

class Node:                                                                     #n?? da ??rvore
    def __init__(self, link, html):
        self.link = link
        self.html = html
        self.children = []

def PrintTreePreorder(self):                                                    #print em profundidade (debug only)
    print(self.link)
    for item in self.children:
        PrintTreePreorder(item)

def insert(self, children):                                                     #insert crian??a
    try:
        r = requests.get(children)
        html = r.text.encode("utf8")
        self.children.append(Node(children, html))
    except:
        print("insert except")


def seek(self, link):                                                           #procurar um link na ??rvore pra visitar fazer o crawling a partir dele
    if self.link == link:
        return self
    else:
        for children in self.children:
            return seek(children, children.link)

nodeList = []
for item in roots:                                                              #cria uma ??rvore por root
    print(item)
    r = requests.get(item)                                                      #baixa html de cada root
    html = r.text.encode("utf8")
    nodeList.append(Node(item, html))                                           #cria e salva n?? (uma ??rvore por root)



def crawl(self):                                                                #pega o link e html do n??, procura todos links na p??gina e adiciona na fronteira e ??rvore
    crawled.append(self.link)
    root = self.link
    html = self.html
    print("now crawling:", root)

    search = re.findall(r'href=[\'"?](http[://\w\-._]+)', html.decode("utf8"))
    for link in search:
        if link not in exceptions:
            for item in rootNames:
                if item in link and link not in downloaded and link not in crawled:
                    frontier.append(link)
                    print("link novo: ", link)
                    insert(self, link)                                      #inserir como filho (vai baixar MUITOS html)
                    downloaded.append(link)

    search = []
    search = re.findall(r'src=[\'"?](http[://\w\-._]+)', html.decode("utf8"))
    for link in search:
        if link not in exceptions:
            for item in rootNames:
                if item in link and link not in downloaded and link not in crawled:
                    frontier.append(link)
                    print("link novo: ", link)
                    insert(self, link)                                      #inserir como filho (vai baixar MUITOS html)
                    downloaded.append(link)

    

for item in nodeList:
    crawl(item)
    for children in frontier:
        found = seek(item, children)
        if found:
            print("==============================================================================================================================================================")
            print("children: ", children)
            crawl(found)

print(len(frontier))
print(len(downloaded))
print(len(crawled))

from bs4 import BeautifulSoup
linksProdutos = []

for item in downloaded:

    url = item
    try:
        response = requests.get(url)
    except:
        print("NoneType encontrado")

    if 'webfones' in item:
        try:
            site = BeautifulSoup(response.text, 'html.parser')
            produto = site.findAll('div', attrs={'class': 'x-group'})
            for prod in produto:
                stringProduto = str(prod)

                link = stringProduto.split('href="')
                link = link[1].split(' ')
                link = link[0]
                
                if link not in linksProdutos:
                    linksProdutos.append(link)
        except:
            print("NoneType encontrado")
"""
    elif 'magazineluiza' in item:
        try:
            site = BeautifulSoup(response.text, 'html.parser')
            produto = site.findAll('div', attrs={'class': 'sc-hKwDye bbqWyp sc-UMyrj eVrEIK'}) 
            print(produto)
            for prod in produto:
                stringProduto = str(prod)
                print(stringProduto)
        except:
            print("NoneType encontrado")
"""

print(len(linksProdutos))

for link in linksProdutos:
    print(link)

