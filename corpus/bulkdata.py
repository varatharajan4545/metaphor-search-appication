import json
from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch(['http://localhost:9200'])

# Read JSON file
with open('180660v_corpus.json', 'r', encoding='utf-8') as json_file:
    json_array = json.load(json_file)

# Index documents in Elasticsearch
for doc in json_array:
    res = es.index(index='harris_ar_songlyrics2', document=doc)
    print(res)