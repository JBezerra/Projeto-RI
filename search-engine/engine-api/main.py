import math
import json
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

f = open("./indice-invertido.json", "r")
indice_invertido = json.load(f)

f = open("./indice-invertido-avancado.json", "r")
indice_invertido_avancado = json.load(f)

with open("./htmls.txt", "r") as file:
  lines = file.readlines()
  lines = [line.rstrip() for line in lines]
URLS = lines

def busca_ranqueada(pesquisa, dados_indice_invertido, total_documentos_retornados):
    array_palavras_pesquisa = pesquisa.split()
    quant_palavras_pesquisa = len(array_palavras_pesquisa)
    # (somatória quadrática do peso das palavras da busca para o documento [denominador esquerdo do cálculo do cosseno], somatório da multiplicação entre o peso do termo no documento e o peso do termo na busca [numerador do cálculo do cosseno])
    score_documentos = [(0, 0)] * total_documentos_retornados
    somatorio_termos_busca = 0
    # term-at-time
    for i in range(quant_palavras_pesquisa):
        palavra = array_palavras_pesquisa[i]
        if palavra in dados_indice_invertido.keys():
            freq_nos_docs = dados_indice_invertido[palavra]['freqDocs']
            documentos_freq = dados_indice_invertido[palavra]['docs']

            pesquisa_palavra_idf = math.log(total_documentos_retornados / freq_nos_docs)
            # considerando apenas o idf para a consulta
            # [denominador direito do cálculo do cosseno]
            somatorio_termos_busca += pesquisa_palavra_idf ** 2

            for j in range(freq_nos_docs):
                indice_documento = documentos_freq[j][0]
                freq_documento = documentos_freq[j][1]
                tfidf = freq_documento * pesquisa_palavra_idf
                score_documento = score_documentos[indice_documento - 1]
                score_documentos[indice_documento - 1] = (
                    score_documento[0] + tfidf ** 2, score_documento[1] + (tfidf * pesquisa_palavra_idf))

    # (indice do documento, rank do documento)
    rank_scores = []
    for x in range(total_documentos_retornados):
        score = 0
        if score_documentos[x][0] != 0:
            score = (score_documentos[x][1] / math.sqrt(
                score_documentos[x][0] * somatorio_termos_busca))

        if (score > 0):
            if len(rank_scores) > 0:
                for n in range(len(rank_scores)):
                    if (score > rank_scores[n][1]):
                        rank_scores.insert(n, (x + 1, score))
                        break

                    if n == len(rank_scores) - 1:
                        rank_scores.append((x + 1, score))

            else:
                rank_scores.append((x + 1, score))
        else:
            rank_scores.append((x + 1, score))

    return rank_scores[:total_documentos_retornados]

def search_core(query):
    rank_tfidf = busca_ranqueada(query, indice_invertido, 557)
    top_5_rank = rank_tfidf[0:5]
    urls = []
    for (url_index, rank) in top_5_rank:
        url = URLS[url_index]
        urls.append(url)
    return urls

def advanced_search_core(query):
    pesquisa_geral = "xiaomi.marca 128gb.armazenamento"
    pesquisa_geral = "xiaomi.marca 64gb.armazenamento"
    rank_tfidf = busca_ranqueada(query, indice_invertido_avancado, 557)
    top_5_rank = rank_tfidf[0:5]
    urls = []
    for (url_index, rank) in top_5_rank:
        url = URLS[url_index]
        urls.append(url)
    return urls


app = Flask(__name__)
CORS(app, resources={r'/*' : {'origins': '*'}})

@app.route('/search/')
def search():
    args = request.args.to_dict()
    query = args['query']
    search_results = search_core(query)
    response = jsonify(search_results)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/advanced-search/')
def advanced_search():
    args = request.args.to_dict()
    marca = args['marca']
    armazenamento = args['armazenamento']
    memoria = args['memoria']
    search_results = advanced_search_core(f"{marca}.marca {armazenamento}.armazenamento")
    response = jsonify(search_results)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001", debug=True)