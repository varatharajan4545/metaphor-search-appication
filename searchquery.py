from elasticsearch import Elasticsearch

from query import basic_search, exact_search, wild_card_search, multi_match

# from rules import process

INDEX = 'harris_ar_songlyrics2'
client = Elasticsearch(HOST="http://localhost", PORT=9200)


# def search(query):
#     # result = client. (index=INDEX,body=standard_analyzer(query))
#     # keywords = result ['tokens']['token']
#     # print(keywords)
#
#     # query_body= process(query)
#     query_body = basic_search(query)
#     print('Making Basic Search ')
#     res = client.search(index=INDEX, body=query_body)
#     return res
def process_query(query):
    # if any(word in query for word in top_words):
    #     print("Best search query")
    #     query_body = best_search(query)
    if '''”''' in query or '''"''' in query:
        print("Exact search query")
        query_body = exact_search(query)
    elif '*' in query:
        print("wild card search query")
        query_body = wild_card_search(query)
        print(query_body)
    elif '@' in query:
        print("multi search query")
        query_body = multi_match(query)
        print(query_body)
    else:
        print("basic search query")
        query_body = basic_search(query)
    return query_body


def search(query):
    query_body = process_query(query)
    print('Searching...')
    resp = client.search(index=INDEX, body=query_body)
    return resp
